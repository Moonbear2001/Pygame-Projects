import pygame
from pygame.locals import K_w, K_s, K_a, K_d
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class Protagonist(pygame.sprite.Sprite):

    # Where you end up when you enter this type of door
    spawn_positions = {"north": (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.8),
                       "south": (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.2),
                       "east": (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT // 2),
                       "west": (SCREEN_WIDTH * 0.8, SCREEN_HEIGHT // 2)}

    move_speed = 10

    def __init__(self, screen, radius):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.radius = radius
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, radius, radius)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_w] and self.rect.top > 0:
            self.rect.y -= self.move_speed
        if keys[K_s] and self.rect.bottom < SCREEN_HEIGHT:  
            self.rect.y += self.move_speed
        if keys[K_a] and self.rect.left > 0:
            self.rect.x -= self.move_speed
        if keys[K_d] and self.rect.right < SCREEN_WIDTH:  
            self.rect.x += self.move_speed

    def draw(self):
        pygame.draw.circle(self.screen, "blue", self.rect.center, self.radius)

    def position_after_exit(self, exit_direction):
        self.rect.center = self.spawn_positions[exit_direction]