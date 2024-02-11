#coding:utf-8
class Rectangle:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def surface(self):
		return self.a * self.b


class Somme:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def som(self):
		return self.a + self.b