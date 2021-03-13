"""
town.py
Contains a bunch of classes that are used throughout the town
"""

class Building:
    """
    Building class template
    """
    def __init__(self, x, y):
        """ Constructor for the Building class

        Args:
            x (int): the x position of the Building
            y (int): the y position of the Building
        """
        self.x = x
        self.y = y

class Person:
    """
    Person class template
    """
    def __init__(self, x, y):
        """Constructor for the Person class

        Args:
            x (int): x position of the Person
            y (int): y position of the Person
        """
        self.x = x
        self.y = y