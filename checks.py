import pygame

global damage_cd
global life_cd
global show_projectiles
global run_time

damage_cd = False
life_cd = False
show_projectiles = True
run_time = pygame.time.get_ticks()

display_lost_life = False