print("Basic dictionaries")
person = {"fname": "Peter",
          "lname": "Boldizs",
          "byear": 1970}
print(person)
print(person["lname"])
person["gender"] = "male"
person["alive"] = True
person["fname"] = "Robert"
print(person)
del person["byear"]
print(person.keys())
print(person.values())
#person.clear()

person["byear"] = 1977
print("contents")
for attr in person:
    print("{} = {} ".format(attr,person[attr]))

print("contents sorted")
#okeys = list(person.keys())
#okeys.sort()
okeys = sorted(list(person.keys()))
for k in okeys:
    print("{} => {} ".format(k,person[k]))

while True:
    key = input("enter a key (q to quit):")
    if key == "q":
        break
    if key in person:
        value = person.get(key)
        print(value)
    else:
        print("we do not have {}".format(key))
            
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
print("zipped dict:",dz)

print(dz.popitem())
print(dz.get('e'))
          