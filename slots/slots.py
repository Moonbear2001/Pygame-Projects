import pygame
import random
from pygame.locals import *

# Calculate payout based on bet and slots
def payout(bet, s1, s2, s3):
    if s1 == s2 == s3:
        return 5 * bet
    elif s1 == s2 or s1 == s3 or s2 == s3:
        return 2 * bet
    else:
        return 0

# Constants
FPS = 60
S_WIDTH = 1280
S_HEIGHT = 720

SPRITE_SIZE = 400
SPRITE_SHEET_PATH = "assets/fruits_spritesheet.jpg"
SPRITESHEET_PX_W = 7975
SPRITESHEET_PX_H = 2257
SPRITESHEET_ROWS = 1
SPRITESHEET_COLS = 5
SPRITE_W = SPRITESHEET_PX_W / SPRITESHEET_COLS
SPRITE_H = SPRITESHEET_PX_H / SPRITESHEET_ROWS

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
clock = pygame.time.Clock()
running = True

# Upload sprite sheet
sprites = []
sprite_sheet = pygame.image.load(SPRITE_SHEET_PATH).convert_alpha()
for row in range(SPRITESHEET_ROWS):
    for col in range(SPRITESHEET_COLS):
        x = col * SPRITE_W
        y = row * SPRITE_H
        sprite = pygame.Surface((SPRITE_W, SPRITE_H), pygame.SRCALPHA)
        sprite.blit(sprite_sheet, (0, 0), (x, y, SPRITE_W, SPRITE_H))
        sprite = pygame.transform.scale_by(sprite, 0.1)
        sprites.append(sprite)

# Lets go gambling!
slot1 = random.randint(0, 4)
slot2 = random.randint(0, 4)
slot3 = random.randint(0, 4)
bank = 100
bet = 10
bank -= bet
payout = payout(bet, slot1, slot2, slot3)
print("Payout: ", payout)
bank += payout

# Main game loop
while running:
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("gamble")

    # Drawing
    screen.blit(sprites[slot1], (50, 50))
    screen.blit(sprites[slot2], (250, 50))
    screen.blit(sprites[slot3], (450, 50))


    pygame.display.flip()
    clock.tick(FPS)  

pygame.quit()

