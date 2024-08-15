import pygame


WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])

playing = True

while playing:
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            playing = False

    pygame.display.update()

quit()