"""
In javascript there is something called Promise.allSettled which waits for
all promises to settle (either fulfilled or rejected) and returns their results.
In python asyncio, we can achieve similar behavior using asyncio.gather with return_exceptions=True.
This example demonstrates how to perform multiple asynchronous operations, wait for all of them to complete,
and handle both successes and failures.

To differentiate from successful and failed requests, we need to use isinstance to check the type of each result.

"""

import asyncio
import random

# Each fetch either succeeds with a str or yields an Exception when gathered with
# return_exceptions=True.
## Note succeeds with a str in this instance, since we just simulate a http request
type FetchResult = str | Exception


# Simulated async request (e.g. fetching from datastore)
async def fetch_data(id: str) -> FetchResult:
  await asyncio.sleep(random.uniform(0.2, 1.0))  # simulate network delay
  if random.random() < 0.3:
    raise Exception(f"❌ Request {id} failed")
  return f"✅ Request {id} succeeded"


async def fetch_all_data():
  tasks = [fetch_data(i) for i in range(10)]
  # This (asyncio.gather(..., return_exceptions=True)) is like Promise.allSettled —
  # it waits for all, even if some fail
  results = await asyncio.gather(*tasks, return_exceptions=True)
  return results


def process_results(results: list[FetchResult]) -> dict[str, list[FetchResult]]:
  """
  This functions is used to simulate how to work with the results.
  Our goal here is to create a dictionary with two keys: 'successes' and 'failures'.
  successes will contain a list of all successful results,
  and failures will contain a list of all exceptions.
  """

  processed = {"successes": [], "failures": []}

  for result in results:
    if isinstance(result, Exception):
      processed["failures"].append(result)
    else:
      processed["successes"].append(result)

  return processed


def main():
  print("Starting script...")

  # Run async section (this blocks until all async requests finish)
  results = asyncio.run(fetch_all_data())

  # Handle results (success + failures)
  processed_results = process_results(results)
  print("Processed Results:")
  print(f"Successes: {processed_results['successes']}")
  print(f"Failures: {processed_results['failures']}")
  # Continue synchronous code
  print("hello after fetching data from 10 datastores")


if __name__ == "__main__":
  main()
