#!/usr/bin/python3
"""
This module is composed by a class that defines a rectangle
"""

class Rectangle:
    """Class to define a rectangle"""

    def __init__(self, width=0, height=0):
        """ Method to initialize the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the width value

        Returns:
        width of the rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width value

        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """

        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """Method that returns the value of the height

            Returns: 
                Height of the rectangle
            """

            return self.__height

        @height.setter
        def height(self, value):
            """Method that defines the height

            Args:
                value: height

            Raises:
                TypeError: if height is not an integer
                ValueError: if height is less than zero
            """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
