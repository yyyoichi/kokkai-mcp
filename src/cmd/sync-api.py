import argparse
import asyncio
from calendar import monthrange
from datetime import date
from typing import List
from src.client import Client
from src.config import KokkkaiAPIRequestConfig, SpeechRequestParam
from src.kokkaiapiclient.api.speech.speech_get_response import SpeechGetResponse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Speech data retriever")
    parser.add_argument("--use_cache", type=int, default=0, help="Use cache (1: True, 0: False, default: 0)")
    parser.add_argument("--year", type=int, required=True, help="Year to retrieve speeches for")
    parser.add_argument("--month", type=int, required=True, help="Month to retrieve speeches for")
    args = parser.parse_args()

    c = Client(config=KokkkaiAPIRequestConfig(use_cache=args.use_cache==1, interval_milsec=1000))
    async def worker(year: int, month: int):
        """
        Get speech data for a specific year and month.
        """
        speeches :List[SpeechGetResponse] = []
        from_date = f"{year:04d}-{month:02d}-01"
        until_date = f"{year:04d}-{month:02d}-{monthrange(year, month)[1]}"
        p = SpeechRequestParam(
            from_date=date.fromisoformat(from_date),
            until_date=date.fromisoformat(until_date),
        )
        async for s in c.iter_speech(p):
            speeches.append(s)
        return speeches
    
    result = asyncio.run(worker(args.year, args.month))
    print(f"Retrieved {len(result)} speeches")
    