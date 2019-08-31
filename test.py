"""
@time : 2019/8/30下午4:58
@Author: kongwiki
@File: test.py
@Email: kongwiki@163.com
"""
from functools import reduce
A = [1]
B = [2, 3]
C = [4, 5]
F = [6, 7, 8]
G = [9]

def myfunc(*lists):
	total = reduce(lambda x, y: x * y, map(len, lists))
	retList = []

	for i in range(0, total):
		step = total
		tempItem = []
		for l in lists:
			step /= len(l)
			# print(int(i//step%len(l)))
			tempItem.append(str(l[int(i // step % len(l))]))
			retList.append(tuple(tempItem))
		print("  ".join(tempItem))
	return retList


myfunc(A, B, C, F, G)