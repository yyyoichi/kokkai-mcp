import asyncio
from datetime import timedelta, datetime
from pathlib import Path
from typing import AsyncGenerator
import hishel
import httpx
from src.config import KokkkaiAPIRequestConfig, SpeechRequestParam
from src.kokkaiapiclient.api.speech.get_record_packing_query_parameter_type import GetRecordPackingQueryParameterType
from src.kokkaiapiclient.api.speech.speech_get_response import SpeechGetResponse
from src.kokkaiapiclient.api.speech.speech_request_builder import SpeechRequestBuilder
from src.kokkaiapiclient.api_client import ApiClient
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider)
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.headers_collection import HeadersCollection

def get_client() -> ApiClient:
    cache_client = hishel.AsyncCacheClient(
        transport=httpx.AsyncHTTPTransport(retries=3),
        storage=hishel.AsyncFileStorage(base_path=Path("/tmp/.cache")),
        controller=hishel.Controller(
            cacheable_methods=["GET"],
            cacheable_status_codes=[200],
            force_cache=True,
        ),
    )
    return ApiClient(request_adapter=HttpxRequestAdapter(authentication_provider=AnonymousAuthenticationProvider(), http_client=cache_client))

def get_client_no_cache() -> ApiClient:
    return ApiClient(request_adapter=HttpxRequestAdapter(authentication_provider=AnonymousAuthenticationProvider()))

class Client():
    """
    Client class for interacting with the Kokkkai API.
    """
    def __init__(self, config: KokkkaiAPIRequestConfig = KokkkaiAPIRequestConfig()):
        self.config = config.regularize()
        if self.config.use_cache:
            self.client = get_client()
        else:
            self.client = get_client_no_cache()

    async def iter_speech(self, p: SpeechRequestParam) -> AsyncGenerator[SpeechGetResponse, None]:
        request_enable = datetime.now()
        has_next = True
        param = SpeechRequestBuilder.SpeechRequestBuilderGetQueryParameters(
            start_record=1,
            maximum_records=100,
            from_=p.from_date.isoformat(),
            until=p.until_date.isoformat(),
            record_packing=GetRecordPackingQueryParameterType.Json,
            speaker= " ".join(p.speaker) if p.speaker is not None else None,
        )

        while has_next:
            speech: SpeechGetResponse | None = None

            if self.config.refer_cache == True:
                # ストレージから引く
                h = HeadersCollection()
                h.try_add("Cache-Control", "only-if-cached")
                conf = RequestConfiguration[SpeechRequestBuilder.SpeechRequestBuilderGetQueryParameters](headers=h, query_parameters=param)
                try:
                    speech = await self.client.api.speech.get(request_configuration=conf)
                except Exception as e:
                    # print("ストレージから取得できませんでした。", e)
                    pass
            # キャッシュが存在したかどうか
            exists_cache = speech is not None
            if speech is None:
                
                h = HeadersCollection()
                if self.config.refer_cache == False:
                    h.try_add("Cache-Control", "no-cache")
                conf = RequestConfiguration[SpeechRequestBuilder.SpeechRequestBuilderGetQueryParameters](headers=h, query_parameters=param)
                # もし現在時刻がreuqest_enableに満たなければその時間まで待機する
                diff = datetime.now() - request_enable
                if diff.microseconds < 0:
                    await asyncio.sleep(float(diff.microseconds) / 1000000.0)
                try:
                    speech = await self.client.api.speech.get(request_configuration=conf)
                    # 次に取得可能な日時を設定する。
                    request_enable = datetime.now() + timedelta(milliseconds=self.config.interval_milsec)
                except Exception as e:
                    print("取得に失敗しました", e)
                    break
                
            if speech is None or speech.speech_response is None:
                print("取得できませんでした")
                break

            print(f"取得件数: {param.start_record}-> {speech.speech_response.number_of_return} /{speech.speech_response.number_of_records} {"use cache" if exists_cache else ""}") # type: ignore
            has_next = speech.speech_response.next_record_position is not None
            if has_next:
                # 次の取得位置を設定する
                param.start_record = speech.speech_response.next_record_position.integer # type: ignore
            yield speech
            
