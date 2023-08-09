# Wed Aug  9 13:15:42 2023 - start of First call
# Wed Aug  9 13:15:43 2023 - end of First call
# Wed Aug  9 13:15:43 2023 - start of Second call
# Wed Aug  9 13:15:44 2023 - end of Second call

import asyncio
import time

async def print_after(message):
    print(f"{time.ctime()} - start of", message)
    await asyncio.sleep(1)
    print(f"{time.ctime()} - end of", message)

async def main():
    # Start coroutine twice (hopefully the start!)
    first_awaitable = print_after("First call")
    second_awaitable = print_after("Second call")
    # Wwait for coroutine to finish
    await first_awaitable
    await second_awaitable

asyncio.run(main())