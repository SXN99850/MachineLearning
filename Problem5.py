import math

# The radius of a circle is 30 meters.
radius_of_circle = 30
PI = math.pi

# 1.Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
_area_of_circle_ = PI * radius_of_circle ** 2
print("Area of circle with radius 30meters is %.3f" % _area_of_circle_)

# 2.Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * PI * radius_of_circle
print("Circumference of circle is %.3f" % _circum_of_circle_)

# 3.Take radius as user input and calculate the area
radius_of_user_circle = int(input("Enter radius of circle: "))
_area_of_user_circle_ = PI * radius_of_user_circle ** 2
print("Area of circle with radius:", radius_of_user_circle, "is %.3f" % _area_of_user_circle_)
