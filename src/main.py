import city
import town
import pygame
"""
main.py
The main program (run this!!!)
"""
pygame.init()
sim = city.City()
screen = pygame.display.set_mode((town.Building.BUILDING_SIZE*5, town.Building.BUILDING_SIZE*5))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
    for building in sim.buildings:
        x = building.x
        y = building.y
        size = town.Building.BUILDING_SIZE
        pygame.draw.rect(screen, (255, 0, 0), (x, y, size, size), 1)

    pygame.display.flip()
