# Async-Await

This directory will show how to achive the same behaviours as Javascript's `Promise.all()` and `Promise.allSettled()`

## Javascript's Promise:

- `Promise.all` will reject** as soon** as **one** of the Promises in the array **rejects**.

- `Promise.allSettled` will **never** reject - it will resolve once **all** Promises in the array have either rejected or resolved.

Their resolve values are different as well:

- `Promise.all` will resolve to an **array** of each of the values that the Promises resolve to
  - eg `[Promise.resolve(1), Promise.resolve(2)]` will turn into `[1, 2]`.
- `Promise.allSettled` will instead give you
  - `[{ status : 'fulfilled', value: 1 }, { status : 'fulfilled', value: 2 }]`.

## Python's Equivalence

### asyncio.gather() behavior:

- `asyncio.gather(return_exceptions=False)` - equivalent to `Promise.all`

  - Raises exception immediately when any coroutine fails
  - Returns list of successful results: `[response1, response2]`

- `asyncio.gather(return_exceptions=True)` - equivalent to `Promise.allSettled`
  - Never raises exceptions, always completes
  - Returns mixed list: `[response1, Exception("error"), response3]`

### Example with requests:

```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://api.github.com", "https://invalid-url"]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]

        # Promise.all equivalent - fails fast
        try:
            results = await asyncio.gather(*tasks, return_exceptions=False)
            # Type: List[str] - only successful responses
        except Exception as e:
            print(f"Failed: {e}")

        # Promise.allSettled equivalent - never fails
        results = await asyncio.gather(*tasks, return_exceptions=True)
        # Type: List[Union[str, Exception]] - mixed results

        # Check results with isinstance()
        for result in results:
            if isinstance(result, Exception):
                print(f"Failed: {result}")
            else:
                print(f"Success: {len(result)} chars")
```

We use `isinstance(result, Exception)` because `return_exceptions=True` returns actual Exception objects mixed with successful results in the same list, requiring type checking to distinguish between success and failure cases.

## Creation

`async-await` is initialized with the `uv`-tool.

1. `uv init`

## Contribution

if no `.venv` folder, please run:

0. `uv venv` # will create the .venv (virtual environment)

when/if `.venv` folder, run:

1. `source .venv/bin/activate`
2. `uv sync`

### Add dependency

`uv add _dependency_`
