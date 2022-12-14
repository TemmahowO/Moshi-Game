import pygame
from pygame.locals import *
from random import randint
import json

class Player:
    def __init__(self):
        self.player_x = randint(-500, 500)
        self.player_y = randint(-500, 500)
        self.player_speed = 0
        self.health = 100
        self.hunger = 50
      
    def health_system(self):
        self.hunger -= .1
        if self.hunger <= 0:
            self.hunger = 0
            self.health -= 1


class Object:
    def __init__(self):
        self.object_x = randint(0, 500)
        self.object_y = randint(100, 500)
        self.y_speed = 0
        self.x_speed = 0
        self.colour = (255, 255, 255)
        self.default_size = 10
        self.object_rect = Rect((self.object_x, self.object_y, self.default_size, self.default_size))

    def draw(self, window, size):
        self.draw_x = self.object_x
        self.draw_y = self.object_y
        self.object_rect = Rect((self.object_x, self.object_y, size, size))
        
        pygame.draw.rect(window, self.colour, self.object_rect)

    def is_visible(self):
        if self.player_x in range(self.object_x, self.object_y):
            self.draw(self.window)

    def surface_crossover(self):
      if self.object_x <= 0:
        self.object_x = 810
      elif self.object_x >= 800:
        self.object_x = -10
      
class Tree(Object):
    pass

# Defined here instead of main.py so I could get the movement controller and other stuff working without any stupid workarounds.
objects = Object()
player = Player()

# Takes care of player movement
def movement_controller():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        objects.x_speed = -5
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
         objects.x_speed = 5
    else:
        objects.x_speed = 0

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        objects.y_speed = 5
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        objects.y_speed = -5
    else: 
        objects.y_speed = 0

    return objects.x_speed, objects.y_speed
