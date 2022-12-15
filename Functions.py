import pygame
from pygame.locals import *
from random import randint
import json
from Classes import *

# Defined here instead of main.py so I could get the movement controller and other stuff working without any stupid workarounds.
objects = Object()
player = Player()


def message_to_screen(window, msg, colour, pos_x, pos_y):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, colour)
    window.blit(screen_text, [pos_x, pos_y])

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

# This is responsible for saving objects coordinates so that when the player comes back after the
# object went of screen and the surface crossover function is called (see the last function in the object class)
# the object is re-rendered onto the screen in the same place.
def write_to_json():
    with open("coords.json", "a") as json_write:
        coords = [
                {
                "player": {
                    "player_x": player.player_x,
                    "player_y": player.player_y
                },
                "object": {
                    "object_x": objects.object_x,
                    "object_y": objects.object_y
                }
            }
        ]

        if objects.object_x <= -10:
            json.dump(coords, json_write, indent=4)
        elif objects.object_x >= 810:      
            json.dump(coords, json_write, indent=4)

        if objects.object_y <= -10:
            json.dump(coords, json_write, indent=4)
        elif objects.object_y >= 710:
            json.dump(coords, json_write, indent=4)


def render_from_json():
    with open("coords.json", "r") as json_read:
        loaded_coords = json.load(json_read)
    print(loaded_coords)