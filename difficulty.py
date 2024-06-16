# anything that relates to difficulty should go here


difficulty = ""


if difficulty == "easy":
    health = 100
    lives = 3
    damage = 10
    spawn_rate = 0.5
    enemy_health = 30
    enemy_damage = 5
elif difficulty == "medium":
    health = 75
    lives = 2
    damage = 5
    spawn_rate = 1
    enemy_health = 50
    enemy_damage = 8
else:
    health = 50
    lives = 1
    damage = 2
    spawn_rate = 2
    enemy_health = 70
    enemy_damage = 10