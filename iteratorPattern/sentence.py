"""
@time : 2019/9/3下午9:47
@Author: kongwiki
@File: sentence.py
@Email: kongwiki@163.com
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
	def __init__(self, text):
		self.text = text
		self.word = RE_WORD.findall(text)

	def __getitem__(self, index):
		return self.word[index]

	def __len__(self):
		return len(self.word)

	def __repr__(self):
		return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
	s = Sentence('"The time has come," the Walrus said.')
	print(s)
	# 输出为Sentence('"The time ha... Walrus said.')的原因为 sentence类
	# 中的__repr__方法
	for word in s:
		print(word)
	print(list(s))
