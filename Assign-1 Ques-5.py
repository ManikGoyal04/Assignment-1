import math

for angle in range(0, 346, 15):
    radian = math.radians(angle)
    sin = round(math.sin(radian), 4)
    cos = round(math.cos(radian), 4)
    print(angle, '---', sin , cos )