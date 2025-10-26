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

  # Execute the requests and gather results and return results
  return [w.result.fetch_data[i].status_code for i in range(len(urls))]


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
