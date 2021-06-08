#!/usr/bin/python3
""" rectangle """


from models.base import Base


class Rectangle(Base):
    """ rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, width):
        """ set width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, height):
        """ set height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, x):
        """ set x """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, y):
        """ set y """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ get area """
        return self.__height * self.__width

    def display(self):
        """ display """
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width, end="\n")

    def __str__(self):
        """ str """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ update of the arguments """
        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']
        else:
            if len(args) < 1:
                return
            self.id = args[0]
            if len(args) < 2:
                return
            self.__width = args[1]
            if len(args) < 3:
                return
            self.__height = args[2]
            if len(args) < 4:
                return
            self.__x = args[3]
            if len(args) < 5:
                return
            self.__y = args[4]

    def to_dictionary(self):
        dct = {}
        dct.setdefault('id', self.id)
        dct.setdefault('width', self.__width)
        dct.setdefault('height', self.__height)
        dct.setdefault('x', self.__x)
        dct.setdefault('y', self.__y)
        return dct
