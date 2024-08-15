import pygame


class Cube:
    width = 50
    height = 50
    speed = 7.5
    colour = 'green'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, self.colour, self.rect)


class Enemy:
    width = 75
    height = 75
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