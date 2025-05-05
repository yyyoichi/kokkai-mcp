import asyncio
from typing import List
from src.client import Client
from src.config import KokkkaiAPIRequestConfig
from src.kokkaiapiclient.api.speech.speech_get_response import SpeechGetResponse

if __name__ == "__main__":
    c = Client(config=KokkkaiAPIRequestConfig(usecache=True, interval_milsec=1000))
    async def worker(year: int, month: int):
        """
        Get speech data for a specific year and month.
        """
        speeches :List[SpeechGetResponse] = []
        async for s in c.iter_speech(year, month):
            speeches.append(s)
        return speeches
    
    result = asyncio.run(worker(2022, 1))
    print(f"Retrieved {len(result)} speeches")
    