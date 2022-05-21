import pygame

def draw_grid(screen, color):
    WIDTH = 1400
    HEIGHT = 800

    black = ( 0, 0, 0 )
    white = ( 255, 255, 255 )
    gray = ( 204, 255, 255 )

    label_font = pygame.font.Font('ZakirahsHand.ttf', 32)

    leftMenu = pygame.draw.rect(screen, color, [0, 0, 200, HEIGHT-100], 1)
    butomMenu = pygame.draw.rect(screen, color, [0, HEIGHT-100, WIDTH, 100])
    boxes = []
    colors = [gray, white, gray]

    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))

    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))

    kick_text = label_font.render('Kick', True, white)
    screen.blit(kick_text, (30, 230))

    base_drum = label_font.render('Base Drum', True, white)
    screen.blit(base_drum, (30, 330))

    crash = label_font.render('Crash', True, white)
    screen.blit(crash, (30, 430))

    clap = label_font.render('Clap', True, white)
    screen.blit(clap, (30, 530))

    floor_tom = label_font.render('Floor Tom', True, white)
    screen.blit(floor_tom, (30, 630))

    for i in range(6):
        pygame.draw.line(screen, gray, (0, (i*100)+100), (200, (i*100)+100),5)
