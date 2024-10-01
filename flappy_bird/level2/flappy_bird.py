import pygame
import random
import sys

# Initialize Pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
BIRD_JUMP = -8
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
PIPE_GAP = 150 
GROUND_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)
GREEN = (0, 255, 0)

# Load assets
BIRD_WIDTH, BIRD_HEIGHT = 40, 30
BIRD_IMAGE = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
BIRD_IMAGE.fill((255, 255, 0))

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Clock to control frame rate
clock = pygame.time.Clock()

# Font for score display
font = pygame.font.SysFont(None, 36)


class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

    def update(self):
        # Apply gravity
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y

        # Prevent bird from going off the screen
        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0

    def jump(self):
        self.velocity = BIRD_JUMP

    def draw(self, screen):
        screen.blit(BIRD_IMAGE, self.rect)


class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - GROUND_HEIGHT)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT)

    def update(self):
        self.x -= 3
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def off_screen(self):
        return self.x + PIPE_WIDTH < 0


def main():
    # Initialize variables
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 200) for i in range(2)]
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
                    bird.jump()

        # Update game objects
        bird.update()

        # Update pipes and check for off-screen pipes
        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe(SCREEN_WIDTH))
                score += 1  # Add score when a pipe goes off screen

        # Check for collisions with pipes or ground
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                running = False
        if bird.rect.bottom > SCREEN_HEIGHT - GROUND_HEIGHT:
            running = False

        # Draw everything
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        # Draw the ground
        pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
