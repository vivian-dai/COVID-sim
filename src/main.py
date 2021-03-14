import pygame
import random

"""
#main.py
#Sunday 13 2021
#Some People
#Biohacks
"""




WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.init()


PROFESSIONS = ["Unemployed", "Doctor", "Business owner", "From home"]
BUILDINGS = ["Hospital", "Retail", "Food", "Residential", 
"Police station", "9-5 job", "Elderly", "School"]
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
    def draw(self):
        if self.open:
            pygame.draw.rect(gameWindow, BLACK,(self.x, self.y, 64,64), 2)
        else:
            pygame.draw.rect(gameWindow, BLACK,(self.x, self.y, 64, 64))

class Person:
    """
    Person class template
    """
    def __init__(self, building, age, profession_index, sex, infected, chronic_disease, residence):
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
        self.cured = True
        

    def move(self, building):
        """Moves the Person to the Building builing

        Args:
            building (Building)
        

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

        

gameWindow = pygame.display.set_mode((800, 600))




def redrawgameWindow(time):
    gameWindow.fill(WHITE)#fill background with white

    displayText(pygame.font.SysFont ("Comic Sans MS", 16), "Susceptible " + str(susceptible), BLACK, (500, 100), "CENTER")
    displayText(pygame.font.SysFont ("Comic Sans MS", 16), "Infected " + str(infected), BLACK, (500, 200), "CENTER")
    displayText(pygame.font.SysFont ("Comic Sans MS", 16), "Cured " + str(cured), BLACK, (500, 300), "CENTER")
    displayText(pygame.font.SysFont ("Comic Sans MS", 16), "Hospitalized " + str(hospitalized), BLACK, (500, 400), "CENTER")
    displayText(pygame.font.SysFont ("Comic Sans MS", 16), "Time " + str(time), BLACK, (500, 500), "CENTER")
    
    city.draw()
    pygame.display.update()#update the display
    


happiness = 100


class city_Structure():
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
        building_types = []
        for i in range(len(BUILDINGS)):
            building_types.append(i)
        random.shuffle(building_types)
        for i in range(5):
            for j in range(5):
                self.buildings.append(Building(i*Building.BUILDING_SIZE + i*10,
                j*Building.BUILDING_SIZE + j*10, building_types[(i*j)%len(building_types)], True))
                if ((i*j)%len(building_types) == 1) or ((i*j)%len(building_types) == 2):
                    self.entertainmentBuildings.append(building_types[(i*j)%len(building_types)]);

        sexes = ['M', 'F']
        tf = [True, False]
        chronically_affected = [True, False, False, False]
        
        for i in range(1000):

            age_chance = random.randint(0,100)
            sex = random.choice(sexes)
            if (age_chance <= 67): #adult
                occupation = random.randint(1, len(PROFESSIONS) - 1)
                age = random.randint(20, 65)

                if PROFESSIONS[occupation] == "Doctor":
                    possible_buildings = []
                    for j in self.buildings:
                        if BUILDINGS[int(j.building_type_index)] == "Hospital":
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(Person(random.choice(possible_buildings), 
                        age, occupation, sex, random.choice(tf),
                         random.choice(chronically_affected), "Residential"))
                elif PROFESSIONS[occupation] == "Business owner":
                    possible_jobs = ["Retail", "Food", "Residential", 
                    "Police station", "9-5 job", "School"]
                    possible_buildings = []
                    for j in self.buildings:
                        if BUILDINGS[int(j.building_type_index)] in possible_jobs:
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(Person(random.choice(possible_buildings), 
                        age, occupation, sex, random.choice(tf), random.choice(tf),
                         random.choice(chronically_affected)))
                elif PROFESSIONS[occupation] == "From home":
                    possible_buildings = []
                    for j in self.buildings:
                        if BUILDINGS[int(j.building_type_index)] == "Residential":
                            possible_buildings.append(j)
                    if len(possible_buildings) > 0:
                        self.people.append(Person(random.choice(possible_buildings), 
                        age, occupation, sex, random.choice(tf),
                         random.choice(chronically_affected), "Residential"))
            elif (age_chance  <= 90): #youth
                age = random.randint(0, 19)
                self.people.append(Person("School", 
                age, "Unemployed", sex, random.choice(tf),
                         random.choice(chronically_affected), "Residential"))
            else: #elderly
                age = random.randint(65, 100)
                self.people.append(Person("Elderly", 
                age, "Unemployed", sex, random.choice(tf),
                         random.choice(chronically_affected), "Elderly"))
    
    
    def draw(self):
        for i in range(len(self.buildings)):
            self.buildings[i].draw()
    def people_Leave(self):

        for i in range(len(self.people)):
            if (self.people[i].infected) and not(self.people[i].cured):
                if (happiness < 25) or (random.randInt(0,4) == 0):
                    throwAway = True;
                    throwCounter = 0;
                    while throwAway:
                        if (self.people[throwCounter].infected == False):
                            self.people[throwCounter].infected = True;
                            infected += 1
                            susceptible -= 1
                            throwAway = False
                        throwCounter +=  1
                if (self.people[i].age >= 65 or self.people[i].chronic_disease) and (random.randInt(0,150) == 0):
                    self.people[i].hospitalized = true
                    self.people[i].timer = -1
                self.people[i].timer += 1
                if (self.people[i].timer == 56):
                    self.people[i].cured = True
                    cured += 1
                    infected -= 1
                    
        for i in range(len(self.buildings)):
            self.buildings[i].people = [];



def time_Period(time):
    time += 6
    if (time == 24):
        time = 0;
    city.people_Leave()

    



def displayText(font, text, colour, location, centered): #ultra laziness retuns!
    if centered == "LEFT": #if I put left, it'll blit the text normally
        gameWindow.blit(font.render(text, 0, colour),location)
    elif centered == "RIGHT":#blits the text on the right
        size = pygame.font.Font.size(font, text)#gets the characteristics of the text in order to lbit it
        gameWindow.blit(font.render(text, 0, colour),(location[0] - size[0], location[1]))#size is used here in order to determine the coordinates
    else:
        size = pygame.font.Font.size(font, text)#size also used here
        gameWindow.blit(font.render(text, 0, colour),(location[0] - size[0]/2, location[1]))#size is also used here, but this time to centre the text


    
run = True
city = city_Structure()

cooldown = 0
susceptible = 1000
infected = 0
cured = 0
hospitalized = 0

global time
time = 0

while run:
    keys = pygame.key.get_pressed() #get keypresses
    playOnce = True #playonce becomes true at the start of the loop signalling that the loop has played more than one
    pygame.time.delay(17)#sets game at 60 fps
    (mouseX, mouseY) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_SPACE:
                time_Period(time)
    if (mouseX > 0 and mouseX < 370 and mouseY > 0 and mouseY < 370):
        if pygame.mouse.get_pressed()[0] and cooldown == 0:
            if (city.buildings[(5*(int(mouseX/74))+ (int (mouseY/74)))].open):
                city.buildings[(5*(int(mouseX/74))+ (int (mouseY/74)))].open = False
            else:
                city.buildings[(5*(int(mouseX/74))+ (int (mouseY/74)))].open = True
            cooldown = 10;

    
    if (cooldown > 0):
        cooldown-= 1
    print(time)
    redrawgameWindow(time)

pygame.quit()
