import pygame
import entities
import screen_background as SB
import checks
import difficulty

global cd_start

#if your seeing all this, ignore it, its just copy and pasted and ill make it work later
def damage_check():
    global cd_start
    if not checks.damage_cd and not checks.life_cd:
        for enemy in entities.enemies:
            if entities.player.character.colliderect(enemy.character):
                entities.player.health -= enemy.damage
                checks.damage_cd = True
                
                cd_start = pygame.time.get_ticks()
        for projectile in entities.projectiles:
            if entities.player.character.colliderect(projectile.character):
                entities.player.health -= projectile.damage
                entities.projectiles.remove(projectile)
                checks.damage_cd = True
                
                
                cd_start = pygame.time.get_ticks() 
        if entities.player.character.x > SB.screen_width or entities.player.character.x < 0 or entities.player.character.y > SB.screen_height or entities.player.character.y < 0:
            entities.player.health -= 1
            checks.damage_cd = True
            
            cd_start = pygame.time.get_ticks()
    if checks.damage_cd and pygame.time.get_ticks() - cd_start > 200:
        checks.damage_cd = False
        
   

   # checks if the player has lost a life and gives them protection if so
    if entities.player.health <= 0:
        entities.player.lives -= 1
        entities.player.health = difficulty.health
        checks.life_cd = True
        print("life cooldown started")
        cd_start = pygame.time.get_ticks()
    if checks.life_cd:
        if pygame.time.get_ticks() - cd_start > 3000:
            checks.life_cd = False
            print("life cooldown done")

    for projectile in entities.player_projectiles:
        for enemy in entities.enemies:
            if projectile.character.colliderect(enemy.character):
                enemy.health -= projectile.damage
                projectile.kill()

    for enemy in entities.enemies:
        if enemy.health <= 0:
            enemy.kill()
            entities.player.score += 100 * difficulty.score_multiplier

