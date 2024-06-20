# anything that relates to difficulty should go here
# keep in mind that the spawn rate actually is in reverse, a smaller number means faster spawns

difficulty = 0


if difficulty == 0:
    health = 150
    lives = 3
    damage = 10
    spawn_rate = 2
    enemy_health = 30
    enemy_damage = 5
    score_multiplier = 1.5
    text = "Easy"
elif difficulty == 1:
    health = 100
    lives = 2
    damage = 5
    spawn_rate = 1
    enemy_health = 50
    enemy_damage = 8
    score_multiplier = 1
    text = "Normal"
else:
    health = 75
    lives = 1
    damage = 2
    spawn_rate = 0.5
    enemy_health = 70
    enemy_damage = 10
    score_multiplier = 0.5
    text = "Hard"

def set_difficulty():
    global text
    if difficulty == 0:
        text = "Easy"
        print("yuh")
    elif difficulty == 1:
        text = "Normal"
    else:
        text = "Hard"