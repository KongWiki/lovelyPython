"""
@time : 2019/9/27下午8:33
@Author: kongwiki
@File: sentence_gen2.py
@Email: kongwiki@163.com
"""
import re
import reprlib

RE_WORD = re.compile("\w+")


# 惰性实现
class Sentence:
	def __init__(self, text):
		self.text = text

	def __repr__(self):
		return "Sentence(%s)" % reprlib.repr(self.text)

	def __iter__(self):
		for match in RE_WORD.finditer(self.text):
			# 提取出匹配的具体文本
			yield match.group()


