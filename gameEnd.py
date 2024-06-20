import pygame
import entities
import checks

def game_end_check():

    if entities.player.lives <= 0:
        checks.show_title = True
        checks.once_counter = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False 
    return True
    # any future game ending actions should be added here (such as running out of lives)

