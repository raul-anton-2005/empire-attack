import pygame
from character import Cube


WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])

playing = True
cube = Cube(100, 100)

while playing:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            playing = False
    cube.draw(WINDOW)
    pygame.display.update()

quit()