import pygame
import entities
import screen_background as SB

import checks


def draw(run_time):
    
    for enemy in entities.enemies:
        pygame.draw.rect(SB.screen, (255, 0, 0), enemy.character)

    pygame.draw.rect(SB.screen, (0, 255, 0), entities.player.character) 
    
    for projectile in entities.projectiles:
        pygame.draw.rect(SB.screen, (0, 0, 255), projectile.character)