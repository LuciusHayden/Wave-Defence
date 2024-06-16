import pygame
import entities
import screen_background as SB
import checks

#if your seeing all this, ignore it, its just copy and pasted and ill make it work later
def damage_check():
    if not checks.damage_cd and not checks.life_cd:
        for enemy in entities.enemies:
            if entities.player.character.colliderect(enemy.character):
                entities.player.health -= enemy.damage
                checks.damage_cd = True
                print(checks.damage_cd)
                cd_start = pygame.time.get_ticks()
        """for projectile in projectiles:
            if player.character.colliderect(projectile.character):
                player.health -= projectile.damage
                projectiles.remove(projectile)
                damage_cd = True
                cd_start = pygame.time.get_ticks() """
        if entities.player.character.x > SB.screen_width or entities.player.character.x < 0 or entities.player.character.y > SB.screen_height or entities.player.character.y < 0:
            entities.player.health -= 1
            checks.damage_cd = True
            cd_start = pygame.time.get_ticks()
        if checks.damage_cd:
            if pygame.time.get_ticks() - cd_start > 200:
                checks.damage_cd = False
   