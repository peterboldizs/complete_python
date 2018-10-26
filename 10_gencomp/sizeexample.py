import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range returns {}".format(start))
        yield start
        start += 1


big_range = range(5)
print("size of big range is {} bytes".format(sys.getsizeof(big_range)))
# _ = input("line 15")

big_list = []
for val in big_range:
    big_list.append(val)
print("size of big list is {} bytes".format(sys.getsizeof(big_list)))
print("-" * 40)
my_big_range = my_range(5)
print(next(my_big_range))
print("size of my big range is {} bytes".format(sys.getsizeof(my_big_range)))

my_big_list = []
# _ = input("line 27")
for val in my_big_range:
    # _ = input("line 29 - in side for loop")
    my_big_list.append(val)
print("size of my big list is {} bytes".format(sys.getsizeof(my_big_list)))
print(my_big_range)
print(my_big_list)
print("-" * 40)
print("loop again?")
for i in my_big_range:
    print("i is {}".format(i))

print(big_range)
for j in big_range:
    print("j is {}".format(j))
