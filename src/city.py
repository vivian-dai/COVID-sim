import town
import random
import pygame
"""
city.py
A predefined template for a city
"""

class City:
    """
    A template for a City
    """
    def __init__(self):
        """
        ...constructor for a City
        """
        
        self.buildings = []
        self.entertainmentBuildings = []
        self.people = []
        self.people = []
        self.happiness = 100
        building_types = []
        for i in range(len(town.BUILDINGS)):
            building_types.append(i)
        random.shuffle(building_types)
        for i in range(5):
            for j in range(5):
                self.buildings.append(town.Building(i*town.Building.BUILDING_SIZE + i*10,
                j*town.Building.BUILDING_SIZE + j*10, building_types[(i*j)%len(building_types)], True))
                if ((i*j)%len(building_types) == 1) or ((i*j)%len(building_types) == 2):
                    self.entertainmentBuildings.append(building_types[(i*j)%len(building_types)])
        sexes = ['M', 'F']
        chronically_affected = [True, False, False, False]

        for i in range(1500):


            age_chance = random.randint(0,100)
            sex = random.choice(sexes)
            if (age_chance <= 67): #adult
                occupation = random.randint(1, len(town.PROFESSIONS) - 1)
                age = random.randint(20, 65)

                if town.PROFESSIONS[occupation] == "Doctor":
                    possible_buildings = []
                    for j in self.buildings:
                        if town.BUILDINGS[int(j.building_type_index)] == "Hospital":
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(town.Person(random.choice(possible_buildings), 
                        age, occupation, sex,
                         random.choice(chronically_affected), 1))
                elif town.PROFESSIONS[occupation] == "Business owner":
                    possible_jobs = ["Retail", "Food", "Residential", 
                    "Police station", "9-5 job", "School"]
                    possible_buildings = []
                    for j in self.buildings:
                        if town.BUILDINGS[int(j.building_type_index)] in possible_jobs:
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(town.Person(random.choice(possible_buildings), 
                        age, occupation, sex, 
                         random.choice(chronically_affected), 3))
                elif town.PROFESSIONS[occupation] == "From home":
                    possible_buildings = []
                    for j in self.buildings:
                        if town.BUILDINGS[int(j.building_type_index)] == "Residential":
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(town.Person(random.choice(possible_buildings), 
                        age, occupation, sex, 
                         random.choice(chronically_affected), 3))
            elif (age_chance  <= 90): #youth
                age = random.randint(0, 19)
                self.people.append(town.Person("School", 
                age, "Unemployed", sex, 
                         random.choice(chronically_affected), 3))
            else: #elderly
                age = random.randint(65, 100)
                self.people.append(town.Person("Elderly", 
                age, "Unemployed", sex,
                         random.choice(chronically_affected), "Elderly"))



         
    def draw(self, screen):
        """Draws the City

        Args:
            screen (pygame surface): the screen to draw on
        """
        for i in range(len(self.buildings)):
            self.buildings[i].draw(screen)

    def people_leave(self, cured, infected):
        """calculates how many People in the City are cured and infected

        Args:
            cured (int): number of people that are cured
            infected (int): number of people infected

        Returns:
            [tuple]: (cured[int], infected[int])
        """
        for i in range(len(self.people)):
            if (self.people[i].infected) and not(self.people[i].cured):
                if (self.happiness < 25) or (random.randint(0,4) == 0):
                    throwAway = True
                    throwCounter = 0
                    while throwAway:
                        if (self.people[throwCounter].infected == False):
                            self.people[throwCounter].infected = True
                            throwAway = False
                        throwCounter +=  1
                if (self.people[i].age >= 65 or self.people[i].chronic_disease) and (random.randint(0, 150) == 0):
                    self.people[i].hospitalized = True
                    self.people[i].timer = -1
                self.people[i].timer += 1
                if (self.people[i].timer == 56):
                    self.people[i].cured = True
                    cured += 1
                    infected -= 1
            self.people[i].move()
            return cured, infected