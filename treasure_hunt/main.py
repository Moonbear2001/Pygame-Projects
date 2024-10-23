import pygame
from enum import Enum

from game import *
from sprites import *
from constants import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Dungeon setup
protagonist1 = Protagonist(screen, 50)
current_dungeon = Dungeon(screen, dungeon_name="hard")

# Main game loop
while running:

    # Event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Logic
    current_dungeon.update(protagonist1)
    protagonist1.update()
    
    # Draw
    current_dungeon.draw()
    protagonist1.draw()

    # End game if treasure found
    if current_dungeon.treasure_found:
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()