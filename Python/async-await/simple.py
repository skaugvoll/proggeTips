import asyncio


async def do_something_async_but_wait_for_completion():
    print("Hello from async-await! - You will wait for me to complete...")
    await asyncio.sleep(3)
    print("Async operation complete!")


def main():
    print("Hello I will no do start something async that takes 3s")
    asyncio.run(do_something_async_but_wait_for_completion())
    print("This print should only appear after the async operation is complete.")


if __name__ == "__main__":
    main()
