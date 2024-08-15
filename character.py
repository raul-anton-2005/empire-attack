import pygame


class Cube:
    width = 50
    height = 50
    speed = 0.75
    colour = 'green'

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)