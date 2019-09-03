"""
@time : 2019/9/3下午3:13
@Author: kongwiki
@File: achieveDecorate.py
@Email: kongwiki@163.com
"""
import time


def clock(func):
	def clocked(*args):
		# 记录出事的时间
		t0 = time.perf_counter()
		# 保存原来函数的结果
		result = func(*args)
		# 记录执行结束的时间
		elapsed = time.perf_counter()
		# 获取对应的被装饰的函数的名字
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print("[%0.8fs]%s(%s) -> %r" % (elapsed, name, arg_str, result))
		return result

	return clocked


@clock
def snooze(seconds):
	time.sleep(seconds)


@clock
def factorial(n):
	return 1 if n < 2 else n * factorial(n - 1)


if __name__ == '__main__':
	print("*" * 40, "calling snooze(.123)")
	snooze(.123)
	print("*" * 40, "calling factorail(6)")
	print("6!=", factorial(6))
