import city
import town
import pygame
"""
main.py
The main program (run this!!!)
"""
pygame.init()
#---------------------------VARIABLES---------------------------#
sim = city.City()
screen = pygame.display.set_mode((town.Building.BUILDING_SIZE*5 + 256, town.Building.BUILDING_SIZE*5))
building_type_string = ""
main_font = pygame.font.SysFont('Comic Sans MS', 12)

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            if mousex <= town.Building.BUILDING_SIZE*5:
                for building in sim.buildings:
                    if building.is_inside(mousex, mousey):
                        building_type_string = town.BUILDINGS[building.building_type_index]
                        print(building_type_string)
    
    for building in sim.buildings:
        x = building.x
        y = building.y
        size = town.Building.BUILDING_SIZE
        pygame.draw.rect(screen, (255, 0, 0), (x, y, size, size), 1)

    text = main_font.render(building_type_string, 0, (255, 0, 0))
    screen.blit(text, (town.Building.BUILDING_SIZE*5, 12))


    pygame.display.flip()
