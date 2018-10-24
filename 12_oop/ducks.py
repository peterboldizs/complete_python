class Bird(object):

    def __init__(self):
        self._feather = "feather"


class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I think I'll just walk")


class Duck(Bird):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on it, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(Bird):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far South")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")

    def aviate(self):
        print("penguins can also fly")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # if type(duck) is Duck:
        print("adding {} to flock".format(type(duck)))
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)

    #   else:
    #       raise TypeError("cannot add {} to flock".format(str(type(duck).__name__)))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                print("try to make {} fly".format(type(duck)))
                duck.fly()
            except AttributeError as ae:
                problem = ae
        if problem:
            raise problem


def simulate_bird(bird):
    bird.walk()
    bird.swim()
    bird.quack()


if __name__ == '__main__':
    donald = Duck()
    simulate_bird(donald)
    donald.fly()

    percy = Penguin()
    simulate_bird(percy)

    print("-" * 40)
    print("migration simulation")
    d1 = Duck()
    d2 = Duck()
    d3 = Duck()
    m1 = Mallard()

    flock = Flock()
    flock.add_duck(d1)
    flock.add_duck(d2)
    flock.add_duck(d3)
    flock.add_duck(percy)
    flock.add_duck(m1)

    flock.migrate()
