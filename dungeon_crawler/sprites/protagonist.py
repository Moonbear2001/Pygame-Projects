import pygame
from pygame.locals import K_w, K_s, K_a, K_d

class Protagonist(pygame.sprite.Sprite):

    move_speed = 10

    def __init__(self, screen, radius):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.radius = radius
        self.rect = pygame.Rect(0, 0, radius, radius)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.move_speed
        if keys[K_s]:
            self.rect.y += self.move_speed
        if keys[K_a]:
            self.rect.x -= self.move_speed
        if keys[K_d]:
            self.rect.x += self.move_speed

    def draw(self):
        pygame.draw.circle(self.screen, "blue", self.rect.center, self.radius)