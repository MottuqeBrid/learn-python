# AsyneIO in Python

import time
import asyncio


async def func1():
    print("Function 1 started")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("Function 1 ended")


async def func2():
    print("Function 2 started")
    # time.sleep(1)
    await asyncio.sleep(1)
    print("Function 2 ended")


async def func3():
    print("Function 3 started")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("Function 3 ended")


async def main():
    # task = asyncio.create_task(func1())
    # # await func1()
    # await func2()
    # await func3()
    L = await asyncio.gather(func1(), func2(), func3())
    print(L)


asyncio.run(main())
# func1()
# func2()
# func3()
# print("All functions completed")
