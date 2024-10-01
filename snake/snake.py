import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 10  # Snake speed (frames per second)

# Snake's starting position and body
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)  # Start moving right
snake_length = 1

# Food (starts at a random position)
food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Draw grid for debugging (optional)
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

# Draw snake
def draw_snake():
    for segment in snake:
        rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, GREEN, rect)

# Draw food
def draw_food():
    rect = pygame.Rect(food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, RED, rect)

# Update the snake's position
def update_snake():
    global snake_length, food_position, score

    # Get the current head position
    head_x, head_y = snake[0]

    # Calculate the new head position
    new_head = (head_x + snake_direction[0], head_y + snake_direction[1])

    # Check if snake eats food
    if new_head == food_position:
        snake_length += 1
        score += 1
        food_position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    
    # Add new head to the snake
    snake.insert(0, new_head)

    # Keep the snake at its current length
    if len(snake) > snake_length:
        snake.pop()

# Check for collisions with walls or itself
def check_collisions():
    head_x, head_y = snake[0]

    # Check if snake hits the wall
    if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
        return True

    # Check if snake hits itself
    if len(snake) > 1 and (head_x, head_y) in snake[1:]:
        return True

    return False

# Main game loop
def main():
    global snake_direction

    running = True
    while running:
        screen.fill(BLACK)

        # Event handling (key presses)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Update snake position
        update_snake()

        # Check for collisions
        if check_collisions():
            running = False

        # Draw everything
        draw_snake()
        draw_food()
        # Uncomment the line below to display the grid (optional)
        # draw_grid()

        # Display the score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
