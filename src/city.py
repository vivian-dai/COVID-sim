import town
import random
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
                self.buildings.append(town.Building(i*town.Building.BUILDING_SIZE,
                j*town.Building.BUILDING_SIZE, building_types[(i*j)%len(building_types)], True))

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
                age = random.randint(30, 65)
                possible_buildings = []
                for j in self.buildings:
                    if town.BUILDINGS[int(j.building_type_index)] == "Hospital":
                        possible_buildings.append(j)
                if len(possible_buildings) > 0:
                    self.people.append(town.Person(random.choice(possible_buildings), 
                    age, occupation, sex, random.choice(tf), random.choice(tf)))
            elif town.PROFESSIONS[occupation] == "Business owner":
                age = random.randint(30, 65)
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
                age = random.randint(30, 65)
                possible_buildings = []
                for j in self.buildings:
                    if town.BUILDINGS[int(j.building_type_index)] == "Residential":
                        possible_buildings.append(j)
                if len(possible_buildings) > 0:
                    self.people.append(town.Person(random.choice(possible_buildings), 
                    age, occupation, sex, random.choice(tf), random.choice(tf)))