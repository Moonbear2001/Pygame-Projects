import json
import pygame

from constants import *

class Level:

  def __init__(self, level_file):
    self.level_info = self.load_level(level_file)
    self.layers = self.level_info["layers"]
    self.colors = {1: "black", 2: "white"}
    for layer in self.layers:
      print(layer)
      

  def load_level(self, level_file):
    """
    Load level info from a file.
    """
    with open(level_file, "r") as file:
      return json.load(file)
    
  def draw(self, screen):
    """
    Draw each layer of the leve.
    """
    for layer in self.layers:
      for row_num in range(SCREEN_HEIGHT // TILE_SIZE):
        for col_num in range(SCREEN_WIDTH // TILE_SIZE):
          pygame.draw.rect(screen, self.colors[layer["data"][row_num][col_num]], pygame.Rect(row_num * TILE_SIZE, col_num * TILE_SIZE, TILE_SIZE, TILE_SIZE))