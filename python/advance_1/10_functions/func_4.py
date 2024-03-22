import math


def circle_stats(radiuse):
    area = math.pi * radiuse ** 2
    circumferance = 2 * math.pi * radiuse

    return area , circumferance

a , c = circle_stats(3)
print(math.floor(a))
print(math.floor(c))