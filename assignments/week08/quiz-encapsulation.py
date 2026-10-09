"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init(self, length, width):
        self.__length = length
        self.__wideh = width

        def gerArea(self):
            return f"Area of {self.__width} width and {self.__lenfth} length = { self.__width * self.__length}"

        def getPerimeter(self):
            return f"Perimeter of {self.__width} width and {self.__lenfth} length = {2 * (self.__width + self.__length)}"

        def isSquare(self):
            return self .__width == self.__length


myRectangle = Rectangle(5, 10)
myRectangle.__length = -5

print(myRectangle.getArea())

myRectangle2 = Rectangle(10, 10)
print(myRectangle2.isSquare())