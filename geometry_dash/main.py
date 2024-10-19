import pygame
import sys
from colors import *

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

FLOOR_HEIGHT = 

# Set up the screen (window)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Project")

clock = pygame.time.Clock()

cube = pygame.transform.scale_by(pygame.image.load("geometry_dash/assets/cube.png"), 0.1)
floor = pygame.image.load("geometry_dash/assets/floor.png")
bg = pygame.image.load("geometry_dash/assets/bg.png")

class Cube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load("geometry_dash/assets/cube.png"), 0.1)
        self.rect = self.image.get_rect()
        self.yvel = 0
        self.gravity = 1
        self.jumping = False
      
    def update(self):
        self.yvel += self.gravity
        self.rect.y += self.yvel



# Main game loop
running = True
while running:
    
    # Handle events (key presses, mouse movement, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic


    # Drawing 
    screen.fill(BACKGROUND_COLOR)
    screen.blit(bg, (0, 0))
    screen.blit(floor, (0, SCREEN_HEIGHT - 100))
    screen.blit(cube, (100, 100))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
