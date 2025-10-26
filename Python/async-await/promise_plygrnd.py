import asyncio
from dataclasses import dataclass
from functools import partial

import requests


@dataclass
class DocFactAttributes:
  body: str


@dataclass
class DogFact:
  id: str
  type: str
  attributes: DocFactAttributes


@dataclass
class DogFactResponse:
  data: list[DogFact]


valid_dog_fact_api_url = "https://dogapi.dog/api/v2/facts"
invalid_dog_fact_api_url = "http://invalid_url/api/v2/facts"


async def promise_all_fetch_dog_fact():
  """
  promise_all (default) crashes the python program if one of the requests failes e.g
  # Traceback (most recent call last):
  #   File "async-await/plygrnd.py", line 36, in <...>
  # ...
  # requests.exceptions.ConnectionError:
  # HTTPConnectionPool(host='invalid_url', port=80):
  # Max retries exceeded with url: /api/v2/facts
  # (Caused by NameResolutionError("<urllib3.connection.HTTPConnection object at 0x101b9d010>:
  # Failed to resolve 'invalid_url' ([Errno 8] nodename nor servname provided, or not known)"))
  #
  # Hence "requires" try/except when calling this function, and if one of the requests fails, consider all failed,
  # as no return data
  """

  loop = asyncio.get_running_loop()

  promises = [
    loop.run_in_executor(None, partial(requests.get, invalid_dog_fact_api_url)),
    loop.run_in_executor(None, partial(requests.get, valid_dog_fact_api_url)),
    loop.run_in_executor(None, partial(requests.get, valid_dog_fact_api_url)),
    loop.run_in_executor(None, partial(requests.get, valid_dog_fact_api_url)),
  ]
  responses = await asyncio.gather(*promises)
  print(responses)


async def promise_allsettled_fetch_dog_fact():
  """
  all_settled (return-execptions=True) does not "crash" the python program it returns an array of e.g
  # [ConnectionError(...), <Response [200]>, <Response [200]>, <Response [200]>]
  """
  loop = asyncio.get_running_loop()

  promises = [
    loop.run_in_executor(None, partial(requests.get, invalid_dog_fact_api_url)),
    loop.run_in_executor(None, partial(requests.get, valid_dog_fact_api_url)),
    loop.run_in_executor(None, partial(requests.get, valid_dog_fact_api_url)),
    loop.run_in_executor(None, partial(requests.get, valid_dog_fact_api_url)),
  ]
  responses = await asyncio.gather(*promises, return_exceptions=True)
  print(responses)


def main():
  print("----------------")
  print("Running promise_all_fetch_dog_fact:")
  print("----------------")
  try:
    asyncio.run(
      promise_all_fetch_dog_fact()
    )  # crashes the main function / python program with exception, so requires try/except
  except Exception as e:
    print("Caught exception from promise_all_fetch_dog_fact:", e)
    print("If not caught, this would have crashed the main function / python program")

  print("----------------")
  print("Running promise_allsettled_fetch_dog_fact:")
  print("----------------")
  asyncio.run(promise_allsettled_fetch_dog_fact())  # does not crash the main function / python program


if __name__ == "__main__":
  main()
