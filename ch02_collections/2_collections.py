#!/usr/bin/python3

print("Tuple")
te = ()
t = (1, 2, 3, 4, 5)
print(type(t))
print(3 in t)
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

print("List")
le = []
my_list = [1, 2, 3]
for x in my_list:
    print(x)

print([x + 5 for x in my_list])

my_list.append(12)
print(my_list)
my_list.extend([1, 1, 5, 7])
print(my_list)
print(my_list.count(1))
my_list.insert(0, 11)
print(my_list.index(12))
print(my_list.pop())
print(my_list.pop())
my_list.reverse()
my_list.sort()
print(my_list)
my_list2 = [5, 6, 7, 8]
my_list3 = my_list + my_list2
print(my_list3)
my_list4 = my_list2 * 2
print(my_list4, len(my_list4))

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
my_set = set()
my_set.add(2)
my_set.add(3)
my_set.add(5)
my_set.add(7)
print(my_set)
my_set.add(1)
print(my_set)
my_set.remove(1)
print(3 in my_set)
print(4 in my_set)
my_set.add(3)
print(my_set)
#  my_set2 = set([7, 11, 13, 17])
my_set2 = [7, 11, 13, 17]
print(my_set | my_set2)
print(my_set & my_set2)
print(my_set - my_set2)
my_set3 = {2, 3, 3, 5, 5, 7}
print(my_set3)

print("Dictionary")
da = dict(a=1, z=-1)
db = {'a': 1, 'z': -1}
dc = dict(zip(['a', 'z'], [1, -1]))
dd = dict([('a', 1), ('z', -1)])
print(da, db)
print(da == db == dc == dd)

z = list(zip('hello', range(1, 6)))
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
