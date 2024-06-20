import pygame
import auras

global damage_cd
global life_cd
global show_projectiles
global run_time
global rolled

global dice
global show_aura
global selected

damage_cd = False
life_cd = False
show_projectiles = True
run_time = pygame.time.get_ticks()

total_cooldown = 5000

display_lost_life = False

show_aura = True
stats_changed = False
cd_start = 0

#remaining_cooldown = total_cooldown - (pygame.time.get_ticks() - auras.cd_start)

scoreboard = 0

rolled = False

show_title = True

timer = 0

once_counter = 0