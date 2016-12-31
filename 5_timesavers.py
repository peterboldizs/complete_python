#!/usr/bin/python3
from math import sqrt
from string import ascii_lowercase

print("timesaver tools")

print(list(map(lambda *a: a, range(3), 'abc')))
print(list(map(lambda *a: a, range(3), 'abc', range(4,7))))

names = ('peter', 'marti', 'david', 'dori', 'anna')
ages = (47,45,17,16,11)

t1 = (1,2,3,4,5,6)
t2 = (10,20,30,40,50,60,70)
print(list(zip(t1,t2)))
print(list(zip(names, ages)))
print(list(map(lambda *a: a, names, ages)))

l1 = [2,6,4,8,9]
l2 = [12,3,2,32,7]
l3 = [7,2,8,5,4]
maxes = map(lambda n: max(*n), zip(l1,l2,l3))
print("maxes: ", list(maxes))

print(list(filter(lambda x: x > 10, l2)))

print("squares: ", [n **2 for n in range(10)])
print("even squares: ", [n **2 for n in range(10) if not n % 2])

items = 'ABCDE'
print(list([items[a], items[b]] for a in range(len(items)) for b in range(a, len(items))))

mx = 10
legs1 = [(a, b, sqrt(a**2 + b**2)) for a in range(1, mx) for b in range(a, mx)]
print(list(legs1))
legs2 = [(a, b, int(c)) for a, b, c in legs1 if c.is_integer()]
print(legs2)

lettermap = dict((c, k) for k, c in enumerate(ascii_lowercase, 1))
print(lettermap)
lettermap2 = {k:v for v, k in enumerate(ascii_lowercase, 1)}
print(lettermap2)

print("generators")

def get_squares_gen(num):
    for x in range(num):
        yield x ** 2

squares = get_squares_gen(5)
print(next(squares))
print(squares.__next__()) # same
print(next(squares))
print(next(squares))
print(next(squares))
#print(next(squares)) StopIteration raised
print("geometric progress")
def geom_prog(a, q):
    k = 0
    while True:
        res = a * q ** k
        if res < 500000:
            yield res
        else:
            return
        k += 1

for n in geom_prog(2, 5):
    print(n)

print("yield from subiterator")
def si_squares(s, e):
    yield from (n ** 2 for n in range(s,e))

for m in si_squares(2,9):
    print(m)

cubes_gen = (k ** 3 for k in range(10))
print("cubes_gen:", list(cubes_gen))
print("cubes_gen again:", list(cubes_gen))

cubes2 = [k ** 3 for k in range(10)]
odd_cubes = (c for c in cubes2 if c % 2)
print("odd cubes: ", list(odd_cubes))

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

print("generate triples")
def gen_triple(num):
    for m in range(1, int(num ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 and gcd(m,n) == 1:
                c = m ** 2 + n ** 2
                if c <= num:
                    a = m ** 2 - n ** 2
                    b = 2 * m * n
                    yield a, b, c

triples = sorted(gen_triple(50), key = lambda * triple: sum(*triple))
print(triples)

print("fibonacci")
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci(100)))

print("counter")
def counter(start=0):
    n = start
    while True:
        res = yield n
        print(type(res), res)
        if res == 'Q':
            break
        n += 1
c = counter(3)
print(next(c))
print(c.send("jaj"))
print(next(c))
print(c.send('Q'))

