## 可迭代对象 迭代器 生成器

### **可迭代对象**:

使用`__iter__`内置函数获取迭代器的对象。如果对象实现了能返回迭代器`__iter__`方法，那么对象就是可迭代的。同时实现了`__getitem__`方法，而且其参数是从零开始的索引，这种对象也是可迭代的。

### **迭代器**:

实现了无参数的`__next__`方法，返回序列中的下一个元素，如果没有函数了，抛出`StopIteration`异常，因为其也实现了`__iter__`方法，所以迭代器也是可迭代对象


```python
it = iter(s)
while True:
	try:
		print(next(it))
	except:
		del it
		break
```





### ~~**可迭代对象的两种标准**~~： 

1. 鸭子类型的极端：
   1. 不仅要实现`__iter__`方法
   2. 还要实现`__getitem__`方法，且其参数是从0开始的整数。
2. 白鹅类型：
   1. 如果实现了`__iter__`方法，该对象极为可迭代对象

### **检查是否能迭代**:

 调用`iter(x)`函数，使用`isinstance(x， abc.Iterable)`更准确，因为`iter(x)`函数会考虑遗留的`__getitem()`方法，而`abc.Iterable`不考虑

**迭代器**: 用于从集合中取出元素

**生成器** : 用于凭空生成元素

所有的生成器都是迭代器，因为生成器完全实现了迭代器接口

### 迭代器与可迭代对象的区别

可迭代对象有`__iter__`方法，每次都会实例化一个新的迭代器；但是迭代器需要实现`__next__`方法，返回单个元素，此外还需要实现`__iter__`方法返回迭代器本身

**迭代器是可迭代的，但可迭代的对象其不是迭代器**

**所以可迭代对象一定不能是自身的迭代器，也就是说可迭代对象必需要实现`__iter__`方法，但是不能实现`__next__`方法。迭代器应该是一直可以迭代的，迭代器的`__iter__`方法应该返回其自身。**
