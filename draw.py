import pygame
import entities
import screen_background as SB
import auras
import checks


def draw(run_time):
    for enemy in entities.enemies:
        entities.enemy_sprite = pygame.transform.scale(entities.enemy_sprite, (enemy.character.width, enemy.character.height))
        SB.screen.blit(entities.enemy_sprite, enemy.character)

    entities.player_sprite = pygame.transform.scale(entities.player_sprite, (entities.player.character.width, entities.player.character.height))
    SB.screen.blit(entities.player_sprite, entities.player.character)
    

    for projectile in entities.projectiles:
        pygame.draw.rect(SB.screen, (0, 0, 255), projectile.character)


    for projectile in entities.player_projectiles:
        pygame.draw.rect(SB.screen, (auras.selected.colorX, auras.selected.colorY, auras.selected.colorZ), projectile.character)