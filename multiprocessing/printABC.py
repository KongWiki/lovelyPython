"""
@time : 2019/8/28上午11:55
@Author: kongwiki
@File: printABC.py
@Email: kongwiki@163.com
"""
from threading import Condition, Thread

"""
三个线程依次输出ABC 10次
"""

condition = Condition()
current = "A"


class ThreadA(Thread):
	def run(self):
		global current
		for _ in range(10):
			with condition:
				while current != "A":
					condition.wait()
				print("A")
				current = "B"
				condition.notify_all()


class ThreadB(Thread):
	def run(self):
		global current
		for _ in range(10):
			with condition:
				while current != "B":
					condition.wait()
				print("B")
				current = "C"
				condition.notify_all()


class ThreadC(Thread):
	def run(self):
		global current
		for _ in range(10):
			with condition:
				while current != "C":
					condition.wait()
				print("C")
				current = "A"
				condition.notify_all()


if __name__ == '__main__':
	a = ThreadA()
	b = ThreadB()
	c = ThreadC()

	a.start()
	b.start()
	c.start()

	a.join()
	b.join()
	c.join()
