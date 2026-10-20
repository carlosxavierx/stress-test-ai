import asyncio
import aiohttp
import time
import statistics
import pandas as pd

URL = "http://localhost:11434/api/generate"

PROMPT = "Hola"


async def send_request(session):

    start = time.time()

    try:

        async with session.post(
            URL,
            json={
                "model": "gemma4:e4b",
                "prompt": PROMPT,
                "stream": False,
                "options": {
                    "temperature": 0.2,
                    "num_predict": 25
                }
            },
        ) as response:

            await response.json()

            return time.time() - start

    except Exception:
        return None


async def run_test(users):

    async with aiohttp.ClientSession() as session:

        tasks = [
            send_request(session)
            for _ in range(users)
        ]

        results = await asyncio.gather(*tasks)

        success = [r for r in results if r]

        avg_time = (
            round(statistics.mean(success), 2)
            if success
            else 0
        )

        return {
            "users": users,
            "requests": len(results),
            "success": len(success),
            "errors": len(results) - len(success),
            "avg_time": avg_time,
        }


async def main():

    scenarios = [5, 10, 20]

    results = []

    for users in scenarios:

        print(
            f"\nExecutant {users} usuaris..."
        )

        result = await run_test(users)

        print(result)

        results.append(result)

    df = pd.DataFrame(results)

    df.to_csv(
        "results_optimized.csv",
        index=False
    )

    print("\nResultats guardats a results_optimized.csv")


asyncio.run(main())
