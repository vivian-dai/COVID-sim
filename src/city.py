import town
import random
import pygame
"""
city.py
A predefined template for a city
"""
happiness = 100

class City:
    """
    A template for a City
    """
    def __init__(self):
        """
        ...constructor for a City
        """
        
        self.buildings = []
        self.people = []
        building_types = []
        for i in range(len(town.BUILDINGS)):
            building_types.append(i)
        random.shuffle(building_types)
        for i in range(5):
            for j in range(5):
                self.buildings.append(town.Building(i*town.Building.BUILDING_SIZE + i*10,
                j*town.Building.BUILDING_SIZE + j*10, building_types[(i*j)%len(building_types)], True))

        sexes = ['M', 'F']
        tf = [True, False]
        for i in range(1000):
            
            occupation = random.randint(0, len(town.PROFESSIONS) - 1)
            sex = random.choice(sexes)
            if town.PROFESSIONS[occupation] == "Unemployed":
                age = random.randint(0, 100)
                if age >= 65:
                    possible_buildings = []
                    for j in self.buildings:
                        if town.BUILDINGS[int(j.building_type_index)] == "Elderly":
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(town.Person(random.choice(possible_buildings), 
                        age, occupation, sex, random.choice(tf), random.choice(tf)))
                else:
                    possible_buildings = []
                    for j in self.buildings:
                        if town.BUILDINGS[int(j.building_type_index)] == "Residential":
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(town.Person(random.choice(possible_buildings), 
                        age, occupation, sex, random.choice(tf), random.choice(tf)))
            elif town.PROFESSIONS[occupation] == "Doctor":
                age = random.randint(25, 65)
                possible_buildings = []
                for j in self.buildings:
                    if town.BUILDINGS[int(j.building_type_index)] == "Hospital":
                        possible_buildings.append(j)
                if len(possible_buildings) > 0:
                    self.people.append(town.Person(random.choice(possible_buildings), 
                    age, occupation, sex, random.choice(tf), random.choice(tf)))
            elif town.PROFESSIONS[occupation] == "Business owner":
                age = random.randint(25, 65)
                possible_jobs = ["Retail", "Food", "Residential", "Entertainment", 
                "Police station", "9-5 job", "School"]
                possible_buildings = []
                for j in self.buildings:
                    if town.BUILDINGS[int(j.building_type_index)] in possible_jobs:
                        possible_buildings.append(j)
                if len(possible_buildings) > 0:
                    self.people.append(town.Person(random.choice(possible_buildings), 
                    age, occupation, sex, random.choice(tf), random.choice(tf)))
            elif town.PROFESSIONS[occupation] == "From home":
                age = random.randint(25, 65)
                possible_buildings = []
                for j in self.buildings:
                    if town.BUILDINGS[int(j.building_type_index)] == "Residential":
                        possible_buildings.append(j)
                if len(possible_buildings) > 0:
                    self.people.append(town.Person(random.choice(possible_buildings), 
                    age, occupation, sex, random.choice(tf), random.choice(tf)))
            
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
                if (happiness < 25) or (random.randInt(0,4) == 0):
                    throwAway = True
                    throwCounter = 0
                    while throwAway:
                        if (self.people[throwCounter].infected == False):
                            self.people[throwCounter].infected = True;
                            throwAway = False
                        throwCounter +=  1
                if (self.people[i].age >= 65 or self.people[i].chronic_disease) and (random.randInt(0,150) == 0):
                    self.people[i].hospitalized = True
                    self.people[i].timer = -1
                self.people[i].timer += 1
                if (self.people[i].timer == 56):
                    self.people[i].cured = True
                    cured += 1
                    infected -= 1
                    
            for i in range(len(self.buildings)):
                self.buildings = []
            
            return cured, infected