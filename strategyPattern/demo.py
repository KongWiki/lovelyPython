"""
@time : 2019/9/2下午5:11
@Author: kongwiki
@File: demo.py
@Email: kongwiki@163.com
"""
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", 'name fidelity')


class LineItem:
	def __init__(self, product, quantity, price):
		self.product = product
		self.quantity = quantity
		self.price = price

	def total(self):
		return self.price * self.quantity


class Order:  # 联系上下文
	def __init__(self, customer, cart, promotion=None):
		self.customer = customer
		self.cart = list(cart)
		self.promotion = promotion

	def total(self):
		if not hasattr(self, '__total'):
			self.__total = sum(item.total() for item in self.cart)
		return self.__total

	def due(self):
		if self.promotion is None:
			discount = 0
		else:
			discount = self.promotion.discount(self)
		return self.total() - discount

	def __repr__(self):
		fmt = '<Order total: {:2f} due: {:2f}>'
		return fmt.format(self.total(), self.due())


class Promotion(ABC):

	@abstractmethod
	def discount(self, order):
		"""
		返回折扣金额
		:param order:
		:return:
		"""


# 第一个策略
class FidelityPromo(Promotion):
	"""
	为积分为1000及以上的顾客
	"""

	def discount(self, order):
		return order.total() * .05 if order.customer.fidelity >= 1000 else 0


# 第二个策略
class BulkItemPromo(Promotion):
	"""
	为单个商品数量超过20及以上的顾客10%
	"""

	def discount(self, order):
		discount = 0
		for item in order.cart:
			if item.quantity >= 20:
				discount += item.total() * .1
		return discount


# 第三个策略
class LargeOrderPromo(Promotion):
	"""
	订单中的不同商品达到10个或以上是7%
	"""

	def discount(self, order):
		discount_items = {item.product for item in order.cart}
		if len(discount_items) >= 10:
			return order.total() * .07

		return 0


if __name__ == '__main__':
	wkk = Customer('John Doe', 0)
	a = Customer('Ann Smith', 1100)
	cart = [LineItem('banana', 4, .5),
			LineItem('apple', 10, 1.5),
			LineItem('watermellon', 5, 5.0)]

	print(Order(wkk, cart, FidelityPromo()))
	print(Order(a, cart, FidelityPromo()))
	print("--------------------------------")
	banana_cart = [LineItem('banana', 30, .5),
				   LineItem('apple', 10, 1.5)]
	print(Order(wkk, banana_cart, BulkItemPromo()))