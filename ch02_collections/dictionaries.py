print("Dictionary operations")
print("equal")
da = dict(a=1, z=-1)
db = {'a': 1, 'z': -1}
dc = dict(zip(['a', 'z'], [1, -1]))
dd = dict([('a', 1), ('z', -1)])
print(da, db)
print(da == db == dc == dd)

print("zipping 1")
z = list(zip('hello', range(1, 6)))
print("zipped list: ", z)
da['c'] = 5
print(da, len(da))
print('z' in da)
print(da.keys())
print(da.values())
print(da.items())

print("deleting")
del da['z']
print(da, len(da))
print('z' in da)

print("zipping 2")
dz = dict(zip('hello', range(5)))
print("zipped dict:", dz)

print("popping and getting")
print(dz.popitem())
print(dz.get('e'))

dz_tuple = tuple(dz.items())
print(dz_tuple)

my_str = ["a", "b", "c", "d"]
my_str2 = '1'.join(my_str)
print("new str by join: {}".format(my_str2))
letters = "qwertz"
my_str3 = my_str2.join(letters)
print(my_str3)

print("split words")
sentence = input("enter your sentence:")
words = sentence.split()
print("you entered {} words: {}".format(len(words), words))