
class Animal:
    pass

class Dog(Animal):

    def talk(self):
        print("Bark")

class Cat(Animal):

    def talk(self):
        print("Mew")


class Payment:
    def pay(self):
        print("Paymment via bank")


class Esewa(Payment):
    def pay(self):
        print("Payment via eswa")

class Khalti(Payment):
    def pay(self):
        print("payment via khalti.")

khalti = Khalti()
eswa = Esewa()

khalti.pay()
eswa.pay()


"""
Make parent class Shape with method area(). Make Circle, Rectangle, 
Triangle childclass, override area() each. Write loop that call area()
 on list of mixed shape objects — polymorphism let same method call work
diff per type.
"""
import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self, r):
        return 3.14* 2**2 # 2^2

class Rectangle(Shape):
    def area(self, l, b):
        return l*b

class Triangle(Shape):
    def area(self, b, h):
        return (b*h)/2


list_of_object = [Circle(), Rectangle(), Triangle()]

for obj in list_of_object:
    obj.area()


class Shape:
    def __init__(self, length):
        self.length = length
 
    def area(self):
        print("Need to implement in child class to get the actual area.")


class Circle(shape):
    def __init__(self, length, radius):
        super().__init__(length)
        self.radius = radius
           
    def Area(self):
        return "Area is"+ 3.14 * self.radius * self.radius
 
class Rectangle(shape):
    def __init__(self, length, breadth):
        super().__init__(length)
        self.breadth = breadth
   
    def Area(self):
            return "Area is"+ 3.14 * self.length * self.breadth
 
class Triangle(shape):
    def __init__(self, length, breadth):
        super().__init__(length)
        self.breadth = breadth
 
    def area(self):
        return "Area of triangle is " + 1/2 * self.length * self.breadth
 
objects = [
     
]
 