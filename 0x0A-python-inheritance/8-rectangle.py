#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation os a recatangle"""
    def __init__(self, width, height):
        """installation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
