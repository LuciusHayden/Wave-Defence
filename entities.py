
import pygame
import difficulty
import screen_background as SB
import checks
import random

enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
player_projectiles = pygame.sprite.Group()

player_sprite = pygame.image.load('images/player-sprite.png').convert_alpha()
enemy_sprite = pygame.image.load('images/enemy-sprite.png').convert_alpha()



class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, health, damage, speed, pos):
        super().__init__()
        self.health = health
        self.damage = damage
        self.speed = speed
        self.character = pygame.Rect(x, y, 30, 30)
        self.pos = pygame.math.Vector2(x, y)

class Player(Character):
    def __init__(self, x, y, health, damage, speed, lives, pos):
        super().__init__(x, y, health, damage, speed, pos)
        self.lives = lives
        self.image = player_sprite
        self.rect = self.image.get_rect()
        self.score = checks.scoreboard
    def update(self):
        key = pygame.key.get_pressed()
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        if key[pygame.K_a]:
            self.pos.x -= self.speed
        if key[pygame.K_d]:
            self.pos.x += self.speed
        if key[pygame.K_w]:
            self.pos.y -= self.speed
        if key[pygame.K_s]:
            self.pos.y += self.speed
        

class Enemy(Character):
    def __init__(self, x, y, health ,damage, speed, target, spawn_rate, pos, score_value):
        super().__init__(x, y, health, damage, speed, pos)
        self.health = difficulty.enemy_health
        self.damage = difficulty.enemy_damage
        self.character = pygame.Rect(x, y, 30, 30) 
        self.speed = speed
        self.target = target
        direction_vector = pygame.math.Vector2(player.character.x - x, player.character.y - y)
        self.velocity = direction_vector.normalize() * self.speed
        self.spawn_rate = difficulty.spawn_rate
        self.image = enemy_sprite
        self.rect = self.image.get_rect()
        self.score_value = score_value
    def update(self):
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        self.pos += self.velocity
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        if self.health <= 0:
            self.kill()
        direction_vector = pygame.math.Vector2(player.character.x - self.character.x, player.character.y - self.character.y)
        if direction_vector.length() > 0:  # makes sure the program doesnt crash when the player collides with the enemy (vectors of length 0 cannot be normalized)
            self.velocity = direction_vector.normalize() * self.speed
        
        

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, size, damage, speed, target):
        super().__init__()
        self.damage = damage
        self.size = size
        self.character = pygame.Rect(x, y, size, size) 
        self.speed = speed
        self.target = target
        self.pos = pygame.math.Vector2(x, y)
        direction_vector = pygame.math.Vector2(player.pos.x - x, player.pos.y - y)
        if direction_vector.length() > 0:  # makes sure the program doesnt crash when the player collides with the enemy (vectors of length 0 cannot be normalized)
            self.velocity = direction_vector.normalize() * self.speed

    def update(self):
        try: self.pos += self.velocity
        except Exception: pass
        
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        if self.character.x > SB.screen_width or self.character.x < 0 or self.character.y > SB.screen_height or self.character.y < 0:
            self.kill()

class PlayerProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, size, damage, speed):
        super().__init__()
        self.damage = damage
        self.size = size
        self.character = pygame.Rect(x, y, size, size) 
        self.speed = speed
        self.pos = pygame.math.Vector2(x, y)
        target_x, target_y = pygame.mouse.get_pos()
        direction_vector = pygame.math.Vector2(target_x - x, target_y - y)
        
        if direction_vector.length() > 0:  # makes sure the program doesnt crash when the player collides with the enemy (vectors of length 0 cannot be normalized)
            self.velocity = direction_vector.normalize() * self.speed

    def update(self):
        try: self.pos += self.velocity
        except Exception: pass
        
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        if self.character.x > SB.screen_width or self.character.x < 0 or self.character.y > SB.screen_height or self.character.y < 0:
            self.kill()
            
spawn_locatonsX = [200, 400, 600, 800, 1000, 1200, 1400, 1600]
spawn_locationsY = [200, 400, 600, 800]

#x, y, health ,damage, speed, target, spawn_rate, pos, score_value

def spawn_enemies(run_time):
    if run_time % (difficulty.spawn_rate*2000) == 0:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.9), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.5), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.5), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.8), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.5), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.9), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*5000) == 0 and run_time > 30000:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health , difficulty.damage * 2, 0.84, (player.character), difficulty.spawn_rate, (200, 200), 1000)
    if run_time % (difficulty.spawn_rate*2000) == 0 and run_time > 30000 :
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.5), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0 and run_time > 30000:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.9), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*5000) == 0 and run_time > 50000:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health , difficulty.damage * 2, 0.84, (player.character), difficulty.spawn_rate, (200, 200), 1000)
    if run_time % (difficulty.spawn_rate*10000) == 0 and run_time > 50000 :
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health * 2, difficulty.damage * 4, 0.84, (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0 and run_time > 50000:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.9), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*5000) == 0 and run_time > 50000:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health , difficulty.damage * 2, 0.84, (player.character), difficulty.spawn_rate, (200, 200), 1000)
    if run_time % (difficulty.spawn_rate*10000) == 0 and run_time > 50000 :
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health * 2, difficulty.damage * 4, 0.84, (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
    if run_time % (difficulty.spawn_rate*2000) == 0 and run_time > 50000:
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health // 2, difficulty.damage, random.uniform(0.3,0.9), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)
def spawn_projectiles(run_time):
    for enemy in enemies:
        if run_time % 1500 == 0:
            if random.randint(0,1) == 1:
                projectile = Projectile(enemy.character.x, enemy.character.y, 15,10, 0.8, (player.character.x, player.character.y))
                projectiles.add(projectile)


def starting_enemies():
    for enemy in range(5):
        enemy = Enemy(random.choice(spawn_locatonsX), random.choice(spawn_locationsY), difficulty.health, difficulty.damage, random.uniform(0.3,0.5), (player.character), difficulty.spawn_rate, (200, 200), 100)
        enemies.add(enemy)


def shoot_projectiles():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_projectile = PlayerProjectile(player.character.x, player.character.y, 10, difficulty.damage, 0.8)
            player_projectiles.add(player_projectile)
            print("Shot projectile")
#x, y, size, damage, speed

# x, y, health, damage, speed, lives, pos
player = Player(800, 500, difficulty.health, difficulty.damage, 1, difficulty.lives, (800, 500))




