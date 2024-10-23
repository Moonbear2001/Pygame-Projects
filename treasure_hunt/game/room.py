import pygame
from sprites.door import Door

class Room:

    opposite_directions = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east"
        }

    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.connections = {"north": None, "south": None, "east": None, "west": None}
        self.doors = pygame.sprite.Group()
        self.visited = False
        self.has_treasure = False

    def connect(self, direction, other_room):
        
        if direction in self.connections:
            self.connections[direction] = other_room
            other_room.connections[self.opposite_directions[direction]] = self
            self.doors.add(Door(direction))

    def draw(self):
        self.screen.fill("black")
        self.doors.draw(self.screen)

    def enter(self):
        self.visited = True

