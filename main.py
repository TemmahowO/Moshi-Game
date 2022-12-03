import pygame

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
gray = (169,169,169)
black = (0, 0, 0)

window_height = 500
window_width = 500
clock = pygame.time.Clock()
fps = 25
player_y = 250
player_x = 250
player_x_speed = 0
player_y_speed = 0

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

        # Player Movement Controller
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x_speed = 5
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x_speed = -5
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                player_y_speed = -5
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_y_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
                    player_x_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    player_y_speed = 0

    # Actually moving the player
    player_x += player_x_speed
    player_y += player_y_speed

   # Camera
    if player_y >= window_height - 120:
        player_y_speed = 0
        player_y = window_height - 120
        food_y_speed = 5
    # used real values instead of a sum because I can't be bothered to figure out
    # what I am supposed to take away from 500 to make 120
    elif player_y <= 120:
         player_y_speed = 0
         player_y = 120
         food_y_speed = -5

    if player_x >= window_width - 120:
        player_x_speed = 0
        player_x = window_width - 120
        food_x_speed = -5
    elif player_x <= 120:
        player_x_speed = 0
        player_x = 120

    # Moving the objects
    food_x += food_x_speed
    food_y += food_y_speed


    print("y: ", player_y)
    print("x: ", player_x)

    # Rendering and updating stuff.
    window.fill(white)
    food = pygame.draw.rect(window, gray, [food_x, food_y, 10, 10])
    player = pygame.draw.rect(window, red, [player_x - 10, player_y - 10, 10, 10])
    pygame.display.update()
    clock.tick(fps)
    print("cock")

quit()
