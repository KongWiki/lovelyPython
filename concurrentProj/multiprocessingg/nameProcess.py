"""
@time : 2019/9/23上午2:47
@Author: kongwiki
@File: nameProcess.py
@Email: kongwiki@163.com
"""
import multiprocessing
import time


def foo():
	name = multiprocessing.current_process().name
	print("Starting %s\n" % name)
	time.sleep(3)
	print("Existing %s \n" % name)


if __name__ == '__main__':
	process_with_name = multiprocessing.Process(name='foo_process', target=foo)
	# ? unknow what mean
	# process_with_name.daemon = True
	process_with_default_name = multiprocessing.Process(target=foo)
	process_with_name.start()
	process_with_default_name.start()
	# process_with_name.join()
	# process_with_default_name.join()



