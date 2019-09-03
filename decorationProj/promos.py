"""
@time : 2019/9/2下午4:51
@Author: kongwiki
@File: promos.py
@Email: kongwiki@163.com
"""
promos = []

def promotion(promo_func):
	promos.append(promo_func)
	return promo_func


@promotion
def fidelity(order):
	"""
	为积分为1000或以上的顾客提供5%的折扣
	:param order:
	:return:
	"""
	return  order.total()*0.5 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
	"""
	单个商品为20个或以上的提供20%的折扣
	:param order:
	:return:
	"""
	discount = 0
	for item in order.cart:
		if item.quantity >= 20:
			discount += item.total()*.1
	return discount

