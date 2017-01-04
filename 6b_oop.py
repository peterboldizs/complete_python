print("OOP concepts")


class Point():
    x = 4
    y = 10

p = Point()
print(p.x)
print(p.y)
p.x = 12
print(p.x)
print(Point.x)
del p.x
print(p.x)
p.z = 5
print(p.z)
# print(Point.z) AttributeError: type object 'Point' has no attribute 'z'

print("square")
class Square():
    side = 8
    def area(self):
        return self.side ** 2

sq = Square()
print(sq.area())
sq.side = 10
print(sq.area())

print("rectangle")
class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b

r1 = Rectangle(10, 4)
print(r1.area())


