#coding:utf-8
from orienter import Rectangle as r
from orienter import Somme as s

r1 = r(50, 23)
print(r1.surface())

n1 = int(input("Entrez un chiffre/nombre:	"))
n2 = int(input("Entrez un chiffre/nombre:	"))

s1 = s(n1, n2)
print(s1.som())