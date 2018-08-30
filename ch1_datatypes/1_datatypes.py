#!/usr/bin/python3

import sys
from fractions import Fraction
from decimal import Decimal as D

print(sys.version)
print("float_info",sys.float_info)

print(True and True)
print(True and False)
print(True or False)

print("Numeric types")
print(7 / 4)
print(7 // 4)
print(7 % 4)
print(3 * 0.1 - 0.3)
c = 3.14 + 2.73j
d = 1 + 1j
print(c.real)
print(c.imag)
print(c.conjugate())
print(c-d)
f = Fraction(10,6)
print(f)
print(f.numerator, f.denominator)
print(Fraction(2,3) + Fraction(1,3))

d = D(3.14)
print(d)
print(D(0.1) * D(3) - D(0.3))
print(D('0.1') * D(3) - D('0.3'))

print("Strings")
str1 = 'single quotes'
str2 = "double quotes"
str3 = '''triple
single quotes'''
str4 = """triple
double
quotes"""
print(str1)
print(str2)
print(str3)
print(str4)
print(len(str4))
str5 = "árvíztűrő tükörfúrógép"
print(type(str5))
print(str5)
e_str5 = str5.encode('utf-8')
print(type(e_str5))
print(e_str5)
de_str5 = e_str5.decode('utf-8')
print(type(de_str5))
print(de_str5)

str6 = "This is the beginning of a beautiful frienship"
print(str6[2:34:3])
print(str6[::-1])

