'''
Practical 3

Compute volume of following 3D shapes: cube, cylinder, cone and sphere.
'''

from math import pi

radius = float(input("Enter a radius: "))
height = float(input("Enter a height: "))

# Cube
print(f"Volume of cube with side {height} is {height**3}")

# Cylinder
print(f"Volume of cylinder with radius {radius} and height {height} is {pi*radius**2*height}")

# Cone
print(f"Volume of cone with radius {radius} and height {height} is {1/3*pi*radius**2*height}")

# Sphere
print(f"Volume of sphere with radius {radius} is {4/3*pi*radius**3}")
