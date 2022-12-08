import pygame
from pygame.locals import *
from Player import * 
import time


white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_width = 500
window_height = 500
fps = 30
clock = pygame.time.Clock()
rand_x = 100
rand_y = 400

object_y = 240
object_x = 240
player_x_pos = 250
player_y_pos = 250

player_x = 0
player_y = 0

player_width = 10
player_hight = 10
object_width = 10
object_hight = 10

score = 0

Game_on = True

pygame.init()

fonts = pygame.font.get_fonts()

def message_to_screen(msg, colour, pos_x, pos_y):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, colour)
    window.blit(screen_text, [pos_x, pos_y])

# Variables

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")


while Game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_on = False
    
    # Todo - Get this into the player class
    object_rect = Rect((object_x, object_y, object_width, object_hight))
    player_rect = Rect((player_x_pos, player_y_pos, player_width, player_hight))
    collide_true = pygame.Rect.colliderect(player_rect, object_rect)

    #I also add player_x and y to player.speed to keep track of where the player is in the game, as the player rect does not move.
    movement_controller()
    object_x += player.x_speed
    object_y += player.y_speed
    player_x += player.y_speed
    player_y += player.y_speed

    #Nevermind
    if collide_true == True:
        rand_x2 = randint(rand_x, rand_y)
        rand_y2 = randint(rand_x, rand_y)
        object_y = rand_y2
        object_x = rand_x2
        score += 1

    window.fill(gray)
    message_to_screen(f"Score: {score}", red, 100, 350)
    pygame.draw.rect(window, white, object_rect) # Object
    pygame.draw.rect(window, red, player_rect) # Player
    clock.tick(fps)
    pygame.display.update()


pygame.quit()
quit()