#!/usr/bin/python3
"""  Recangle(BaseGeometry) logic """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """

    # def __init__(self, width, height):
    # self.width = width
    # self.height = height

    def __str__(self):
        """ __str__"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __init__(self, width, height):
        """ object instantiated """
        # super().__init__(self)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height
