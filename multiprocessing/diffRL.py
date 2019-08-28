"""
@time : 2019/8/27下午1:36
@Author: kongwiki
@File: diffRL.py
@Email: kongwiki@163.com
"""
"""
Rlock 和 Lock的区别
"""
import threading

lock = threading.Lock()

rlock = threading.RLock()

# lock.acquire()
# lock.acquire()
# lock.release()
# lock.release()
rlock.acquire()
rlock.acquire()
rlock.release()
rlock.release()