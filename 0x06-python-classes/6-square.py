#!/usr/bin/python3
"""6-square
a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Square class init, assign a value to
        Args:
            size (int): The private arg size of the square.
            position (tuple): bfbf
        Raise:
            ValueError: If size is less than Zero
            TypeError: If size is not an integer or isn't a tuple
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not type(position) == tuple or not len(position) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(position)):
            if not type(position[i]) == int or position[i] < 0:
                str1 = 'position must be a tuple of 2'
                raise TypeError(str1 + ' positive integers')
        self.__size = size
        self.__position = position

    def area(self):
        """Method to calc the area of a square.
        Returns:
            The area of a square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Method getter.
        Returns:
            The size of a square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method setter: set the size
        Args:
            value (int): The private arg size of the square.
        Raise:
            ValueError: If value is less than Zero
            TypeError: If value is not an integer
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Method that prints in stdout the square with the character"""
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
    
    @property
    def position(self):
        """ Method:
        Return: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method setter: set the position
        Args:
            value (int): tuple with 2 values
        Raise:
            TypeError: If tuple not contains 2 integers
        """
        if not type(value) == tuple or not len(value) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(value)):
            if not type(value[i]) == int or value[i] < 0:
                str1 = 'position must be a tuple of 2'
                raise TypeError(str1 + ' positive integers')
        self.__position = value
