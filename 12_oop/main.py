from enemy import Troll, Vampyre, VampyreKing
from player import Player

a = 3
b = "tim"
c = 1, 2, 3

print(a)
print(b)
print(c)
p1 = Player("Peter")
print(p1)

t1 = Troll("To")
t1.take_damage(5)
print(t1)

v1 = Vampyre("Vlad")
print(v1)
v1.take_damage(3)
print(v1)

v2 = VampyreKing("Dave")
print(v2)
v2.take_damage(16)
print(v2)
