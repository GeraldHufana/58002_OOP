# This is a sample Python script.

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159

    def perimeter(self):
        return 2 * self.pi * self.radius
    def area(self):
        return self.pi * self.radius ** 2

    def Display(self):
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())

radius = float(input("Enter the radius of the circle: "))
c = Circle(radius)
c.Display()

