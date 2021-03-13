"""
town.py
Contains a bunch of classes that are used throughout the town
"""

#-------------------------------CONSTANTS-------------------------------#
PROFESSIONS = ["Doctor", "Citizen"]
BUILDINGS = ["Hospital", "Commerce", "Food"]

class Building:
    """
    Building class template
    """
    def __init__(self, x, y, building_type_index, is_open):
        """ Constructor for the Building class

        Args:
            x (int): the x position of the Building
            y (int): the y position of the Building
            building_type_index (int): index of the type of Building
            open (boolean): if the Building is open or not
        """
        self.x = x
        self.y = y
        self.building_type_index = building_type_index
        self.open = is_open

class Person:
    """
    Person class template
    """
    def __init__(self, x, y, age, profession_index, sex, happiness):
        """Construcotr for the Person class

        Args:
            x (int): the x position of the Person
            y (int): the y position of the Person
            age (int): how old the Person is
            profession_index (int): index of the Person's profession
            sex (char): Person's sex
            happiness (int): how happy the Person is
        """
        self.x = x
        self.y = y
        self.age = age
        self.profession_index = profession_index
        self.sex = sex
        self.happiness = happiness

    def move(self, x_change, y_change):
        """Moves the Person by x_change horizontally and y_change vertically

        Args:
            x_change (int): change in x
            y_change (int): change in y
        """
        self.x += x_change
        self.y += y_change