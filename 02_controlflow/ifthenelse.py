print("if-the-else")
late = False

if late:
    print("call manager")
else:
    print("do not call him")

pay = 50000

if pay < 100:
    tax = 0.1
elif pay < 500:
    tax = 0.3
elif pay < 1000:
    tax = 0.5
else:
    tax = 0.75

taxed_pay = pay - (pay * tax)
print("pay: {0}, tax:  {1},  taxed_pay: {2}".format(pay, tax, taxed_pay))

myname = input("what is your name: ")
age = int(input("how old are you: "))
if (age >= 16) and (age <= 65):
    print("adult")
else:
    print("student")

if 18 <= age < 31:
    print("welcome to the trip, {}".format(myname))
else:
    print("you cannot com to the trip")

if (age < 16) or (age > 65):
    print("free time")

letter = input("enter a letter: ")
if letter in myname:
    print("I have {} in my name".format(letter))
else:
    print("I do not have {} in my name".format(letter))
