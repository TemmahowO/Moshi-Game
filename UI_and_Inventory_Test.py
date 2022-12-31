import pygame
import sys
from pygame.locals import Rect
import time


def main():
    handled = False
    white = [255, 255, 255]
    green = [0, 255, 0]
    window_width = 400
    window_height = 400
    window = pygame.display.set_mode((window_height, window_width))
    pygame.display.set_caption("UI&Inventory Test")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
        handled_2 = pygame.mouse.get_pressed()[0]
        square_rect = Rect(100, 100, 20, 20)
        window.fill(white)
        pygame.draw.rect(window, green, square_rect)
        if pygame.mouse.get_pressed()[0] and square_rect.collidepoint(pygame.mouse.get_pos()) and handled == False:
            print("You have opened a chest!")
            handled = pygame.mouse.get_pressed()[0]
            time.sleep(10)
        print(handled)
        pygame.display.update()
        


if __name__ == "__main__":
    pygame.init()
    main()
    
    