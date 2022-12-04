import pygame
from random import randint

# Classes and functions

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


def collision_check():
    # if player_x > object_x and player_x < object_x + object_width or player_x + player_width > object_x and player_x + player_width < object_y + object_width:
    #     print("x collision")
    #     if player_y > object_y and player_y < object_y + object_hight or player_y + player_hight > object_y and player_y + player_hight < object_y:
    #         print("x and y")

     if player_x >= object_x and player_x <= object_x + 20:
        if player_y >= object_y and player_y <= object_y + 20:
            print("Balls")

pygame.init()

# Variables

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

Game_on = True

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")


while Game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_on = False

    #used object_x/y instead of player_x/y because the player does not move but, everything else does.
    movement_controller()
    object_x += player.x_speed
    object_y += player.y_speed

    collision_check()

    window.fill(gray)
    pygame.draw.rect(window, white, [object_x, object_y, object_width, object_hight]) # Object
    pygame.draw.rect(window, red, [player_x, player_y, player_width, player_hight]) # Player
    clock.tick(fps)
    pygame.display.update()
    

pygame.quit()
quit()