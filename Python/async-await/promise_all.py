"""
asyncio.gather(*tasks) → runs all coroutines concurrently.
If any coroutine raises an exception, gather re-raises it (like Promise.all rejects).
If you want behavior like Promise.allSettled (which never fails), you can use:
await asyncio.gather(*tasks, return_exceptions=True)
"""

import asyncio
import random


async def fetch_data(name, delay):
  """Simulate an async operation like a network request."""
  await asyncio.sleep(delay)
  if random.random() < 0.2:  # simulate random failure
    raise Exception(f"{name} failed!")
  return f"{name} completed after {delay:.1f}s"


async def promise_all(tasks):
  """
  Equivalent of JavaScript's Promise.all:
  - Runs all tasks concurrently
  - Returns results if all succeed
  - Raises the first exception if any fails
  """
  return await asyncio.gather(*tasks)  # raises if any fails


async def main():
  tasks = [
    fetch_data("User API", 1.0),
    fetch_data("Posts API", 2.0),
    fetch_data("Comments API", 1.5),
  ]

  try:
    results = await promise_all(tasks)
    print("✅ All tasks completed:")
    for r in results:
      print("  →", r)
  except Exception as e:
    print("❌ One of the tasks failed:", e)


if __name__ == "__main__":
  asyncio.run(main())
