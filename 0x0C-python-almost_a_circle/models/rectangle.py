#!/usr/bin/python3
""" SUBCLASS RECTANGLE TO INHERIT FROM THE BASE"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class inherits base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ instance representation of the object """
        str = f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"
        return str

    @property
    def width(self):
        """ width getter function"""
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter function """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

    @property
    def height(self):
        """ height getter function """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter function"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

    @property
    def x(self):
        """ x getter function """
        return self.__x

    @x.setter
    def x(self, x):
        """  x setter function """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

    @property
    def y(self):
        """ y getter function """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter function """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y

    def area(self):
        """ Area of a Rectangle computed"""
        return self.__width * self.__height

    def display(self):
        """ display # rectangle """
        str = ""
        if self.width == 0 or self.height == 0:
            print(str)
            return
        for y in range(self.y):
            str = str + "\n"
        for i in range(self.height):
            for x in range(self.x):
                str = str + " "
            for j in range(self.width):
                str = str + '#'
            str = str + '\n'
        print("{}".format(str), end="")

    def update(self, *args, **kwargs):
        """ update no key arguments """
        if args and len(args) > 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ rectangle object to dictionary """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
