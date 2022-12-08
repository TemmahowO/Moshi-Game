import pygame

fonts = pygame.font.get_fonts()

font = pygame.font.SysFont(None, 55

def message_to_screen(msg, colour, pos_x, pos_y):
    screen_text = font.render(msg, True, colour)
    window.blit(screen_text, [pos_x, pos_y])
