print("while loop")
n = 27
print("convert ", n, " to binary")
remainders = []
while n > 0:
    rem = n % 2
    remainders.append(rem)
    n //= 2
remainders = remainders[::-1]
print("result: ", remainders)

rems = []
n = 27
print("convert ", n, " to binary")
while n > 0:
    n, rem = divmod(n, 2)
    rems.append(rem)
rems = rems[::-1]
print("better result: ", rems)

names = ['peter', 'marti', 'david', 'dori', 'anna']
ages = [47, 46, 17, 16, 11]
pos = 0
while pos < len(names):
    n = names[pos]
    a = ages[pos]
    print("Name: {0}, age: {1}".format(n, a))
    pos += 1

