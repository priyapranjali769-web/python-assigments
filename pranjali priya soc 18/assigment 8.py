#CREATING A FILE NAMES SHAPES

#To find area of the shapes using modules
import math
def circle_area(radius):
    return math.pi*radius**2

def rectangle_area(length,bredth):
    return length*bredth

def triangle_area(base,height):
    return 0.5*base*height


#NEXT FILE CODE TO IMPORT ABOVE FILE

import shapes
print("Choose your shape:")
print("1,For circle")
print("2, For Rectangle")
print("3, For triangle")

#Taking the choices input from the user
choices = int(input("Enter your choice  of the shapes:"))

#Applying the conditions for the choices
if choices == 1:
    r = float(input("Enter the radius of the circle:"))       #For finding area of circle
    area = shapes.circle_area(r)
    print("The area of youe circle is:",area)

elif choices == 2:
    l = float(input("Enter the length of the rectangle:"))       #For finding area of rectangle
    b = float(input("Enter the bredth of the rectangle:"))
    area = shapes.rectangle_area(l,b)
    print("The area of the rectangle is:")

elif choices == 3:
    base = float(input("Enter the base of the triangle:"))        #For finding area of triangle
    h = float(input("Enter the height of the triangle:"))
    area = shapes.triangle_area(base,h)

else:
    print("There are no further choices for the shapes")