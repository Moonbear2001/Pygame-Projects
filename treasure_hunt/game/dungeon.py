import pygame
import json
from pathlib import Path

from .room import Room
from constants import DUNGEON_FOLDER
from sprites import Treasure

class Dungeon:

    def __init__(self, screen, dungeon_dict=None, dungeon_name=None):
        self.screen = screen
        self.rooms = {}

        # Future option to just pass a dictionary, could allow for procedural generation
        self.dungeon_dict = dungeon_dict if dungeon_dict else self.load_from_json(dungeon_name)
        self.setup_rooms()

        self.treasure = Treasure(screen)
        self.treasure_found = False

    def load_from_json(self, dungeon_name):
        """
        Load a dungeon from a json file.
        """
        dungeon_path = Path(DUNGEON_FOLDER) / f"{dungeon_name}.json"

        with open(dungeon_path, 'r') as file:
            json_data = json.load(file)

        return json_data
    
    def setup_rooms(self):
        """
        Use the dungeon dict to setup the rooms.
        """

        for room_id, room_data in self.dungeon_dict["rooms"].items():
            self.add_room(room_id, room_data['name'])

        # Set starting room
        self.current_room = self.rooms[self.dungeon_dict['starting_room']]
        self.current_room.enter()

        for room_id, room_data in self.dungeon_dict['rooms'].items():
            for direction, connected_room_id in room_data['connections'].items():
                if connected_room_id:
                    self.connect_rooms(room_id, connected_room_id, direction)

        # Put treasure in a room
        self.rooms[self.dungeon_dict["treasure_room"]].has_treasure = True

    def add_room(self, name, room_name):
        new_room = Room(self.screen, room_name)
        self.rooms[name] = new_room
        return new_room

    def connect_rooms(self, room1_name, room2_name, direction):
        room1 = self.rooms[room1_name]
        room2 = self.rooms[room2_name]
        room1.connect(direction, room2)

    
    def update(self, protagonist):

        # Detect protag hitting doors and reposition as required
        collided_doors = pygame.sprite.spritecollide(protagonist, self.current_room.doors, False)
        if collided_doors:
            direction = collided_doors[0].direction
            self.current_room = self.current_room.connections[direction]
            self.current_room.enter()
            protagonist.position_after_exit(direction)

        # Detect hitting treasure and end game if found
        if self.current_room.has_treasure:
            collided_treasure = pygame.sprite.collide_circle(protagonist, self.treasure)
            if collided_treasure:
                self.treasure_found = True

    def draw(self):
        self.current_room.draw()
        if self.current_room.has_treasure:
            self.treasure.draw()