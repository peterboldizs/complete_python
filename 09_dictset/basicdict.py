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
# person.clear()

person["byear"] = 1977
print("contents")
for attr in person:
    print("{} = {} ".format(attr, person[attr]))

print("contents sorted")
# okeys = list(person.keys())
# okeys.sort()
okeys = sorted(list(person.keys()))
for k in okeys:
    print("{} => {} ".format(k, person[k]))

while True:
    key = input("enter a key (q to quit):")
    if key == "q":
        break
    if key in person:
        value = person.get(key)
        print(value)
    else:
        print("we do not have {}".format(key))
