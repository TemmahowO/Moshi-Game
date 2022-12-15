import pygame
from pygame.locals import *
from random import randint

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

    # For the camera
    def surface_crossover(self):
        if self.object_x <= -10:
            self.object_x = 810
            self.object_y = randint(0, 700)

        elif self.object_x >= 810:
            self.object_x = -10
            self.object_y = randint(0, 700)
            
        if self.object_y <= -10:
            self.object_y = 710
            self.object_x = randint(0, 800)
        elif self.object_y >= 710:
            self.object_y = -10
            self.object_x = randint(0, 800)

class Tree(Object):
    pass

