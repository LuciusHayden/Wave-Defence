# anything that relates to difficulty should go here


difficulty = ""


if difficulty == "easy":
    health = 100
    lives = 3
    damage = 10
    spawn_rate = 0.5
elif difficulty == "medium":
    health = 75
    lives = 2
    damage = 5
    spawn_rate = 1
else:
    health = 50
    lives = 1
    damage = 2
    spawn_rate = 2