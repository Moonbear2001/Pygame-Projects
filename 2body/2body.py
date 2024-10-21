import pygame
import math

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
G = 6.67430e-11
TIME_STEP = 1000

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Body:
    def __init__(self, x, y, mass, vx=0, vy=0):
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.ax = 0.0
        self.ay = 0.0

    def update_pos(self):
        self.x += self.vx * TIME_STEP
        self.y += self.vy * TIME_STEP

    def update_vel(self):
        self.vx += self.ax * TIME_STEP
        self.vy += self.ay * TIME_STEP

    def calc_grav_force(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance == 0:
            return 0, 0
        
        force = G * self.mass * other.mass / distance ** 2

        fx = force * (dx / distance)
        fy = force * (dy / distance)

        return fx, fy
    
    def draw(self, surface, color):
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 10)
    
# Initialize 2 bodies
# body1 = Body(300, 300, 5e22, vx = 0, vy=100)
# body2 = Body(500, 300, 1e22, vx = 0, vy=-100)
body1 = Body(300, 300, 100, vx = 0, vy=1)
body2 = Body(400, 400, 10000, vx = 0, vy=-1)


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2 Body Problem")
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculation
    fx1, fy1 = body1.calc_grav_force(body2)
    fx2, fy2 = body2.calc_grav_force(body1)
    
    fx2, fy2 = -fx1, -fy1

    body1.ax = fx1 / body1.mass
    body1.ay = fy1 / body1.mass
    body2.ax = fx2 / body2.mass
    body2.ay = fy2 / body2.mass

    # Update velocities and positions
    body1.update_vel()
    body2.update_vel()
    body1.update_pos()
    body2.update_pos()

    print(body1.x, body1.y)

    # Render game
    screen.fill("black")
    body1.draw(screen, "red")
    body2.draw(screen, "red")
    pygame.draw.circle(screen, "red", (0, 0), 100)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()