import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TREASURE_SIZE

class Treasure:

    gold_color = (218, 165, 32)

    def __init__(self, screen):
        self.screen = screen
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, TREASURE_SIZE, TREASURE_SIZE)
        self.image = pygame.Surface((TREASURE_SIZE, TREASURE_SIZE))

    def draw(self):
        pygame.draw.circle(self.screen, self.gold_color, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), TREASURE_SIZE)

