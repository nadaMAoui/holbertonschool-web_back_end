#!/usr/bin/env python3
"""Async Generator"""
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)

# Example usage:
async def main():
    async for number in async_generator():
        print(number)

# Run the event loop manually
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
