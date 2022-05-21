# Making a drum machine using pygame

import pygame
from pygame import mixer # for sound effects

from grids import draw_grid

pygame.init()
# initialize all imported pygame modules

WIDTH = 1400
HEIGHT = 800
# Screen size of the machine

black = ( 0, 0, 0 )
white = ( 255, 255, 255 )
sidemenu = ( 204, 255, 255 )
# set colors for screen

screen = pygame.display.set_mode([WIDTH, HEIGHT])
# Initialize a window or screen of (1400x800) for display
pygame.display.set_caption('Py Drum')
# sets caption of the window

fps = 60
clock = pygame.time.Clock()

# Main Game Loop
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    draw_grid(screen, sidemenu)

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()
    # It allows only a portion of the screen to updated, instead of the entire area.
    # if no argument is passed it updates the entire Surface area like pygame.
pygame.quit()
