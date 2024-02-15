import asyncio
from random import uniform
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

# Example usage:
async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

# Run the event loop manually
loop = asyncio.get_event_loop()
loop.run_until_complete(print_yielded_values())