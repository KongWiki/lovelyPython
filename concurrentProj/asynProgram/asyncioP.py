"""
@time : 2019/8/29下午3:07
@Author: kongwiki
@File: asyncioP.py
@Email: kongwiki@163.com
"""
import asyncio
import datetime
import time


def function_1(end_time, loop):
	print("function_1 called")
	if (loop.time() + 1.0) < end_time:
		loop.call_later(1, function_2, end_time, loop)
	else:
		loop.stop()


def function_2(end_time, loop):
	print("function_2 called ")
	if (loop.time() + 1.0) < end_time:
		loop.call_later(1, function_3, end_time, loop)
	else:
		loop.stop()


def function_3(end_time, loop):
	print("function_3 called")
	if (loop.time() + 1.0) < end_time:
		loop.call_later(1, function_1, end_time, loop)
	else:
		loop.stop()


def function_4(end_time, loop):
	print("function_5 called")
	if (loop.time() + 1.0) < end_time:
		loop.call_later(1, function_4, end_time, loop)
	else:
		loop.stop()


loop = asyncio.get_event_loop()
print(loop.time())
end_loop = loop.time() + 9.0
loop.call_soon(function_1, end_loop, loop)
# loop.call_soon(function_4, end_loop, loop)
loop.run_forever()
loop.close()
