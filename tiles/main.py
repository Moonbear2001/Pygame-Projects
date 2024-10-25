import pygame
import sys
from pathlib import Path

from level import Level
from constants import *


pygame.init()

# Constants

FPS = 60
BACKGROUND_COLOR = (0, 0, 0) 

# Set up the screen (window)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Project")

clock = pygame.time.Clock()

# Game setup
test_level_path = Path(__file__).parent / "levels" / "1.json"
level = Level(test_level_path)

def main():
    
    # Main game loop
    running = True
    while running:
        
        # Handle events (key presses, mouse movement, etc.)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic
        

        # Drawing 
        level.draw(screen)


        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()