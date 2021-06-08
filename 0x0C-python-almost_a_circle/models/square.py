#!/usr/bin/python3
""" Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, size):
        """ set width and height """
        self.width = size
        self.height = size

    def __str__(self):
        """Str print"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    def update(self, *args, **kwargs):
        """Update the values of the square"""
        if args is not None and len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
        else:
            if len(args) < 1:
                return
            self.id = args[0]
            if len(args) < 2:
                return
            self.width = args[1]
            self.height = args[1]
            if len(args) < 3:
                return
            self.x = args[2]
            if len(args) < 4:
                return
            self.y = args[3]

    def to_dictionary(self):
        """Add the items of a rectangle into a dictionary"""
        dct = {}
        dct.setdefault('id', self.id)
        dct.setdefault('size', self.width)
        dct.setdefault('x', self.x)
        dct.setdefault('y', self.y)
        return dct
