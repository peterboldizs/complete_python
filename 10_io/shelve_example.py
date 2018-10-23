import shelve

print("shelve with list")
with shelve.open("shelve_test") as person:
    person["fname"] = "Peter"
    person["lname"] = "Boldizs"
    person["byear"] = 1970

    for key in person:
        print("{}=>{}".format(key, person.get(key)))

print("shelve with dict")
with shelve.open("shelve_test2") as person2:
    person2 = {"fname": "Peter",
               "lname": "Boldizs",
               "byear": 1970}
    print(person2)
    while True:
        dict_key = input("enter attribute (q to quit):")
        if dict_key == "q":
            break
        if dict_key in person2:
            print(person2[dict_key])
        else:
            print("we do not have {}".format(dict_key))

list1 = ["a", "b", "c"]
list2 = ["alfa", "beta", "gamma"]
list3 = ["e1", "e2", "e3"]

with shelve.open("mylists") as mylists:
    mylists["list1"] = list1
    mylists["list2"] = list2
    mylists["list3"] = list3

    print(mylists)
    print("*" * 40)
    print("original shelve")
    for i in mylists.items():
        print(i)

    t_list1 = mylists["list1"]
    t_list1.append("d")
    mylists["list1"] = t_list1
    print("*" * 40)
    print("updated shelve")
    for i in mylists.items():
        print(i)

my_lists2 = shelve.open("mylists", writeback=True)
t_list2 = my_lists2["list2"]
t_list2.append("delta")
my_lists2["list2"] = t_list2

print("*" * 40)
print("updated shelve again")
for i in my_lists2.items():
    print(i)
my_lists2.close()
