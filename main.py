# indev - V0.01

import pygame
from pygame.locals import *
import sys
from Classes import * 
import Functions

def main():
    pygame.init()

    white = [255, 255, 255]
    red = [255, 0, 0]
    gray = [169,169,169]
    black = [0, 0, 0]
    green = [0, 255, 0]

    window_width = 800
    window_height = 700
    fps = 60
    clock = pygame.time.Clock()
    Game_on = True
    is_eating = False
    is_dead = False
    draw_food = False
    raw_food_count = 0
    game_over = False

    player = Player(10, False)
    tree = Object(5, 0, 20)
    food = Object(1, 11, 10)


    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Moshi Game")

    while Game_on == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_on = False
                
            if event.type == pygame.KEYDOWN:
                if raw_food_count <= 0:
                    pass
                elif event.key == K_e or event.key == K_q:
                    player.hunger += food.saturation
                    raw_food_count -= 1


            if pygame.mouse.get_pressed() == (1, 0, 0) and Rect.colliderect(player.hitbox_rect, tree.rect):
                red[0] -= 5
                tree.durability -= 0.5
                if tree.durability <= 0:
                    food.x_pos = tree.x_pos + tree.size /2
                    food.y_pos = tree.y_pos + tree.size /2
                    draw_food = True
                    tree.randomize_coords(window, red, 20) # Arguments are there because the draw method is called within the randomize_coords method.
                    tree.durability = 10
                    red[0] = 255
                # Prevents an exception.
                if red[0] <= 0:
                    red[0] = 255
  
            if is_dead:
                game_over = True
                while game_over:
                    window.fill(gray)
                    Functions.message_to_screen(window, "You have died! Press enter to start again and esc to exit!", white, window_width/2 - 100, window_height/2)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            game_over = False
                            Game_on = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            Game_on = False
                            game_over = False
                        elif event.key == K_RETURN:
                            main()
                    pygame.display.update()

        # Collision detection
        if Rect.colliderect(player.rect, food.rect):
            draw_food = False
            raw_food_count += 1
            food.x_pos = 99999
            food.draw(window, green, 5) # Updates the rectangles position

        # Functions.keybinds(player, food.saturation, raw_food_count)
        window.fill(gray)
        player.draw_hitbox(window, gray, 10) # hitbox
        player.draw(window, black, 10) # player
        tree.draw(window, red, 20)
        if draw_food == True:
            food.draw(window, green, 5)
        # Drawing text
        player.health_system(is_eating, is_dead)
        is_dead = player.is_dead
        Functions.message_to_screen(window, f"Food: {raw_food_count}", white, 700, 20)
        Functions.message_to_screen(window, f"Health: {player.health}", white, 0, 20)
        Functions.message_to_screen(window, f"Hunger: {player.hunger}", white, 0, 40)
        # Collision check for the player
        Functions.movement_controller_and_collision_check(player, player.rect, tree.rect) # Called here so it can use the returned rect value
        clock.tick(fps)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()