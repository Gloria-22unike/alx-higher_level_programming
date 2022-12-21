#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represents a square."""
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes a new square.
	Args:
		size (int): The size of the new square.
	"""
        self.__size = size
