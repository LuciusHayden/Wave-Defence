import pygame
import difficulty
import screen_background as SB

class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, health, damage, speed, pos, character):
        super().__init__()
        self.health = health
        self.damage = damage
        self.speed = speed
        self.pos = pygame.math.Vector2(x, y)
        self.character = character

class player(Character):
    def __init__(self, x, y, health, damage, speed, lives, character):
        super().__init__(x, y, speed, character)  # initialize the character attribute from the parent class
        self.health = difficulty.health
        self.damage = difficulty.damage
        self.lives = difficulty.lives
        self.character = pygame.Rect(self.x, self.y, 30, 30)
        
        def update(self):
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                player.pos.x -= player.speed
            if key[pygame.K_d]:
                player.pos.x += player.speed
            if key[pygame.K_w]:
                player.pos.y -= player.speed
            if key[pygame.K_s]:
                player.pos.y += player.speed

class Enemy(Character):
    def __init__(self, x, y, health, damage, speed, target):
        super().__init__(x, y, health, damage, speed)
        self.target = (player.pos.x, player.pos.y)
        direction_vector = pygame.math.Vector2(player.pos.x - x, player.pos.y - y)
        self.velocity = direction_vector.normalize() * self.speed

        def move(self):
            self.target = (player.pos.x, player.pos.y)
            direction_vector = pygame.math.Vector2(self.target[0] - self.pos.x, self.target[1] - self.pos.y)
            self.velocity = direction_vector.normalize() * self.speed
            self.pos += self.velocity
            self.character.topleft = (int(self.pos.x), int(self.pos.y))
    
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

        