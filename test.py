# Python 3.4.3 with Pygame
from sys import exit
import pygame
pygame.init()

WIDTH = HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crash!')

# Draw Once
rectangle = pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 100))
pygame.display.update()

# Main Loop
while True:
    # Mouse position and button clicking
    pos = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]

 
    if pygame.mouse.get_pressed()[0] and mysprite.rect.collidepoint(pygame.mouse.get_pos()) and not handled:
        print ("You have opened a chest!")
        handled = pygame.mouse.get_pressed()[0]

    # Quit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
