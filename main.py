import pygame
import random
from characters import Cube
from characters import Enemy


def manage_keys(keys):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        cube.y -= cube.speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        cube.y += cube.speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cube.x -= cube.speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cube.x += cube.speed

WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
FPS = 60

clock = pygame.time.Clock()

time_spent = 0
time_between_enemies = 1000

playing = True

cube = Cube(100, 100)
enemies = []


while playing:
    time_spent += clock.tick(FPS)

    if time_spent > time_between_enemies:
        enemies.append(Enemy(random.randint(5, WIDTH), 25))
        time_spent = 0
    events = pygame.event.get()

    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            playing = False
    
    WINDOW.fill('black')
    for enemy in enemies:
        enemy.draw(WINDOW)
        enemy.movement()
    cube.draw(WINDOW)
    manage_keys(keys)
    pygame.display.update()

quit()