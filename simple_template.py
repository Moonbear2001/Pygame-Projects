import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
BACKGROUND_COLOR = (0, 0, 0) 

# Set up the screen (window)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Project")

clock = pygame.time.Clock()

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
        screen.fill(BACKGROUND_COLOR) 

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Run the game
if __name__ == "__main__":
    main()