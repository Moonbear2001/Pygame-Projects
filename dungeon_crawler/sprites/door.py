import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Door(pygame.sprite.Sprite):

    len1 = 5
    len2 = 20

    coords = {"north": (SCREEN_WIDTH // 2, 0),
              "south": (SCREEN_WIDTH // 2, SCREEN_HEIGHT),
              "east": (0, SCREEN_HEIGHT // 2),
              "west":(SCREEN_WIDTH, SCREEN_HEIGHT // 2)}

    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.rect = pygame.Rect((self.coords[direction]), (self.len1, self.len2))
        self.image = pygame.Surface((self.len1, self.len2))
        self.image.fill("white")
