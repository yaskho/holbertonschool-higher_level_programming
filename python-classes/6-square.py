#!/usr/bin/python3
"""Module that defines a class Square with size and position attributes."""


class Square:
    """Represents a square with size and position for printing."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Tuple of 2 positive integers (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): New size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): Tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a valid position tuple.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#' considering position.

        If size is 0, print an empty line.
        Position[1] adds vertical space, position[0] adds horizontal space.
        """
        if self.__size == 0:
            print()
            return

            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
