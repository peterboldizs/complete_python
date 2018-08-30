#!/usr/bin/python3

print("Tuple")
te = ()
t = (1,2,3,4,5)
print(type(t))
print(3 in t)
a,b = 1,2
print(a,b)
a,b = b,a
print(a,b)

print("List")
le = []
l = [1,2,3]
for x in l:
    print(x)
print([x + 5 for x in l])
l.append(12)
print(l)
l.extend([1,1,5,7])
print(l)
print(l.count(1))
l.insert(0,11)
print(l.index(12))
print(l.pop())
print(l.pop())
l.reverse()
l.sort()
print(l)
l2 = [5,6,7,8]
l3 = l + l2
print(l3)
l4 = l2 *2
print(l4, len(l4))

print("bytearray")
ba = bytearray(range(5))
print(ba)
ba2 = bytearray(b'peter')
ba2.replace(b'p', b'L')
print(ba2)
print(ba2.upper())

ba3 = ba2.replace(b'p', b'L')
print(ba3)
print(ba3.upper())

print("Set")
s = set()
s.add(2)
s.add(3)
s.add(5)
s.add(7)
print(s)
s.add(1)
print(s)
s.remove(1)
print(3 in s)
print(4 in s)
s.add(3)
print(s)
s2 = set([7,11,13,17])
print(s | s2)
print(s & s2)
print(s - s2)
s3 = {2,3,3,5,5,7}
print(s3)

print("Dictionary")
da = dict(a=1, z=-1)
db = {'a': 1, 'z': -1}
dc = dict(zip(['a', 'z'], [1, -1]))
dd = dict([('a',1), ('z', -1)])
print(da, db)
print(da == db == dc == dd)

z = list(zip('hello', range(1,6)))
print("zipped: ", z)
da['c'] = 5
print(da, len(da))
print('z' in da)
print(da.keys())
print(da.values())
print(da.items())
del da['z']
print(da, len(da))
print('z' in da)
dz = dict(zip('hello', range(5)))
print(dz.keys())
print(dz.values())
print(dz.items())
print(dz.popitem())
print(dz.get('e'))
