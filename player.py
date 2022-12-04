import pygame

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.health = 100
        self.hunger = 50
    
    def health_system(self):
        self.hunger -= .1
        if self.hunger <= 0:
            hunger = 0
            health -= 1

player = Player()

def movement_controller(player_y, player_x):
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT] or keys[K_d]:
        player.speed = 5
    elif keys[K_LEFT] or keys[K_a]:
        player.speed = -5
    if keys[K_UP] or keys[K_w]:
        player.speed = 5
    elif keys[K_DOWN] or keys[K_s]:
        player.speed = -5
    
    player_x += player.speed
    player_y += player.speed