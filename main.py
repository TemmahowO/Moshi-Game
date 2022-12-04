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
        player.x_speed = 5
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x_speed = -5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y_speed = 5
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y_speed = -5
    else:
        player.x_speed = 0
        player.y_speed = 0

    return player.x_speed, player.y_speed

pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_width = 500
window_height = 500

fps = 30
clock = pygame.time.Clock()

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

    movement_controller()
    player_x += player.x_speed
    player_y += player.y_speed

    window.fill(gray)
    pygame.draw.rect(window, red, [player_x, player_y, 10, 10])
    pygame.display.update()
    clock.time(fps)
pygame.quit()
quit()