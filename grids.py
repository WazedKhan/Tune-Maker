import pygame

def draw_grid(screen, color):
    WIDTH = 1400
    HEIGHT = 800
    leftMenu = pygame.draw.rect(screen, color, [0, 0, 200, HEIGHT-100], 1)
    butomMenu = pygame.draw.rect(screen, color, [0, HEIGHT-100, WIDTH, 100], 2)