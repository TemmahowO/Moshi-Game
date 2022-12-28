import pygame
from pygame.locals import *
import sys
from Classes import * 
import Functions

def main():
    pygame.init()

    white = (255, 255, 255)
    red = (255, 0, 0)
    gray = (169,169,169)
    black = (0, 0, 0)

    window_width = 800
    window_height = 700
    fps = 60
    clock = pygame.time.Clock()
    Game_on = True

    player = Player(10)
    objects = Object(5, 10)

    window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("Moshi Game")

    while Game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_on = False

        print(f"Player X: {player.x_pos}, Player Y: {player.y_pos}")
        window.fill(gray)
        player.draw_hitbox(window, white, 10) # hitbox
        player.draw(window, black, 10) # player
        objects.draw(window, red, 20)
        Functions.movement_controller_and_collision_check(player, player.rect, objects.rect) # Called here so it can use the retunred rect values
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()