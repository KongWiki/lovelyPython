"""
@time : 2019/9/3下午7:49
@Author: kongwiki
@File: coroutineDemo.py
@Email: kongwiki@163.com
"""


def simpel_coroutine():
	print("-> coroutine started")
	x = yield
	print("-> coroutine received:", x)


def simple_coro2(a):
	print("-> Started: a = ", a)
	b = yield a
	print("-> Received: b = ", b)
	c = yield a+b
	print("-> Received: c = ", c)


def averger():
	total = 0.0
	count = 0
	averge = None
	while True:
		term  = yield averge
		total += term
		count += 1
		averge = total/count


if __name__ == '__main__':
	# my_coro = simpel_coroutine()
	# print(my_coro)
	# next(my_coro)
	# my_coro.send(42)
	# my_coro2 = simple_coro2(14)
	# from inspect import getgeneratorstate
	# print(getgeneratorstate(my_coro2))
	# 预激
	# next(my_coro2)
	# print(getgeneratorstate(my_coro2))
	# my_coro2.send(28)
	# my_coro2.send(99)
	# print(getgeneratorstate(my_coro2))
	# coro_avg = averger()
	# next(coro_avg)
	# print(coro_avg.send(10))
	# print(coro_avg.send(30))
	# print(coro_avg.send(5))