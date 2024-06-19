import pygame
import random
import text as t
import checks
import entities
import difficulty

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 40)

screen_width = 1600
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

MythicList = []
RareList = []
UncommonList = []
CommonList = []

class aura:
    def __init__(self, x, y, colorX, colorY, colorZ, aura_name, rarity, multiplier_1, multiplier_2): # Multiplier 1 will effect damage, multiplier 2 will effect health 
        self.x = x
        self.y = y
        self.colorX = colorX
        self.colorY = colorY
        self.colorZ = colorZ
        self.color = (self.colorX, self.colorY, self.colorZ)
        self.radius = 40
        self.aura_name = font.render(aura_name, True, (255, 255, 255))
        self.rarity = font.render(rarity, True, (255, 255, 255))
        self.backgroundX = colorX - 120
        self.backgroundY = colorY - 120
        self.backgroundZ = colorZ - 120
        self.multiplier_1 = multiplier_1
        self.multiplier_2 = multiplier_2
        
        
    def draw(self):
        global wait
        global wait_time
        
        self.x = entities.player.character.x
        self.y = entities.player.character.y
        
        
        
        if self.backgroundX  <= 0:
            self.backgroundX = 0
        if self.backgroundY <= 0:
            self.backgroundY = 0
        if self.backgroundZ <= 0:
            self.backgroundZ = 0
        
        self.background_color = (self.backgroundX, self.backgroundY, self.backgroundZ)
        pygame.draw.circle(screen, self.background_color, (self.x + 15, self.y + 17), self.radius)
        #screen.blit(self.aura_name, ((screen_width // 2 - self.aura_name.get_width() // 2, screen_height // 2 - self.aura_name.get_height() // 2)))
        #screen.blit(self.rarity, (screen_width // 2 - self.rarity.get_width() // 2, screen_height // 2 - self.rarity.get_height() // 2 + 250))

    def stat_change(self):
        if checks.stats_changed == False:
            for projectile in entities.player_projectiles:
                projectile.damage *= self.multiplier_1 
            entities.player.health *= self.multiplier_2
            
            
            checks.stats_changed = True

def roll():
    global dice
    global rolled
    global show_aura
    global selected
    
    roll = random.randint(0, 1000)
    if roll > 900 and roll < 1000 and not rolled:
        i = len(MythicList)
        dice2 = random.randint(0, i-1)
        selected = MythicList[dice2]
        show_aura = True
        checks.rolled = True
    if roll > 800 and roll < 900 and not rolled:
        i = len(RareList)
        dice2 = random.randint(0, i-1)
        selected = RareList[dice2]
        show_aura = True
        checks.rolled = True
    if roll > 500 and roll < 800 and not rolled:
        i = len(UncommonList)
        dice2 = random.randint(0, i-1)
        selected = UncommonList[dice2]
        show_aura = True
        checks.rolled = True
    if roll > 0 and roll < 500 and not rolled:
        i = len(CommonList)
        dice2 = random.randint(0, i-1)
        selected = CommonList[dice2]
        show_aura = True
        checks.rolled = True

    
    return selected

def roll_check():
    key = pygame.key.get_pressed()
    if not checks.rolled and key[pygame.K_SPACE] and entities.player.score >= 1000:
        for projectile in entities.player_projectiles:
            projectile.damage = difficulty.damage
        entities.player.health = difficulty.health
        
        checks.stats_changed = False
        roll()
        checks.cd_start = pygame.time.get_ticks()
        entities.player.score -= 1000

            
    if checks.rolled and pygame.time.get_ticks() - checks.cd_start > total_cooldown:
        checks.rolled = False


BloodLust = aura(700, 475, 130, 0, 0,  "BloodLust", "Mythical", 4.5, 0.3)
Impeached = aura(700, 475, 0, 70,0, "Impeached", "Mythical" , 1.5, 2.5)
ArchAngle = aura(700, 475, 250, 241, 147, "ArchAngle", "Mythical", 1 , 3.5)
Genesis = aura(700, 475, 200, 200, 255, "Genesis", "Mythical", 2, 2)
StarScourge = aura(700, 475, 169, 20, 199, "StarScourge", "Mythical", 3, 1.5)

MythicList.append(Impeached)
MythicList.append(BloodLust)
MythicList.append(ArchAngle)
MythicList.append(Genesis)
MythicList.append(StarScourge)

Undead = aura(700, 475, 0, 0, 70, "Undead", "Rare", 1, 2)
Lunar = aura(700, 475, 50, 70, 200, "Lunar", "Rare", 1.5, 1.5)
StarLight = aura(700, 475, 70, 70, 150, "Starlight", "Rare", 1.5, 1.5)
Eclipse = aura(700, 475, 200, 70, 70, "Eclipse", "Rare", 1.8, 1.2)
Comet = aura(700, 475, 150, 70, 70, "Comet", "Rare", 0.7, 2.2)
Solar = aura(700, 475, 255, 140, 0, "Solar", "Rare", 2.2, 0.7)

RareList.append(Undead)
RareList.append(Lunar)
RareList.append(StarLight)
RareList.append(Eclipse)
RareList.append(Comet)
RareList.append(Solar)


Natural = aura(700, 475, 70, 200, 70, "Natural", "Uncommon", 1.2, 1.2)
Uncommon = aura(700, 475, 70, 70, 70, "Uncommon", "Uncommon", 1.4, 1)
Rage = aura(700, 475, 150, 70, 70, "Rage", "Uncommon", 2, 0.6)
Ruby = aura(700, 475, 255, 70, 70, "Ruby", "Uncommon", 0.6, 2)
Gilded = aura(700, 475, 181, 201, 26, "Gilded", "Uncommon", 1.2, 1.2)

UncommonList.append(Natural)
UncommonList.append(Uncommon)
UncommonList.append(Rage)
UncommonList.append(Ruby)
UncommonList.append(Gilded)

Common = aura(700, 475, 70, 70, 70, "Common", "Common", 1, 1)
Good = aura(700, 475, 70, 70, 70, "Good", "Common" , 1, 1.1)
Crystal = aura(700, 475, 144, 0, 255, "Crystal", "Common", 0.9, 1.1)
Evil = aura(700, 475, 144, 70, 70, "Evil", "Common", 1.2, 0.8)

CommonList.append(Common)
CommonList.append(Good)
CommonList.append(Crystal)
CommonList.append(Evil)


run = True
rolled = False 
show_aura = False
remaining_cooldown = 0
total_cooldown = 2000




selected = Common

#print(f"Rolled: {rolled} Show Aura: {show_aura} Remaining Cooldown: {remaining_cooldown}" )
#print(MythicList, CommonList)