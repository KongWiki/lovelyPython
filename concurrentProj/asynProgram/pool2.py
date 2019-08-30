"""
@time : 2019/8/29下午6:06
@Author: kongwiki
@File: pool2.py
@Email: kongwiki@163.com
"""
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from multiprocessing.pool import Pool


NUMBERS = range(25, 38)


def fib(n):
	if n <= 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)


start = time.time()

# use Pool
pool = Pool(5)
for num, result in zip(NUMBERS, pool.map(fib, NUMBERS)):
	print("fib({}) = {}".format(num, result))

print("Pool Cost: {} \n".format(time.time() - start))


# use map
start = time.time()
with ProcessPoolExecutor(max_workers=5) as executor:
	for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
		print("fib({}) = {}".format(num, result))

print("ProcessPool Cost: {} \n".format(time.time() - start))

# use submit
# with ProcessPoolExecutor(max_workers=5) as executor:
# 	# for num, result in zip(NUMBERS, executor.submit(fib, NUMBERS)):
# 	future_to_num = {executor.submit(fib, num): num for num in NUMBERS}
# 	for future in as_completed(future_to_num):
# 		num = future_to_num[future]
# 		try:
# 			result = future.result()
# 		except Exception as e:
# 			print("raise an exception: {}".format(e))
# 		else:
# 			print("fib({}) = {}".format(num, result))
start = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
	for num, result in zip(NUMBERS, executor.map(fib, NUMBERS)):
		print("fib({}) == {}".format(num, result))
print("ThreadPool Cost: {}".format(time.time()-start))
