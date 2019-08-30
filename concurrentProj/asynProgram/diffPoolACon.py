"""
@time : 2019/8/30下午3:13
@Author: kongwiki
@File: diffPoolACon.py
@Email: kongwiki@163.com
"""
from concurrent.futures import as_completed, ProcessPoolExecutor
from multiprocessing.pool import Pool
import time

NUMBERS = range(1, 100000)
K = 50


def f(x):
	r = 0
	for k in range(1, K + 2):
		r += x ** (1 / k ** 1.5)
	return r


print("multiprocessing.pool.Pool\n")
start = time.time()

l = []
pool = Pool(3)
for num, result in zip(NUMBERS, pool.map(f, NUMBERS)):
	l.append(result)
print(len(l))
print("Cost: {}\n".format(time.time() - start))

print("ProcessPoolExecutor with chunksize\n")
start = time.time()

i = []
with ProcessPoolExecutor(max_workers=3) as executor:
	chunksize, extra = divmod(len(NUMBERS), executor._max_workers*4)

	for num, result in zip(NUMBERS, executor.map(f, NUMBERS, chunksize=chunksize)):
		i.append(result)
print(len(i))
print("Cost: {}".format(time.time() - start))


print("ProcessPoolExecutor without chunksize\n")
start = time.time()

j = []
with ProcessPoolExecutor(max_workers=3) as executor:
	for num, result in zip(NUMBERS, executor.map(f, NUMBERS)):
		j.append(result)
print(len(j))
print("Cost: {}".format(time.time() -start))