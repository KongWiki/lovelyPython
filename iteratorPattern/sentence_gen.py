"""
@time : 2019/9/27下午7:48
@Author: kongwiki
@File: sentence_gen.py
@Email: kongwiki@163.com
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
	def __init__(self, text):
		self.text = text
		self.words = RE_WORD.findall(text)

	def __repr__(self):
		return "Sentence(%s)"%reprlib.repr(self.text)

	def __iter__(self):
		for word in self.words:
			# 产出当前的word
			yield word
		return
	# complete

