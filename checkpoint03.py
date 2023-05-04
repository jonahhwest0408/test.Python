#Square
square = float(input("What is the length of a side of the square? "))
side = square **2
print(f"The area of the square is: {side}")

#Rectangle
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
sum = length * width 
print(f"The area of the rectangle is: {sum}")

#Circle
radius = float(input("What is the radius of the circle? "))
circle = 3.14 * (radius ** 2)
print(f"The area of the circle is: {circle}")

#Stretch 1
import math
radius = float(input("What is the radius of the circle? "))
circle = math.pi * (radius ** 2)
print(f"The area of the circle is: {circle}")

#Stretch 2
value = float(input("What is the number value? "))
area_square = value **2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)

print(f"The area of the square: {area_square}")
print(f"The area of the circle: {area_circle}")
print(f"The volume of the cube: {volume_cube}")
print(f"The volume of the sphere: {volume_sphere}")

#Stretch 3
side_2 = float(input("What is the length of the side of the square in cm? "))
square_2 = side_2 ** 2
print(f"The area of the square is: {square_2} cm^2. ")
print(f"The area of the square is also: {square_2 / 10000} m^2. ")

length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is also: {area / 10000} m^2")

radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is also: {area / 10000} m^2")