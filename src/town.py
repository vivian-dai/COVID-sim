import pygame
import random
import city
"""
town.py
Contains a bunch of classes that are used throughout the town
"""

#-------------------------------CONSTANTS-------------------------------#
PROFESSIONS = ["Unemployed", "Doctor", "Buiseness owner", "From home"]
BUILDINGS = ["Hospital", "Retail", "Food", "Residential", "Entertainment", 
"Police station", "9-5 job", "Elderly", "School"]
R_NAUGHT = 2.68
FATALITY_RATE = 0.001
BLACK = (0,0,0)

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
    elif BUILDINGS[building_index] == "School":
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
        self.people = []

    def is_inside(self, x, y):
        """Checks if the coordinates (x, y) is inside the Building

        Args:
            x (int): the x coordinate
            y (int): the y coordinate

        Returns:
            [boolean]: checks if the x and y coordinates are inside this Building with a conditional
        """
        return x >= self.x and x < self.x + self.BUILDING_SIZE and y > self.y and y < self.y + self.BUILDING_SIZE

    def draw(self, screen):
        """Draws the Building

        Args:
            screen (pygame surface): screen to draw on
        """
        if self.open:
            pygame.draw.rect(screen, BLACK,(self.x, self.y, 64,64), 2)
        else:
            pygame.draw.rect(screen, BLACK,(self.x, self.y, 64, 64))


class Person:
    """
    Person class template
    """
    def __init__(self, building, age, profession_index, sex, infected, chronic_disease):
        """Constructor for the Person class

        Args:
            building (Building): the new Building to put the Person in
            age (int): how old the Person is
            profession_index (int): index of the Person's profession
            sex (char): Person's sex
            infected (boolean): if the Person is infected
            mask (boolean): if the Person is wearing a mask
            chronic_disease (boolean): if the person is affected with a chronic disease
        """
        self.residence = True#idk, I'm too lazy
        self.building = building
        self.age = age
        self.profession_index = profession_index
        self.sex = sex
        self.infected = False
        self.chronic_disease = chronic_disease
        self.hospitalized = False
        self.timer = 0
        self.cured = True
        

    def move(self, building, time):
        """Moves the Person to the Building builing

        Args:
            building (Building): which Building to move the Person to
            time (int): the time of day it is

        """
        if self.profession_index == 0:
            if time == (0 or 18):
                self.residence.people.append(self)
            elif time == 6:
                city.entertainmentBuildings[random.randint(0,3)].people.append(self)
            else:
                self.building.people.append(self)
                
        elif self.profession_index == 1:
            if time == (6 or 12 or 18):
                self.building.people.append(self)
            else:
                self.residence.people.append(self)
        elif self.profession_index == 2:
            if time == (6 or 12):
                self.building.people.append(self)
            elif time == 18:
                city.entertainmentBuildings[random.randint(0,3)].people.append(self)
            else:
                self.residence.people.append(self)
        else:
            if time == (12 or 18):
                self.building.people.append(self)
            elif time == 0:
                city.entertainmentBuildings[random.randint(0,3)].people.append(self)
            else:
                self.residence.people.append(self)