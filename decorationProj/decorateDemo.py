"""
@time : 2019/8/31下午5:11
@Author: kongwiki
@File: decorateDemo.py
@Email: kongwiki@163.com
"""


def deco(func):
	def inner():
		print("running inner()")

	return inner


@deco
def target():
	print("runnning target()")


# target()

global c

c = 6
def f1(a):
	print(a)
	print(c)
	c=3
f1(2)