#!/usr/bin/python3

import sys
from decimal import Decimal as D
from fractions import Fraction

print(sys.version)
print("bla bla float_info", sys.float_info)

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
print(c - d)
f = Fraction(10, 6)
print(f)
print(f.numerator, f.denominator)
print(Fraction(2, 3) + Fraction(1, 3))

d = D(3.14)
print(d)
print(D(0.1) * D(3) - D(0.3))
print(D('0.1') * D(3) - D('0.3'))
