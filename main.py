import pygame
from pygame.locals import *
from Classes_Functions import * 

white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_width = 800
window_height = 700
fps = 30
clock = pygame.time.Clock()
rand_x = 100
rand_y = 400

object_y = 240
object_x = 240
player_x_pos = 250
player_y_pos = 250

player_width = 10
player_hight = 10
object_width = 10
object_hight = 10

Game_on = True

pygame.init()

fonts = pygame.font.get_fonts()

def message_to_screen(msg, colour, pos_x, pos_y):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, colour)
    window.blit(screen_text, [pos_x, pos_y])

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")


while Game_on == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_on = False
    
    player_rect = Rect((player_x_pos, player_y_pos, player_width, player_hight))
    collide_true = pygame.Rect.colliderect(player_rect, objects.object_rect)

    movement_controller()
    write_to_json()
    objects.surface_crossover()
    

    #Changing Objects and Players x and y coords.
    objects.object_x += objects.x_speed
    objects.object_y += objects.y_speed
    player.player_x += objects.x_speed
    player.player_y += objects.y_speed
    print(f"object_x: {objects.object_x}\n object_y: {objects.object_y}")

    # Collision checking. Everything else was too complicated.
    if collide_true == True:
        rand_x2 = randint(rand_x, rand_y)
        rand_y2 = randint(rand_x, rand_y)
        objects.object_y = rand_y2
        objects.object_x = rand_x2

    window.fill(gray)
    objects.draw(window, 20)
    pygame.draw.rect(window, red, player_rect)
    message_to_screen(f"player_x: {player.player_x}", red, 0, 0)
    message_to_screen(f"player_y: {player.player_y}", red, 0, 20)
    clock.tick(fps)
    pygame.display.update()


pygame.quit()
quit()