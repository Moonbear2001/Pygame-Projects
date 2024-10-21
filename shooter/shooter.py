import pygame
from random import randint
from math import sqrt

# Events
TIMES_UP = pygame.USEREVENT
NEW_TARGET = pygame.USEREVENT + 1

# Constants
GAME_DURATION = 60000
TARGET_DURATION = 1000
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TARGET_SIZE = 25
SCOPE_SIZE = 24

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Font setup
pygame.font.init()
font = pygame.font.SysFont(None, 100)

# Game setup
score = 0
pygame.time.set_timer(TIMES_UP, GAME_DURATION)
# pygame.time.set_timer(NEW_TARGET, TARGET_DURATION)
target_coords = (100, 100)

# Cursor
cursor_surface = pygame.Surface((SCOPE_SIZE, SCOPE_SIZE))
cursor_surface.fill("black")
pygame.draw.ellipse(cursor_surface, "red", (0, 0, SCOPE_SIZE, SCOPE_SIZE), width=2)
pygame.draw.line(cursor_surface, "red", (0, SCOPE_SIZE // 2), (SCOPE_SIZE // 4, SCOPE_SIZE // 2))
pygame.draw.line(cursor_surface, "red", (SCOPE_SIZE * (3/4), SCOPE_SIZE // 2), (SCOPE_SIZE, SCOPE_SIZE // 2))
pygame.draw.line(cursor_surface, "red", (SCOPE_SIZE // 2, 0), (SCOPE_SIZE // 2, SCOPE_SIZE // 4))
pygame.draw.line(cursor_surface, "red", (SCOPE_SIZE // 2, SCOPE_SIZE * (3/4)), (SCOPE_SIZE // 2, SCOPE_SIZE))
cursor_surface.set_colorkey("black")
color_cursor = pygame.Cursor((SCOPE_SIZE // 2, SCOPE_SIZE // 2), cursor_surface)
pygame.mouse.set_cursor(color_cursor)


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Times up
        if event.type == TIMES_UP:
            running = False

        # New target
        # if event.type == NEW_TARGET:
            # target_coords = (randint(TARGET_SIZE, SCREEN_WIDTH - TARGET_SIZE), randint(TARGET_SIZE, SCREEN_HEIGHT - TARGET_SIZE))

        # Click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            distance = sqrt((mouse_pos[0] - target_coords[0]) ** 2 + (mouse_pos[1] - target_coords[1]) ** 2)
            if distance <= TARGET_SIZE:
                score += 1
                target_coords = (randint(TARGET_SIZE, SCREEN_WIDTH - TARGET_SIZE), randint(TARGET_SIZE, SCREEN_HEIGHT - TARGET_SIZE))


    # Draw score
    screen.fill("black")
    text = font.render(str(score), True, "white")
    text_rect = text.get_rect()
    screen.blit(text, text_rect)
    pygame.draw.circle(screen, "white", target_coords, TARGET_SIZE)

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()