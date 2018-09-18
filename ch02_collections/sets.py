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
my_set.discard(2)
print(3 in my_set)
print(4 in my_set)
my_set.add(3)
print("my_set: {}".format(my_set))
#  my_set2 = set([7, 11, 13, 17])
my_set1 = {11, 13}
my_set2 = set([7, 11, 13, 17])
print("my_set1: {}".format(my_set1))
print("my_set2: {}".format(my_set2))
print("my_set1.issubset(my_set2): {}".format(my_set1.issubset(my_set2)))
#print(my_set | my_set2)
print("difference: {}".format(my_set.difference(my_set2)))
my_set.difference_update(my_set2)
print("difference_update: {}".format(my_set))
my_set.symmetric_difference(my_set2)
print("symmetric_difference: {}".format(my_set))
#print(my_set + my_set2)
print("union: {}".format(my_set.union(my_set2)))
#print(my_set - my_set2)
print("intersection: {}".format(my_set.intersection(my_set2)))
my_set3 = {2, 3, 3, 5, 5, 7}
print(my_set3)

my_set4 = set(["A", "B", "C", "A"])
print(my_set4)
my_set4.add("D")
my_set4.add("C")

for i in my_set4:
    print(i)
    
my_set5 = {"E", "F", "G"}
print("union: {}".format(my_set4.union(my_set5)))
print("sorted union: {}".format(sorted(my_set4.union(my_set5))))
print("intersection: {}".format(my_set2.intersection(my_set3)))

text = "This is the beginning of a beautiful friendship"
vowels = frozenset("aeuio")
mod_text = set(text).difference(vowels)
print(sorted(mod_text))
