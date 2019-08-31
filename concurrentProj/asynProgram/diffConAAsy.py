"""
@time : 2019/8/30下午3:53
@Author: kongwiki
@File: diffConAAsy.py
@Email: kongwiki@163.com
"""
import time
import asyncio
import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor

NUMBERS = range(12)
URL = 'http://httpbin.org/get?a={}'


async def fetch_async(a):
	async with aiohttp.request('GET', URL.format(a)) as r:
		data = await r.json()
	return data['args']['a']



def fetch(a):
	r = requests.get(URL.format(a))
	return r.json()['args']['a']


# requests+ThreadPoolExecutor
start = time.time()
with ThreadPoolExecutor(max_workers=3) as executor:
	for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
		print("fetch({}) = {}".format(num, result))
print("User requests+ThreadPoolExecutor cost: {}\n".format(time.time() - start))


# requests+asyncio
async def run_scraper_tasks(executor):
	loop = asyncio.get_event_loop()

	blocking_tasks = []
	for num in NUMBERS:
		task = loop.run_in_executor(executor, fetch, num)
		task.__num = num
		blocking_tasks.append(task)

	completed, pending  = await  asyncio.wait(blocking_tasks)
	results = {t.__num: t.result() for t in completed}
	for num, result in sorted(results.items(), key=lambda x:x[0]):
		print("fetch({}) = {}".format(num, result))

start = time.time()
executor = ThreadPoolExecutor(3)
event_loop = asyncio.get_event_loop()

event_loop.run_until_complete(
	run_scraper_tasks(executor)
)
print("Use asyncio+requests+ThreadPoolExecutor cost: {}".format(time.time() - start))


start = time.time()
event_loop = asyncio.get_event_loop()
tasks = [fetch_async(num) for num in NUMBERS]
results = event_loop.run_until_complete(
	asyncio.gather(*tasks)
)

for num, result in zip(NUMBERS, results):
	print("fetch({}) = {}".format(num, result))

print("Use asyncio+aiohttp cost: {}".format(time.time() - start))
