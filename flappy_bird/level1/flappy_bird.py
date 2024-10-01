import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = -8
PIPE_WIDTH = 70
PIPE_GAP = 150  # Space between pipes
GROUND_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
GREEN = (0, 255, 0)

# Load assets
BIRD_WIDTH, BIRD_HEIGHT = 40, 30
BIRD_IMAGE = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
BIRD_IMAGE.fill((255, 255, 0))  # Yellow bird

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Clock to control frame rate
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.SysFont(None, 36)

# Bird properties
bird_x = 100
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)

# Pipes list
pipe_x = [SCREEN_WIDTH, SCREEN_WIDTH + 200]
pipe_height = [random.randint(100, SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT) for _ in range(2)]

# Update bird position and apply gravity
def update_bird():
    global bird_y, bird_velocity
    bird_velocity += GRAVITY
    bird_y += bird_velocity
    bird_rect.y = bird_y

    # Prevent bird from going above the screen
    if bird_rect.top < 0:
        bird_rect.top = 0
        bird_velocity = 0

# Handle bird jump
def bird_jump():
    global bird_velocity
    bird_velocity = BIRD_JUMP

# Update pipes positions
def update_pipes():
    for i in range(len(pipe_x)):
        pipe_x[i] -= 3

# Check if any pipes have moved off screen and add new pipes
def handle_pipes():
    for i in range(len(pipe_x)):
        if pipe_x[i] < 0:
            pipe_x[i] = SCREEN_WIDTH
            pipe_height[i] = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT)

# Draw bird
def draw_bird():
    screen.blit(BIRD_IMAGE, bird_rect)

# Draw pipes
def draw_pipes():
    for i in range(len(pipe_x)):
        top_rect = pygame.Rect(pipe_x[i], 0, PIPE_WIDTH, pipe_height[i])
        bottom_rect = pygame.Rect(pipe_x[i], pipe_height[i] + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height[i] - PIPE_GAP)
        pygame.draw.rect(screen, GREEN, top_rect)
        pygame.draw.rect(screen, GREEN, bottom_rect)

# Check for bird collisions with pipes or ground
def check_collision():
    for i in range(len(pipe_x)):
        top_rect = pygame.Rect(pipe_x[i], 0, PIPE_WIDTH, pipe_height[i])
        bottom_rect = pygame.Rect(pipe_x[i], pipe_height[i] + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height[i] - PIPE_GAP)
        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            return True
    if bird_rect.bottom >= SCREEN_HEIGHT - GROUND_HEIGHT:
        return True
    return False

# Main game loop
def main():
    score = 0
    running = True

    while running:
        screen.fill(SKY_BLUE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_jump()

        # Update game objects
        update_bird()
        update_pipes()
        handle_pipes()

        # Check for collisions
        if check_collision():
            running = False

        # Draw everything
        draw_bird()
        draw_pipes()

        # Draw the ground
        pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
