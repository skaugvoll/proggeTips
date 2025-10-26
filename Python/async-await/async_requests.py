import asyncio
import time

import requests
from wove import weave


def seqential_requests(urls: list[str]):
  results = []
  for url in urls:
    response = requests.get(url)
    results.append(response.status_code)
  return results


def async_requests(urls: list[str]):
  # set up the concurrent request(s)
  with weave() as w:

    @w.do(urls)
    def fetch_data(url):
      return requests.get(url)

  print(w.result.timings)  # remove this for more accurate comparison
  # Execute the requests and gather results and return results
  # can print the response's fact id to verify that different requests were made
  # print([w.result.fetch_data[i].json()["data"][0]["id"] for i in range(len(urls))])
  return [w.result.fetch_data[i].status_code for i in range(len(urls))]


async def asyncio_async_requests_simple(urls: list[str]):
  """
  Simplest form of using async/await with Asyncio and Wove.
  """
  async with weave(debug=False) as w:

    @w.do(urls)
    async def async_fetch_data(url):
      return requests.get(url).status_code

  print(w.result.timings)  # remove this for more accurate comparison
  return w.result.final


async def asyncio_async_requests_adv(urls: list[str]):
  """
  Another way to enable more concurrency and processing, but a bit overkill since we don't need to split into 3 ops.
  """
  async with weave(debug=False) as w:

    @w.do(urls)
    async def async_fetch_data(url):
      return requests.get(url)

    @w.do("async_fetch_data")
    async def create_http_status_response_array(response):
      return response.status_code

    # Collects the results.
    # You can mix `async def` and `def` tasks.
    @w.do
    async def summary(create_http_status_response_array):
      return create_http_status_response_array

  print(w.result.timings)  # remove this for more accurate comparison
  return w.result.summary


def main():
  """
  'Compare the time it takes to do 10 concurrent HTTP requests and print their status codes'
  vs
  'Do 10 HTTP requests sequentially and print their status codes'
  """
  urls = ["https://dogapi.dog/api/v2/facts"] * 10

  print("--------------------------------")
  print(f"Starting {len(urls)} concurrent requests...")
  print("--------------------------------")
  async_requests_start = time.time()
  async_status_codes = async_requests(urls)
  async_requests_end = time.time()
  print("Concurrent status codes:", async_status_codes)
  print("Concurrent requests took:", async_requests_end - async_requests_start, "seconds")
  print("--------------------------------\n")

  print("\n--------------------------------")
  print(f"Starting {len(urls)} async Asyncio requests...")
  print("--------------------------------")
  asyncio_async_requests_start = time.time()
  asyncio_async_status_codes = asyncio.run(asyncio_async_requests_simple(urls))
  # asyncio_async_status_codes = asyncio.run(asyncio_async_requests_adv(urls))
  asyncio_async_requests_end = time.time()
  print("Async asyncio status codes:", asyncio_async_status_codes)
  print("Async asyncio requests took:", asyncio_async_requests_end - asyncio_async_requests_start, "seconds")
  print("--------------------------------\n")

  print("\n--------------------------------")
  print(f"Starting {len(urls)} sequential requests...")
  print("--------------------------------")
  seqential_requests_start = time.time()
  seqential_status_codes = seqential_requests(urls)
  seqential_requests_end = time.time()
  print("Sequential status codes:", seqential_status_codes)
  print("Sequential requests took:", seqential_requests_end - seqential_requests_start, "seconds")
  print("--------------------------------")


if __name__ == "__main__":
  main()
