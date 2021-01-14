import math


def f(x):
    y = 4 * x
    y = math.radians(y)
    return (2 * math.cos(y)) / x

total = 0

list = [1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75]

for i in list:
    total += f(i)

total = total / 2

print(total)
