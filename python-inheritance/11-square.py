#!/usr/bin/python3
"""
Defines the Square class inheriting from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
