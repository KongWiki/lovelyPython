"""
@time : 2019/7/30下午4:33
@Author: kongwiki
@File: helloThread.py
@Email: kongwiki@163.com
"""
import threading


def function(i):
    print("function called by thread %i\n" % i)
    return


threads = []

for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
