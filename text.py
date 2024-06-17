#all our text should go here so we can easily change it without lookiing through a lot of the code
#screen.blit(//text_name//, (screen_width - health_text.get_width() - 10, 10)) to add the text to the screen

import pygame
import entities
import screen_background as SB


pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

introduction_text = font.render("PLACEHOLDER", True, (255, 255, 255))



def display_text():
    health_text = font.render(f'Health: {entities.player.health}', True, (255, 0, 0))
    SB.screen.blit(health_text, (SB.screen_width - health_text.get_width() - 10, 10))
    