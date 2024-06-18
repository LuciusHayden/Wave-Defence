#all our text should go here so we can easily change it without lookiing through a lot of the code
#screen.blit(//text_name//, (screen_width - health_text.get_width() - 10, 10)) to add the text to the screen

import pygame
import entities
import screen_background as SB
import checks

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

introduction_text = font.render("PLACEHOLDER", True, (255, 255, 255))



def display_text(run_time):
    health_text = font.render(f'Health: {entities.player.health}', True, (255, 0, 0))
    SB.screen.blit(health_text, (SB.screen_width - health_text.get_width() - 10, 10))
    live_lost_text = font.render(f'You have lost a live', True, (255, 0, 0))
    health_text = font.render(f'Health: {entities.player.health}', True, (255, 0, 0))
    lives_text = font.render(f'Lives: {entities.player.lives}', True, (255, 0, 0))
    timer_text = font.render(f'Time: {run_time // 1000}', True, (255, 0, 0))

    lost_text = font.render(f'You loose', True, (255, 0, 0))
    SB.screen.blit(health_text, (SB.screen_width - health_text.get_width() - 10, 10))
    SB.screen.blit(timer_text, (10, 10))
    SB.screen.blit(lives_text, (SB.screen_width - lives_text.get_width() - 200, 10))

    if checks.display_lost_life == True:
        SB.screen.blit(live_lost_text, (SB.screen_width // 2 - live_lost_text.get_width() // 2, SB.screen_height // 2 - live_lost_text.get_height() // 2))
        checks.life_cd = True