"""
@time : 2019/9/27下午7:10
@Author: kongwiki
@File: sentence_iter.py
@Email: kongwiki@163.com
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


######################
#   典型的迭代器     #
######################

class Sentence:
	"""
	该类仅说明了是一个可迭代的对象
	"""
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self):
		return "Sentence(%s)" % reprlib.repr(self.text)

	def __iter__(self):
		return SentenceIterator(self.words)


class SentenceIterator:
	"""
	该类实现了一个迭代器
	"""
	def __init__(self, text):
		self.text = text
		self.index = 0

	def __next__(self):
		try:
			word = self.text[self.index]
		except IndexError:
			raise StopIteration()
		return word

	# 迭代器需要返回自身迭代对象
	def __iter__(self):
		return self