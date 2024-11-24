import pygame
import os
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(MAIN_DIR, 'assets')

class Cube:
    width = 80
    height = 80
    speed = 7.5
    colour = 'green'
    image = pygame.image.load(f'{ASSETS_DIR}/xwing.png')
    image = pygame.transform.scale(image, (100,100))

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.bullets = []
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
        window.blit(self.image, (self.x, self.y))
    
    def generate_bullets(self):
        self.bullets.append(Bullet(self.rect.centerx - 7, self.rect.centery - 15))


class Bullet:
    width = 10
    height = 20
    speed = 7.5
    colour = 'blue'
    image = pygame.image.load(f'{ASSETS_DIR}/laser.jpg')
    image = pygame.transform.scale(image, (35, 45))

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
        window.blit(self.image, (self.x, self.y))

    def movement(self):
        self.y -= self.speed


class Enemy:
    width = 150
    height = 100
    speed = 4
    colour = 'red'
    image = pygame.image.load(f'{ASSETS_DIR}/tie.jpg')
    image = pygame.transform.scale(image, (150, 100))
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.life = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def movement(self):
        self.y += self.speed

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
        window.blit(self.image, (self.x, self.y))


class Heart:
    width = 30
    height = 30
    speed = 4
    colour = 'red'
    image = pygame.image.load(f'{ASSETS_DIR}/heart.jpg')
    image = pygame.transform.scale(image, (30, 30))

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def movement(self):
        self.y += self.speed

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
        window.blit(self.image, (self.x, self.y))


class Reward:
    width = 30
    height = 30
    speed = 4
    colour = 'red'
    image = pygame.image.load(f'{ASSETS_DIR}/infinite.webp')
    image = pygame.transform.scale(image, (60, 60))

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def movement(self):
        self.y += self.speed

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
        window.blit(self.image, (self.x, self.y))