#!/usr/bin/env python3
""" an asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that returns the waiting time
    before executing a function"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
