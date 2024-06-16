import pygame
import screen_background as SB # also handles ending the game
import text as t #screen.blit(//text_name//, (screen_width - health_text.get_width() - 10, 10)) to add the text to the screen
import entities
import damagecheck as dc
import gameEnd as ge

run = True
while run:
    run = ge.game_end_check()
    SB.screen.fill(SB.screen_color)
    #draws the player and the enemies, in the future this should be moved to a seperate file
    pygame.draw.rect(SB.screen, (0, 255, 0), entities.player.character) 
    pygame.draw.rect(SB.screen, (255, 0, 0), entities.enemy.character)
    
    entities.player.update() #updates the players position
    entities.enemy.update() #updates the enemies position
    pygame.display.update() #updates the screen
    dc.damage_check()
    
    if ge.game_end_check == False: #checks if the game should end and ends it if it should 
        break 

    
pygame.quit()