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
        buildings = []
        people = []
        for i in range(5):
            for j range(5):
                buildings.append(town.Building(i*town.Building.BUILDING_SIZE,
                j*town.Building.BUILDING_SIZE, random.randint(len(town.BUILDINGS)),
                true))