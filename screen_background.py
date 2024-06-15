# In this file we can have all things that relate to the screen such as text or deciding what shows up on screen

import pygame



pygame.init()
run = True
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_color = (0, 0, 0)



def game_end_check():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    return run
    # any future game ending actions should be added here (such as running out of lives)
        

    