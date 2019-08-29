"""
@time : 2019/8/27下午2:28
@Author: kongwiki
@File: conditionThread.py
@Email: kongwiki@163.com
"""
from threading import Thread, Condition
import time

items = []
condition = Condition()


class consumer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def consume(self):
		global items
		global condition
		condition.acquire()
		if not items:
			condition.wait()
			print("消费提醒: 当前没有任何物品消费")
		items.pop()
		print("消费提醒: 当前消费了1个物品")
		print("消费提醒: 当前共有{}物品可以消费".format(len(items)))
		condition.notify()
		condition.release()

	def run(self):
		for i in range(0, 20):
			time.sleep(2)
			self.consume()


class producer(Thread):
	def __init__(self):
		Thread.__init__(self)

	def produce(self):
		global items
		global condition
		condition.acquire()
		if len(items) == 8:
			condition.wait()
			print("生产提醒: 共生产{}物品, 物品生产过多 --- 暂停".format(len(items)))
		items.append(1)
		print("生产提醒: 共生产了{}个商品".format(len(items)))
		condition.notify()
		condition.release()

	def run(self):
		for i in range(0, 20):
			time.sleep(1)
			self.produce()


if __name__ == '__main__':
	producer = producer()
	consumer = consumer()
	producer.start()
	consumer.start()
	producer.join()
	consumer.join()
