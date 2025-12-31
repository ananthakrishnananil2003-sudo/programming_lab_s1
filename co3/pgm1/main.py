length = 10 
width = 5 
height = 3 
radius = 4 
import graphics.rectangle 
print("Rectangle:") 
print("Area:", graphics.rectangle.area(length, width)) 
print("Perimeter:", graphics.rectangle.perimeter(length, width)) 
from graphics import circle 
print("\nCircle:") 
print("Area:", circle.area(radius)) 
print("Perimeter:", circle.perimeter(radius)) 
from graphics.threeD_graphics.cuboid import area as cuboid_area, perimeter as cuboid_perimeter 
print("\nCuboid:") 
print("Surface Area:", cuboid_area(length, width, height)) 
print("Total Edge Length:", cuboid_perimeter(length, width, height)) import graphics.threeD_graphics.sphere as sphere_mod 
print("\nSphere:") 
print("Surface Area:", sphere_mod.area(radius)) 
print("Great Circle Perimeter:", sphere_mod.perimeter(radius))
