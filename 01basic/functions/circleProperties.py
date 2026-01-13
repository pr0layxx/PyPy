def circle(radius):
    area = 3.14 * (radius**2)
    circumference = 2 * 3.14 * radius
    return area, circumference

a, c = circle(3)
print("Area of circle is:", a , "and the circumference is: ", c)
