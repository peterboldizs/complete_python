class Kettle(object):
    power_source = "electric"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 12.99)
hamilton = Kettle("Hamilton", 14.99)

print("Model: {} = {}".format(kenwood.make, kenwood.price))
print("Model: {} = {}".format(hamilton.make, hamilton.price))
print("Model: {0.make} = {0.price}".format(kenwood))

print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)
print("using class method")
Kettle.switch_on(hamilton)
print(hamilton.on)

kenwood.power = 1.4
print(kenwood.power)
# print(hamilton.power) error

print(Kettle.power_source)
print(hamilton.power_source)

kenwood.power_source = "gas"
print(Kettle.__dict__)
print(hamilton.__dict__)
print(kenwood.__dict__)
