#ngl i dont know what on earth im doing here, this is a mess.

import pygame
import difficulty
import screen_background as SB

enemies = pygame.sprite.Group()

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
        

"""class Enemy(Character):
    def __init__(self, x, y, health, damage, speed, target, spawn_rate, pos):
        super().__init__(x, y, health, damage, speed, pos)
        self.target = player.character
        self.pos = pygame.math.Vector2(x, y)
        direction_vector = pygame.math.Vector2(player.character.x - x, player.character.y - y)
        self.velocity = direction_vector.normalize() * self.speed
        self.spawn_rate = spawn_rate

    def update(self):
        # Calculate the direction vector from the enemy to the player
        direction_vector = pygame.math.Vector2(self.target.x - self.pos.x, self.target.y - self.pos.y)

        # Normalize the direction vector and multiply by the enemy's speed
        
        self.velocity = direction_vector.normalize() * self.speed
        
        # Update the enemy's position
        self.pos += self.velocity
        
        # Update the enemy's position attributes
        self.x, self.y = int(self.pos.x), int(self.pos.y)"""

class Enemy(Character):
    def __init__(self, x, y, health ,damage, speed, target, spawn_rate, pos):
        super().__init__(x, y, health, damage, speed, pos)
        self.health = difficulty.enemy_health
        self.damage = difficulty.enemy_damage
        self.character = pygame.Rect(x, y, 30, 30) 
        self.speed = speed
        self.target = target
        direction_vector = pygame.math.Vector2(player.character.x - x, player.character.y - y)
        self.velocity = direction_vector.normalize() * self.speed
        self.spawn_rate = difficulty.spawn_rate

    def update(self):
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        self.pos += self.velocity
        self.character.topleft = (int(self.pos.x), int(self.pos.y))
        direction_vector = pygame.math.Vector2(player.character.x - self.character.x, player.character.y - self.character.y)
        if direction_vector.length() > 0:  # makes sure the program doesnt crash when the player collides with the enemy (vectors of length 0 cannot be normalized)
            self.velocity = direction_vector.normalize() * self.speed
        if self.character.x > SB.screen_width or self.character.x < 0 or self.character.y > SB.screen_height or self.character.y < 0:
            self.kill()
        

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
        self.velocity = direction_vector.normalize() * self.speed

        def update(self):
            self.pos += self.velocity
            self.character.topleft = (int(self.pos.x), int(self.pos.y))
            if self.character.x > SB.screen_width or self.character.x < 0 or self.character.y > SB.screen_height or self.character.y < 0:
                self.kill()

# x, y, health, damage, speed, lives, pos
player = Player(800, 500, difficulty.health, difficulty.damage, 1.5, difficulty.lives, (800, 500))

enemy = Enemy(200, 200, difficulty.health, difficulty.damage, 0.5, (player.character), difficulty.spawn_rate, (200, 200))