'''
Practical 2

Compute area of following shapes: circle, rectangle, triangle, square, trapezoid and
parallelogram.
'''

from math import pi

# Circle
radius = float(input("Enter a radius of circle: "))
print(f"Area of a circle with radius {radius} is {pi*radius**2}\n")

# Rectangle
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
print(f"Area of rectangle with length {length} and breadth {breadth} is {length*breadth}\n")

# Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print(f"Area of triangle with base {base} and height {height} is {1/2*base*height}\n")

# Square
side = float(input("Enter side of square: "))
print(f"Area of square with side {side} is {side**2}\n")

# Trapezoid
side1 = float(input("Enter side 1 of trapezoid: "))
side2 = float(input("Enter side 2 of trapezoid: "))
height = float(input("Enter height of trapezoid: "))
print(f"Area of trapezoid with side 1 {side1}, size 2 {side2} and height {height} is {1/2*(side1+side2)*height}\n")

# Parallelogram
base = float(input("Enter base of parallelogram: "))
height = float(input("Enter height of parallelogram: "))
print(f"Area of parallelogram with base {base} and height {height} is {base*height}\n")


