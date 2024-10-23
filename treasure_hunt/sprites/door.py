import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Door(pygame.sprite.Sprite):

    len1 = 10
    len2 = 100

    coords = {"north": (SCREEN_WIDTH // 2, 0),
              "south": (SCREEN_WIDTH // 2, SCREEN_HEIGHT),
              "west": (0, SCREEN_HEIGHT // 2),
              "east":(SCREEN_WIDTH, SCREEN_HEIGHT // 2)}

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        dimensions = (self.len2, self.len1) if (direction == "north" or direction == "south") else (self.len1, self.len2)
        self.rect = pygame.Rect((0, 0), dimensions)
        self.rect.center = self.coords[direction]
        self.image = pygame.Surface(dimensions)
        self.image.fill("white")
