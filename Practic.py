import asyncio


async def count(limit=3):
    for step in range(1, limit + 1):
        print("Веду отсчёт.", step)
        await asyncio.sleep(0)


coroutine = count(5)

while True:
    coroutine.send(None)
