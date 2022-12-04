import pygame
from random import randint

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_height = 500
window_width = 500
clock = pygame.time.Clock()
fps = 25
player_y_pos = 250
player_x_pos = 250

food_y = 250
food_x = 250
food_x_speed = 0
food_y_speed = 0

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Moshi Game")

hunger = 50
health = 100



while True:
    # Bare bones stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()

    # Movement controller.
    # Did not use "if event.type == KEYDOWN" because it is broken
    if keys[pygame.K_UP]:
        food_y_speed = 5
    elif keys[pygame.K_DOWN]:
        food_y_speed = -5
    else:
        food_y_speed = 0

    if keys[pygame.K_RIGHT]:
        food_x_speed = -5
    elif keys[pygame.K_LEFT]:
        food_x_speed = 5
    else:
        food_x_speed = 0
    
    # Moving the objects
    food_x += food_x_speed
    food_y += food_y_speed

    # Collision checking
    # Figure out how this works. It is confusing the life out of me.
    if player_x_pos >= food_x and player_x_pos <= food_x + 30:
        if player_y_pos >= food_y and player_y_pos <= food_y + 30:
            print("collision detected") 

    #Debug stuff
    print("y: ", food_y)
    print("x: ", food_x)
    #print("food_x_speed: ", food_x_speed, "\nfood_y_speed: ", food_y_speed)

    # Rendering and updating stuff.
    window.fill(white)
    pygame.draw.rect(window, gray, [food_x, food_y, 20, 20]) # Food
    pygame.draw.rect(window, red, [player_x_pos - 10, player_y_pos - 10, 10, 10]) # Player
    pygame.display.update()
    clock.tick(fps)

quit()
