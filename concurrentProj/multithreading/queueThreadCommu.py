"""
@time : 2019/8/28下午6:43
@Author: kongwiki
@File: queueThreadCommu.py
@Email: kongwiki@163.com
"""
from threading import Thread, Event
from queue import Queue
import time
import random


class producer(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		for i in range(10):
			item = random.randint(0, 256)
			self.queue.put(item)
			print('生产提醒: 物品 N° %d 由线程 %s 传入队列' % (item, self.name))
			time.sleep(1)


class consumer(Thread):
	def __init__(self, queue):
		Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			item = self.queue.get()
			print("消费提醒: %d 被线程%s 弹出队列" % (item, self.name))
			self.queue.task_done()


if __name__ == '__main__':
	queue = Queue()
	t1 = producer(queue)
	t2 = producer(queue)
	t3 = consumer(queue)
	t4 = consumer(queue)
	t1.start()
	t2.start()
	t3.start()
	t4.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()
