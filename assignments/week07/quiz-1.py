class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    def get_area(self):
        return self.length * self.width

    
    def get_perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(rect.get_area())       
print(rect.get_perimeter())  


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_circumference(self):
        return 2 * 3.14 * self.radius


mycircle = Circle(10)
print(mycircle.get_area())          
print(mycircle.get_circumference()) 