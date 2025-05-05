from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.name_of_house import NameOfHouse
    from ...models.search_range import SearchRange
    from ...models.speaker_role import SpeakerRole
    from .get_record_packing_query_parameter_type import GetRecordPackingQueryParameterType
    from .meeting_get_response import MeetingGetResponse

class MeetingRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/meeting
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MeetingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/meeting{?any,closing,contentsAndIndex,from,issueFrom,issueID,issueTo,maximumRecords,nameOfHouse,nameOfMeeting,recordPacking,searchRange,sessionFrom,sessionTo,speaker,speakerGroup,speakerPosition,speakerRole,speechID,speechNumber,startRecord,supplementAndAppendix,until}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MeetingRequestBuilderGetQueryParameters]] = None) -> Optional[MeetingGetResponse]:
        """
        会議単位出力
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MeetingGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .meeting_get_response import MeetingGetResponse

        return await self.request_adapter.send_async(request_info, MeetingGetResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MeetingRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        会議単位出力
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MeetingRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MeetingRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MeetingRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MeetingRequestBuilderGetQueryParameters():
        """
        会議単位出力
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "contents_and_index":
                return "contentsAndIndex"
            if original_name == "issue_from":
                return "issueFrom"
            if original_name == "issue_i_d":
                return "issueID"
            if original_name == "issue_to":
                return "issueTo"
            if original_name == "maximum_records":
                return "maximumRecords"
            if original_name == "name_of_house":
                return "nameOfHouse"
            if original_name == "name_of_meeting":
                return "nameOfMeeting"
            if original_name == "record_packing":
                return "recordPacking"
            if original_name == "search_range":
                return "searchRange"
            if original_name == "session_from":
                return "sessionFrom"
            if original_name == "session_to":
                return "sessionTo"
            if original_name == "speaker_group":
                return "speakerGroup"
            if original_name == "speaker_position":
                return "speakerPosition"
            if original_name == "speaker_role":
                return "speakerRole"
            if original_name == "speech_i_d":
                return "speechID"
            if original_name == "speech_number":
                return "speechNumber"
            if original_name == "start_record":
                return "startRecord"
            if original_name == "supplement_and_appendix":
                return "supplementAndAppendix"
            if original_name == "any":
                return "any"
            if original_name == "closing":
                return "closing"
            if original_name == "from_":
                return "from_"
            if original_name == "speaker":
                return "speaker"
            if original_name == "until":
                return "until"
            return original_name
        
        # 発言部分を検索対象とするキーワードを指定します。複数語はスペース区切りでAND検索になります。省略可。
        any: Optional[str] = None

        # 閉会中の会議録を限定検索するかを指定します。省略時はfalse（限定しない）となります。
        closing: Optional[bool] = None

        # 目次・索引を検索対象に限定するかを指定します。省略時はfalse（限定しない）となります。
        contents_and_index: Optional[bool] = None

        # 開催日付の範囲開始日をYYYY-MM-DD形式で指定します。省略可。
        from_: Optional[str] = None

        # 号数の開始号を指定します。省略可。
        issue_from: Optional[int] = None

        # 会議録IDを21桁の英数字で指定します。完全一致検索。省略可。
        issue_i_d: Optional[str] = None

        # 号数の終了号を指定します。省略可。
        issue_to: Optional[int] = None

        # 返戻件数の最大数を指定します。（会議単位簡易出力・発言単位出力:1～100、会議単位出力:1～10）。省略時はデフォルト件数で返戻します。
        maximum_records: Optional[int] = None

        # 検索対象の院名を指定します。省略可。
        name_of_house: Optional[NameOfHouse] = None

        # 検索対象の会議名を部分一致で指定します。複数語はスペース区切りでOR検索になります。省略可。
        name_of_meeting: Optional[str] = None

        # 応答形式を指定します。'xml'または'json'。省略時は'json'となります。
        record_packing: Optional[GetRecordPackingQueryParameterType] = None

        # 検索対象箇所を指定します。"冒頭","本文","冒頭・本文"のいずれかを指定可能です。省略時は"冒頭・本文"となります。
        search_range: Optional[SearchRange] = None

        # 国会回次の開始回を指定します。省略可。
        session_from: Optional[int] = None

        # 国会回次の終了回を指定します。省略可。
        session_to: Optional[int] = None

        # 発言者名を部分一致で指定します。複数語はスペース区切りでOR検索になります。省略可。
        speaker: Optional[str] = None

        # 発言者所属会派を部分一致で指定します。省略可。
        speaker_group: Optional[str] = None

        # 発言者肩書きを部分一致で指定します。省略可。
        speaker_position: Optional[str] = None

        # 発言者役割を指定します。"証人","参考人","公述人"のいずれかを指定可能です。省略可。
        speaker_role: Optional[SpeakerRole] = None

        # 発言IDを"issueID_発言番号"形式で指定します。完全一致検索。省略可。
        speech_i_d: Optional[str] = None

        # 発言番号を整数で指定します。完全一致検索。省略可。
        speech_number: Optional[int] = None

        # 検索結果の開始位置を指定します。省略時は1が指定されたものとして検索します。
        start_record: Optional[int] = None

        # 追録・附録を検索対象に限定するかを指定します。省略時はfalse（限定しない）となります。
        supplement_and_appendix: Optional[bool] = None

        # 開催日付の範囲終了日をYYYY-MM-DD形式で指定します。省略可。
        until: Optional[str] = None

    
    @dataclass
    class MeetingRequestBuilderGetRequestConfiguration(RequestConfiguration[MeetingRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

