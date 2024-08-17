import pygame


class Cube:
    width = 100
    height = 100
    speed = 7.5
    colour = 'green'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.bullets = []
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
    
    def generate_bullets(self):
        self.bullets.append(Bullet(self.rect.centerx - 5, self.rect.centery))


class Bullet:
    width = 10
    height = 20
    speed = 7.5
    colour = 'blue'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)
    def movement(self):
        self.y -= self.speed


class Enemy:
    width = 75
    height = 75
    speed = 4
    colour = 'red'

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


class Heart:
    width = 30
    height = 30
    speed = 4
    colour = 'red'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def movement(self):
        self.y += self.speed

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)