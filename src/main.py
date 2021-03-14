import pygame
import random
import city
import town

"""
#main.py
#Sunday 13 2021
#Some People
#Biohacks
"""




WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.init()

run = True
city = city.City()

cooldown = 0
susceptible = 1000
infected = 0
cured = 0
hospitalized = 0


game_window = pygame.display.set_mode((800, 600))




def redraw_game_window():
    """
    Redraws the entire game window
    """
    game_window.fill(WHITE)#fill background with white

    display_text(pygame.font.SysFont ("Comic Sans MS", 16), "Susceptible " + str(susceptible), BLACK, (500, 100), "CENTER")
    display_text(pygame.font.SysFont ("Comic Sans MS", 16), "Infected " + str(infected), BLACK, (500, 200), "CENTER")
    display_text(pygame.font.SysFont ("Comic Sans MS", 16), "Cured " + str(cured), BLACK, (500, 300), "CENTER")
    display_text(pygame.font.SysFont ("Comic Sans MS", 16), "Hospitalized " + str(hospitalized), BLACK, (500, 400), "CENTER")
    
    city.draw(game_window)
    pygame.display.update()#update the display
    



time = 0
def time_period(time):
    """updates the time period

    Args:
        time (int): time of day
    """
    time += 6
    if (time == 24):
        time = 0
    cured, infected = city.people_leave(cured, infected)

    



def display_text(font, text, colour, location, centered): #ultra laziness retuns!
    """Displays text on the screen

    Args:
        font (pygame Font): the type of Font to use
        text (string): words to display
        colour (pygame color): colour of the text
        location (tuple): a tuple of coordinates (x [int], y [int]) to draw the text at
        centered (string): description of how the text is aligned
    """
    if centered == "LEFT": #if I put left, it'll blit the text normally
        game_window.blit(font.render(text, 0, colour),location)
    elif centered == "RIGHT":#blits the text on the right
        size = pygame.font.Font.size(font, text)#gets the characteristics of the text in order to lbit it
        game_window.blit(font.render(text, 0, colour),(location[0] - size[0], location[1]))#size is used here in order to determine the coordinates
    else:
        size = pygame.font.Font.size(font, text)#size also used here
        game_window.blit(font.render(text, 0, colour),(location[0] - size[0]/2, location[1]))#size is also used here, but this time to centre the text


while run:
    keys = pygame.key.get_pressed() #get keypresses
    play_once = True #playonce becomes true at the start of the loop signalling that the loop has played more than one
    pygame.time.delay(17)#sets game at 60 fps
    (mousex, mousey) = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    for building in city.buildings:
        if building.is_inside(mousex, mousey) and pygame.mouse.get_pressed()[0] and cooldown == 0:
            building.open = not building.open
            cooldown = 10


    if (cooldown > 0):
        cooldown-= 1
    
    redraw_game_window()

pygame.quit()
