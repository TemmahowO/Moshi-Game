import pygame
from random import randint

pygame.init()


white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_width = 500
window_height = 500

object_y = 0
object_x = 0
player_x = 0
player_y = 0

Game_on = True

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.draw.rect(window, red [x, y, 10, 10])

while Game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_on = False
    p1 = Player(120, 120)

pygame.quit()
quit()