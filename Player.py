import pygame
from pygame.locals import *
from random import randint

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.y_speed = 0
        self.x_speed = 0
        self.health = 100
        self.hunger = 50
    
    def health_system(self):
        self.hunger -= .1
        if self.hunger <= 0:
            hunger = 0
            health -= 1

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

def change_object_placement(rand_x, rand_y):
    global object_x
    global object_y
    rand_x = randint(rand_x, rand_y)
    rand_y = randint(rand_x, rand_y)
    object_y = rand_y
    object_x = rand_x
    return rand_x, rand_y