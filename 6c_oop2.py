class Shape:
    geom_type = 'Generic Shape'
    def area(self):
        raise NotImplementedError
    def get_geom_type(self):
        return self.geom_type


class Plotter:
    def plot(self, ratio, topleft):
        print(("Plotting at {}, ratio: {}".format(topleft, ratio)))


class Polygon(Shape, Plotter):
    geom_type = 'Polygon'


class RegularPolygon(Polygon):
    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon):
    geom_type = 'RegularHexagon'
    def area(self):
        return 1.5 * (3 ** 0.5 * self.side ** 2)


class Square(RegularPolygon):
    geom_type = 'Square'
    def area(self):
        return self.side ** 2

#example objects
hexa = RegularHexagon(10)
print(hexa.geom_type)
print(hexa.area())
print(hexa.plot(0.75, 0.0))

sq = Square(12)
print(sq.geom_type)
print(sq.area())
print(sq.plot(0.75, 0.0))

#sh = Shape()
#print(sh.area()) NotImplementedError
print(sq.__class__.__mro__)
