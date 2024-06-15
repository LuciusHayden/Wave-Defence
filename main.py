import pygame
import screen_background as SB # also handles ending the game
import text as t #screen.blit(//text_name//, (screen_width - health_text.get_width() - 10, 10)) to add the text to the screen
import entities

run = True
while run:
    run = SB.game_end_check()
    SB.screen.fill(SB.screen_color)

    

    entities.player.update()
    SB.game_end_check()
    pygame.display.update()
    
pygame.quit()