#!/usr/bin/python3
print("simple for loops")
print("stepped: ")
for j in range(1, 20, 3):
    print(j)

print("multiplication")
for i in range(1, 5):
    for j in range(1, 5):
        print("{1} * {0} = {2}".format(i, j, i * j))
    print("---------")

numbers = "234,567,789,0"
cleanNum = ''
for i in range(0, len(numbers)):
    if numbers[i] in "0123456789":
        # cleanNum = cleanNum + numbers[i]
        cleanNum += numbers[i]  # augmented assignment
print("\ncleaned number: {}".format(cleanNum))

cleanNumber = int(cleanNum)
minus1000 = cleanNumber - 1000
print("minus 1000 : {}".format(minus1000))

num = 5
mul = 8
ans = 0

print("num={}".format(num))
for i in range(mul):
    ans += num
    print("i={}, ans={}".format(i, ans))

print(ans)
