import asyncio
import requests_async as requests
# import requests

async def fn1():
    while True:
        await asyncio.sleep(1)
        print('in fn1')


async def fn2():
    while True:
        await asyncio.sleep(1)
        print('in fn2')


async def fn3():
    await asyncio.sleep(1)
    res = await requests.get('https://www.baidu.com')
    print(res.content.decode())


async def main():
    task1 = asyncio.create_task(fn1())
    task2 = asyncio.create_task(fn2())
    task3 = asyncio.create_task(fn3())

    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(main())
