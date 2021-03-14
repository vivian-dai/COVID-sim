import pygame
import city
import random
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
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (128,0,128)
ORANGE = (255,128,0)
TEAL = (0,128,128)
GREY = (128,128,128)

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
        

        if self.building_type_index == 0:
            colour = RED
        elif self.building_type_index == 1:
            colour = TEAL
        elif self.building_type_index == 2:
            colour = GREEN
        elif self.building_type_index == 3:
            colour = BLACK
        elif self.building_type_index == 4:
            colour = PURPLE
        elif self.building_type_index == 5:
            colour = BLUE
        elif self.building_type_index == 6:
            colour = GREY
        elif self.building_type_index == 7:
            colour = ORANGE
        else:
            colour = YELLOW

        if self.open:
            pygame.draw.rect(screen, colour,(self.x, self.y, 64,64), 2)
        else:
            pygame.draw.rect(screen, colour,(self.x, self.y, 64, 64))


class Person:
    """
    Person class template
    """
    def __init__(self, building, age, profession_index, sex, chronic_disease, residence):
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
        self.residence = residence
        self.building = building
        self.age = age
        self.profession_index = profession_index
        self.sex = sex
        self.infected = False
        self.chronic_disease = chronic_disease
        self.hospitalized = False
        self.timer = 0
        self.death_timer = 0
        self.cured = False
        
        

    def move(self, building):
        """Moves the Person to the Building builing

        Args:
            building (Building)
            """
        if not (self.hospitalized):
            if (self.profession_index == 0):
                if time == (0 or 18):
                    self.residence.people.append(self)
                elif time == 6:
                    happy = False
                    for i in range(len(city.City().entertainment_list)):
                        if (city.City().entertainment_list[i].open):
                            city.City().entertainment_list[i].people.append(self)
                            happy = True
                            break
                    if not happy:
                        city.City().happiness -= 5
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
                    happy = False
                    for i in range(len(city.City().entertainment_list)):
                        if (city.City().entertainment_list[i].open):
                            city.City().entertainment_list[i].people.append(self)
                            happy = True
                            break
                    if not happy:
                        city.City().happiness -= 5
                else:
                    self.residence.people.append(self)
            else:
                if time == (12 or 18):
                    self.building.people.append(self)
                elif time == 0:
                    happy = False
                    for i in range(len(city.City().entertainment_list)):
                        if (city.City().entertainment_list[i].open):
                            city.City().entertainment_list[i].people.append(self)
                            happy = True
                            break
                    if not happy:
                        city.City().happiness -= 5
                else:
                    self.residence.people.append(self)
        else:
            for i in range(len(city.City().hospital_list)):
                if (city.City().hospital_list[i].open) and (len(city.City().hospital_list[i].people) < 64):
                    self.deathTimer = 0
                    city.City().hospital_list[i].people.append(self)
                    break