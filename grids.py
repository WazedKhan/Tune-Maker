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

    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))

    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))

