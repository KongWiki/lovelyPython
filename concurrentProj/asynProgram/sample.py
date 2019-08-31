"""
@time : 2019/8/31上午10:31
@Author: kongwiki
@File: sample.py
@Email: kongwiki@163.com
"""
import time
import asyncio


async def do_some_work(x):
	print("Working {}".format(x))
	await asyncio.sleep(x)


if __name__ == '__main__':
	# print(asyncio.iscoroutinefunction(do_some_work))
	# print(asyncio.iscoroutine(do_some_work(3)))
	loop = asyncio.get_event_loop()
	start = time.time()
	loop.run_until_complete(do_some_work(3))
	print("Cost: {}".format(time.time() - start))