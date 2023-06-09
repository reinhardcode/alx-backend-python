#!/usr/bin/env python3
"""
contains a function measure_time with int
n and max_delay as arg that measures the
total execution time for wait_n and returns
total_time/n float
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures time"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter() - start
    return end / n
