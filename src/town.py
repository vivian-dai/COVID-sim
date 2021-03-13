"""
town.py
Contains a bunch of classes that are used throughout the town
"""

#-------------------------------CONSTANTS-------------------------------#
PROFESSIONS = ["Unemployed", "Doctor", "Buiseness owner", "From home"]
BUILDINGS = ["Hospital", "Retail", "Food", "Residential", "Entertainment", 
"Police station", "9-5 job", "Elderly"]
R_NAUGHT = 2.68
FATALITY_RATE = 0.001

def get_happiness(building_index):
    """gets the happiness loss based on Building type

    Args:
        building_index (int): index of the Buiding

    Returns:
        [int]: happiness which the Building provides
    """
    if BUILDINGS[building_index] == "Hospital":
        return 5
    elif BUILDINGS[building_index] == "Retail":
        return 5
    elif BUILDINGS[building_index] == "Food":
        return 10
    elif BUILDINGS[building_index] == "Entertainment":
        return 15
    elif BUILDINGS[building_index] == "Police station":
        return 7
    elif BUILDINGS[building_index] == "9-5 job":
        return 1
    elif BUILDINGS[building_index] == "Elderly":
        return 3
    else:
        return None

class Building:
    """
    Building class template
    """
    BUILDING_SIZE = 64
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
    def __init__(self, x, y, age, profession_index, sex, infected, mask):
        """Constructor for the Person class

        Args:
            x (int): the x position of the Person
            y (int): the y position of the Person
            age (int): how old the Person is
            profession_index (int): index of the Person's profession
            sex (char): Person's sex
            infected (boolean): if the Person is infected
            mask (boolean): if the Person is wearing a mask
        """
        self.x = x
        self.y = y
        self.age = age
        self.profession_index = profession_index
        self.sex = sex
        self.infected = infected

    def move(self, new_x, new_y):
        """Moves the Person to new_x and new_y

        Args:
            x_change (int): new x position
            y_change (int): new y position
        """
        self.x = new_x
        self.y = new_y