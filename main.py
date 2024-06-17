import pygame
import screen_background as SB # also handles ending the game
import text as t 
import entities
import damagecheck as dc
import gameEnd as ge
import draw
import checks

run = True
while run:
    run_time = pygame.time.get_ticks()
    run = ge.game_end_check()
    SB.screen.fill(SB.screen_color)
    
    draw.draw(run_time)
    entities.player.update() #updates the players position
    entities.enemies.update() #updates the enemies position
    pygame.display.update() #updates the screen
    dc.damage_check() #checks if the player should/can be damaged
    entities.projectiles.update()
    entities.spawn_enemies(run_time)
    entities.spawn_projectiles(run_time)
    
    t.display_text() # text doesnt show for some reason, fix later
    
    if ge.game_end_check == False: #checks if the game should end and ends it if it should 
        break 

    
pygame.quit()