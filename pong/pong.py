import pygame
from pygame.locals import * 
from sys import exit
from random import choice
from math import ceil

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Constants
FPS = 60
WIDTH = 1280
INTRO_SCREEN_SECONDS = 1
OUTRO_SCREEN_SECONDS = 1
HEIGHT = 720
PADDLE_OFFSET = 20
PADDLE_WIDTH = 18
PADDLE_HEIGHT = 110
PADDLE_COLOR = GRAY
BALL_COLOR = WHITE
LINE_COLOR = WHITE
BALL_SPEED = 6
BALL_SIZE = 26

# Functions
def print_msg(screen, msg, color, x, y, size, center=False):
    """
    Prints a message to the screen
    """
    font = pygame.font.SysFont('Arial Black', size)
    text = font.render(msg, True, color)
    if center:
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)
    else:
        screen.blit(text, (x,y))
    pygame.display.flip()

def move_paddles():
    """
    Logic for moving paddles each frame.
    """
    global paddle_left, paddle_right
    keys = pygame.key.get_pressed()
    if keys[K_UP] and paddle_right.top - 10 >= 0:
        paddle_right.y -= 10
    if keys[K_DOWN] and paddle_right.bottom + 10 <= HEIGHT:
        paddle_right.y += 10
    if keys[K_w] and paddle_left.top - 10 >= 0:
        paddle_left.y -= 10
    if keys[K_s] and paddle_left.bottom + 10 <= HEIGHT:
        paddle_left.y += 10

def move_ball():
    """
    Logic for moving ball each frame.
    Return values:
    0 = no score
    1 = left paddle scored (out of bounds on right side)
    2 = right paddle scored (out of bounds on left side)
    """
    global ball, ball_x_vel, ball_y_vel, paddle_left, paddle_right
    res = 0

    ball.x += ball_x_vel
    ball.y += ball_y_vel  

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_y_vel *= -1
    if ball.left <= 0:
        ball_x_vel *= -1
        res = 2
    elif ball.right >= WIDTH:
        ball_x_vel *= -1
        res = 1
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_x_vel *= -1

    return res

def show_msg_screen(message, duration):
    """
    Display intro or outro message.
    """
    pygame.time.set_timer(pygame.USEREVENT, duration * 1000)
    print_msg(SCREEN, message, WHITE, 0, HEIGHT/2, 100, True)
    run = True
    while run:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT or keys[K_ESCAPE]:
                pygame.quit()
                exit()
            if event.type == USEREVENT:
                run = False
    SCREEN.fill(BLACK)

# Initialization
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(BLACK)
fps_clock = pygame.time.Clock()

# Music
# pygame.mixer.init()
# pygame.mixer.music.load("background_music.mp3")
# pygame.mixer.music.set_volume(0)
# pygame.mixer.music.play(-1)

# Intro screen
show_msg_screen("Welcome to Pong", INTRO_SCREEN_SECONDS)

# Paddles + ball
ball_y_vel = BALL_SPEED
ball_x_vel = BALL_SPEED
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
paddle_left = pygame.Rect(PADDLE_OFFSET, HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_right = pygame.Rect(WIDTH - 2 * PADDLE_OFFSET, HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()

    move_paddles()

    if move_ball() != 0: break

    SCREEN.fill(BLACK)
    pygame.draw.line(SCREEN, LINE_COLOR, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 3)
    pygame.draw.ellipse(SCREEN, BALL_COLOR, ball)
    pygame.draw.rect(SCREEN, PADDLE_COLOR, paddle_left)
    pygame.draw.rect(SCREEN, PADDLE_COLOR, paddle_right)

    pygame.display.flip()
    fps_clock.tick(FPS)

# Show outro screen
show_msg_screen("Game Over", OUTRO_SCREEN_SECONDS)

pygame.quit()