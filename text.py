#all our text should go here so we can easily change it without lookiing through a lot of the code
#screen.blit(//text_name//, (screen_width - health_text.get_width() - 10, 10)) to add the text to the screen

import pygame
import entities
import screen_background as SB
import checks
import difficulty

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

introduction_text = font.render("PLACEHOLDER", True, (255, 255, 255))



def display_text(run_time):

    
    health_text = font.render(f'Health: {entities.player.health}', True, (255, 0, 0)) 
    live_lost_text = font.render(f'You have lost a live', True, (255, 0, 0))
    health_text = font.render(f'Health: {entities.player.health}', True, (255, 0, 0))
    lives_text = font.render(f'Lives: {entities.player.lives}', True, (255, 0, 0))
    timer_text = font.render(f'Time: {run_time // 1000}', True, (255, 0, 0))
    lost_text = font.render(f'You loose', True, (255, 0, 0))
    score_text = font.render(f'Score: {round(entities.player.score)}', True, (255, 0, 0))
    game_name = font.render(f'Wave Defender', True, (255, 0, 0))
    guide = font.render(f"Press space to reroll your Aura, each aura has different stats but generally, rarer ones are better.", True, (255, 0, 0))
    guide2 = font.render(f"Rerolling costs 1000 of your score.", True, (255, 0, 0))
    difficulty_text = font.render(f'Difficulty: {difficulty.text}', True, (255, 0, 0))
    difficulty_text2 = font.render(f'Press F to change difficulty', True, (255, 0, 0))
    if checks.show_title == False:
        SB.screen.blit(health_text, (SB.screen_width - health_text.get_width() - 10, 10))
        SB.screen.blit(timer_text, (10, 10))
        SB.screen.blit(lives_text, (SB.screen_width - lives_text.get_width() - 200, 10))
        SB.screen.blit(health_text, (SB.screen_width - health_text.get_width() - 10, 10))
        SB.screen.blit(score_text, (SB.screen_width - score_text.get_width() - 10, 40))

    if checks.show_title == True:
        SB.screen.blit(game_name, (SB.screen_width // 2 - game_name.get_width() // 2, SB.screen_height // 2 - game_name.get_height() // 2))
        SB.screen.blit(guide, (SB.screen_width // 2 - introduction_text.get_width() // 2 - 600, SB.screen_height // 2 - introduction_text.get_height() // 2 +200))
        SB.screen.blit(guide2, (SB.screen_width // 2 - introduction_text.get_width() // 2 - 100 , SB.screen_height // 2 - introduction_text.get_height() // 2 + 250))
        SB.screen.blit(difficulty_text, (SB.screen_width // 2 - game_name.get_width() // 2,SB.screen_height // 2 - game_name.get_height() // 1.5 + + 400))
        SB.screen.blit(difficulty_text2, (SB.screen_width // 2 - game_name.get_width() // 2 - 50,SB.screen_height // 2 - game_name.get_height() // 1.5 + 450))
    if checks.display_lost_life == True:
        SB.screen.blit(live_lost_text, (SB.screen_width // 2 - live_lost_text.get_width() // 2, SB.screen_height // 2 - live_lost_text.get_height() // 2))
        checks.life_cd = True