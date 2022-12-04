import pygame
from random import randint
from player import *


pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_width = 500
window_height = 500

object_y = 0
object_x = 0
player_x = 120
player_y = 120

Game_on = True

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")


while Game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_on = False
    player = Player()
    movement_controller(player_y, player_x)
    window.fill(gray)
    pygame.draw.rect(window, red, [player_x, player_y, 10, 10])
    pygame.display.update()

pygame.quit()
quit()