"""
@time : 2019/8/7上午8:56
@Author: kongwiki
@File: rlockThread.py
@Email: kongwiki@163.com
"""
import threading
import time


class Box(object):
	lock = threading.RLock()

	def __init__(self):
		self.total_items = 0

	def excute(self, n):
		Box.lock.acquire()
		self.total_items += n
		Box.lock.release()

	def add(self):
		Box.lock.acquire()
		self.excute(1)
		Box.lock.release()

	def remove(self):
		Box.lock.acquire()
		self.excute(-1)
		Box.lock.release()


def remover(box, items):
	while items > 0:
		print("在box中移除一项\n")
		box.remove()
		time.sleep(1)
		items -= 1


def adder(box, items):
	while items > 0:
		print("在box中添加一项")
		box.add()
		time.sleep(1)
		items -= 1


if __name__ == '__main__':
	items = 5
	print("在box中放入{}个物品".format(items))
	box = Box()
	t1 = threading.Thread(target=adder, args=(box, items))
	t2 = threading.Thread(target=remover, args=(box, items))
	t1.start()
	t2.start()

	t1.join()
	t2.join()
	print("最后box中还剩余{}个物品".format(box.total_items))
