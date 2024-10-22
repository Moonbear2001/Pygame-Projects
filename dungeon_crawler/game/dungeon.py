import json
from pathlib import Path

from .room import Room

class Dungeon:
    def __init__(self, screen, dungeon_folder):
        self.screen = screen
        self.dungeon_folder = Path(dungeon_folder)
        self.rooms = {}

    def add_room(self, name, room_name):
        new_room = Room(self.screen, room_name)
        self.rooms[name] = new_room
        return new_room

    def connect_rooms(self, room1_name, room2_name, direction):
        room1 = self.rooms[room1_name]
        room2 = self.rooms[room2_name]
        room1.connect(direction, room2)

    def load_from_json(self, dungeon_name):
        dungeon_path = self.dungeon_folder / f"{dungeon_name}.json"

        with open(dungeon_path, 'r') as file:
            json_data = json.load(file)

        rooms = json_data['rooms'].items()
        self.current_room = rooms[0]
    
        for room_id, room_data in rooms:
            self.add_room(room_id, room_data['name'])

        for room_id, room_data in json_data['rooms'].items():
            for direction, connected_room_id in room_data['connections'].items():
                if connected_room_id:
                    self.connect_rooms(room_id, connected_room_id, direction)

    def draw(self):
        self.current_room.draw()
