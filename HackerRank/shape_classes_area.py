'''Problem Description
The program takes the radius from the user and finds the area of the circle using classes.
Problem Solution
1. Take the value of radius from the user.
2. Create a class and using a constructor initialise values of that class.
3. Create a method called as area which returns the area of the class and a method called as perimeter which returns the perimeter of the class.
4. Create an object for the class.
5. Using the object, call both the methods.
6. Print the area and perimeter of the circle.
7. Exit'''
import math
class Rectangle:

    def __init__(self,length,width):
        self.length= length
        self.width= width

    def area(self):

        return self.length*self.width
class Circle:
    def __init__(self, radius):
        self.radius= radius
    def area(self):
        return math.pi*(self.radius**2)

if __name__=='__main__':
    len= 10
    wid= 20
    radius =5
    rect_area= Rectangle(len,wid)
    cir_area= Circle(radius)
    print(rect_area.area())
    print(cir_area.area())
    print(rect_area.area())

    # print(Circle.area(radius))


