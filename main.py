import pygame
from pygame.locals import *
from Player import * 


white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_width = 500
window_height = 500

fps = 30
clock = pygame.time.Clock()

object_y = 240
object_x = 240
player_x = 250
player_y = 250

player_width = 10
player_hight = 10
object_width = 10
object_hight = 10

# Todo - Get this into the player class

Game_on = True

pygame.init()

# Variables

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")


while Game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_on = False
    
    object_rect = Rect((object_x, object_y, object_width, object_hight))
    player_rect = Rect((player_x, player_y, player_width, player_hight))
    collide_true = pygame.Rect.colliderect(player_rect, object_rect)

    #used object_x/y instead of player_x/y because the player does not move instead, everything else does.
    movement_controller()
    object_x += player.x_speed
    object_y += player.y_speed

    #Nevermind
    if collide_true == True:
        change_object_placement(200, 400)
        print(collide_true)

    window.fill(gray)
    pygame.draw.rect(window, white, object_rect) # Object
    pygame.draw.rect(window, red, player_rect) # Player
    clock.tick(fps)
    pygame.display.update()
    

pygame.quit()
quit()