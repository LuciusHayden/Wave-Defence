import pygame
import screen_background as SB # also handles ending the game
import text as t 
import entities
import damagecheck as dc
import gameEnd as ge
import draw
import checks
import auras

entities.starting_enemies() #spawns 5 enemies to start out with

run = True
while run:
    run_time = pygame.time.get_ticks()
    run = ge.game_end_check()
    SB.screen.blit(SB.background_image, (0, 0))

    auras.roll_check()

    auras.selected.draw()
    auras.selected.stat_change()
    t.display_text(run_time) # text doesnt show for some reason, fix later
    
    draw.draw(run_time)
    
    entities.player.update() #updates the players position
    entities.enemies.update() #updates the enemies position
    entities.shoot_projectiles()
    dc.damage_check() #checks if the player or enemies should/can be damaged
    entities.projectiles.update()
    entities.spawn_enemies(run_time)
    entities.spawn_projectiles(run_time)
    entities.player_projectiles.update()
    
    
    """for projectile in entities.player_projectiles:
        print(entities.player.health, projectile.damage) # for testing"""
    
    pygame.display.flip()
    if ge.game_end_check == False: #checks if the game should end and ends it if it shoudld 
        break

    
pygame.quit()