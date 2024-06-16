import pygame


def game_end_check():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False 
    return True
    # any future game ending actions should be added here (such as running out of lives)

