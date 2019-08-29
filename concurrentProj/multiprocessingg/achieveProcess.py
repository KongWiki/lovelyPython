"""
@time : 2019/8/29上午10:03
@Author: kongwiki
@File: achieveProcess.py
@Email: kongwiki@163.com
"""
import multiprocessing


def foo(i):
	print("被进程{}唤醒".format(i))
	return

if __name__ == '__main__':
	process_job = []
	for i in range(10):
		p = multiprocessing.Process(target=foo, args=(i,))
		process_job.append(p)
		p.start()
		p.join()