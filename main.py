import pygame
import screen_background as SB # also handles ending the game
import text as t 
import entities
import damagecheck as dc
import gameEnd as ge
import draw
import checks
import auras
import difficulty


run = True
while run:
    key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    SB.screen.blit(SB.background_image, (0, 0))
    if checks.show_title == True:
        entities.player.health = difficulty.health
        entities.player.lives = difficulty.lives
        for enemy in entities.enemies:
            enemy.kill()
        t.display_text(0)

        if key[pygame.K_f] and pygame.time.get_ticks() - checks.timer > 1000:
            difficulty.set_difficulty()
            difficulty.difficulty += 1
            difficulty.set_difficulty()
            if difficulty.difficulty > 2:
                difficulty.difficulty = 0
            checks.timer = pygame.time.get_ticks()

        

        
        if key[pygame.K_SPACE]:
            checks.show_title = False

        pygame.display.flip()
        if ge.game_end_check == False: #checks if the game should end and ends it if it shoudld 
            break


    else:

        if checks.once_counter == 0: # makes sure that enemies only spawn once
            entities.starting_enemies() #spawns 5 enemies to start out with
            checks.once_counter += 1

        run_time = pygame.time.get_ticks()
        run = ge.game_end_check()
        

        auras.roll_check()

        auras.selected.draw()
        auras.selected.stat_change()
        t.display_text(run_time) # text doesnt show for some reason, fix later
        
        draw.draw(run_time)
        
        entities.player.update() #updates the players position
        entities.enemies.update() #updates the enemies position
        entities.enemies2.update() # updates the enemies position (stronger type)
        entities.enemies3.update() # updates the enemies position (strongest type)
        entities.shoot_projectiles()
        dc.damage_check() #checks if the player or enemies should/can be damaged
        entities.projectiles.update()
        entities.spawn_enemies(run_time)
        entities.spawn_projectiles(run_time)
        entities.player_projectiles.update()

        pygame.display.flip()
        if ge.game_end_check == False: #checks if the game should end and ends it if it shoudld 
            break

    
    
pygame.quit()