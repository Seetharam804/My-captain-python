# My-captain-python 
#Task 1 :Program to find the area of circle 
import math 
r=int(input("enter the radius="))
Area=math.pi*(r**2)
print("Area of circles is",Area)

#Task 2: Program to find the extension of file 

import pathlib
filename=input("enter the file name=") 
file_ext=pathlib.path(filename).suffix 
print("The extension of file name is",file_ext)
