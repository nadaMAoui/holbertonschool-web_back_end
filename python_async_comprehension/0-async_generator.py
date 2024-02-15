import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Example usage:
async def main():
    async for number in async_generator():
        print(number)

# Run the event loop manually
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
