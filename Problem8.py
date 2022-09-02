radius = 10
area = 3.14 * radius ** 2

# Using string formatter %d, area is displayed
print("Area before formatting", area)
print("The area of a circle with radius 10 is %(area)d meters square" % {"area": area})
#another way
print("The area of a circle with radius 10 is %d meters square" % area)
