import pygame

from game import *
from sprites import *
from constants import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Game setup
protagonist = Protagonist(screen, 50)

# Map setup
current_dungeon = Dungeon(screen, DUNGEON_FOLDER)
current_dungeon.load_from_json("dungeon1")

# Main game loop
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Logic
    protagonist.update()

    
    # RENDER YOUR GAME HERE
    current_dungeon.draw()
    protagonist.draw()


    pygame.display.flip()
    clock.tick(FPS)  

pygame.quit()