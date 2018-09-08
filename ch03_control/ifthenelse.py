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

age = int(input("how old are you: "))
if (age >= 16) and (age <= 65):
    print("adult")
else:
    print("student")
    

if 18 < age < 25:
    print("university")
else:
    print("other")

if (age < 16) or (age > 65):
    print("free time")