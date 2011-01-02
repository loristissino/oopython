import math

def sector_area(radius, degrees):
    return radius**2*math.pi*degrees/360

print(sector_area(3,90))


sector_area = lambda radius, degrees: radius**2*math.pi*degrees/360

print(sector_area(3,90))

