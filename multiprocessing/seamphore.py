"""
@time : 2019/8/26下午4:58
@Author: kongwiki
@File: seamphore.py
@Email: kongwiki@163.com
"""
import threading
import time
import random

semaphore = threading.Semaphore(0)


def consumer():
	print("消费者正在等待资源")
	semaphore.acquire()
	print("消费提醒: 消费资源为{}\n".format(item))


def producer():
	global item
	time.sleep(5)
	item = random.randint(0, 1000)
	print("生产提醒: 生产资源为{}".format(item))
	semaphore.release()


if __name__ == '__main__':
	for i in range(0, 5):
		t1 = threading.Thread(target=producer,)
		t2 = threading.Thread(target=consumer)
		t1.start()
		t2.start()

		t1.join()
		t2.join()

	print("程序运行结束")