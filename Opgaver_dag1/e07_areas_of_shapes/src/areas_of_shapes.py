#!/usr/bin/env python3

import math
def triangle(base,height):
    return 0.5*base*height

def rectangle(width,height):
    return width*height

def circle(radius):
    return math.pi*radius **2
def main():
    while True:
        shape=input("Chose a shape (triangle,rectangle,circle): ").lower()
        if shape=="":
         break
        elif shape=="triangle":
         base=float(input("Give base of the triangle: "))
         height=float(input("Give height of the triangle: "))
         area=triangle(base,height)
         
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = rectangle(width, height)
       
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = circle(radius)  # Corrected function name here
      
        else:
            print("Unknown shape!")
            continue

        print(f"The area is {area:.6f}")    
    
if __name__ == "__main__":
    main()
