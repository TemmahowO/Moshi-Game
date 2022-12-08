import pygame
from pygame.locals import *
from random import randint


class Player:
    def __init__(self):
        self.player_x = 0
        self.player_y = 0
        self.y_speed = 0
        self.x_speed = 0
        self.health = 100
        self.hunger = 50
    
    def health_system(self):
        self.hunger -= .1
        if self.hunger <= 0:
            self.hunger = 0
            self.health -= 1


class Object:
    def __init__(self):
        self.object_x = randint(-1000, 1000)
        self.object_y = randint(-1000, 1000)
        self.colour = (255, 255, 255)

    def draw(self, window):
        self.draw_x = self.object_x
        self.draw_y = self.object_y
        pygame.draw.rect(window, self.colour, self.draw_x, self.draw_y)

    def is_visible(self):
        if self.player_x in range(self.object_x, self.object_y):
            self.draw(self.window)


class Tree(Object):
    pass

player = Player()

def movement_controller():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x_speed = -5
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x_speed = 5
    else:
        player.x_speed = 0

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y_speed = 5
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y_speed = -5
    else: 
        player.y_speed = 0

    return player.x_speed, player.y_speed