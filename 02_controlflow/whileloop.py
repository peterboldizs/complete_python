import random

print("simplest while loop")
i = 0
while i < 5:
    print("i is {}".format(i))
    i += 1

options = ["a", "b", "c"]
chosen = ""
while chosen not in options:
    chosen = input("please choose (q for quit): ")
    if chosen == "q":
        print("game over")
        break
else:  # if there was no break
    print("Thanks for choosing: {}".format(chosen))

n = 27
print("convert ", n, " to binary - first option")
remainders = []
while n > 0:
    rem = n % 2
    remainders.append(rem)
    n //= 2
remainders = remainders[::-1]
print("result: ", remainders)

rems = []
n = 27
print("convert ", n, " to binary  - second option")
while n > 0:
    n, rem = divmod(n, 2)
    rems.append(rem)
rems = rems[::-1]
print("better result: ", rems)

names = ['peter', 'marti', 'david', 'dori', 'anna']
ages = [48, 47, 18, 17, 12]
pos = 0
while pos < len(names):
    n = names[pos]
    a = ages[pos]
    print("Name: {0}, age: {1}".format(n, a))
    pos += 1

print("number guessing")
highest = 5
answer = random.randint(1, highest)
print("please guess a number up to {}".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if guess > answer:
        print("guess lower")
    elif guess < answer:
        print("guess higher")
    else:
        print("well done")
