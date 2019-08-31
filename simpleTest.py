"""
@time : 2019/8/30下午4:12
@Author: kongwiki
@File: simpleTest.py
@Email: kongwiki@163.com
"""
"""
sample:
list=[
	[1],
	[2],
	[3],
	[4,5],
	[6,7,8],
	[9]
]

output:
1 2 3 4 6 9
1 2 3 4 7 9
1 2 3 4 8 9
1 2 3 5 6 9
1 2 3 5 7 9
1 2 3 5 8 9

thought
columns: 原数据每一项的积
row: 原数据的个数
"""
from functools import reduce


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


def ac(alist):
	rowLen = len(alist)
	columnLen = 1
	for i in range(rowLen):
		columnLen *= len(alist[i])


if __name__ == '__main__':
	list = [
		[1],
		[2],
		[3],
		[4, 5],
		[6, 7, 8],
		[9]
	]
