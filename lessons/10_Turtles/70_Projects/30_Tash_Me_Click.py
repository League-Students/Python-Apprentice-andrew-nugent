"""
# 30_Tash_Me_Click.py

Copy your old 20_Tash_Me.py code here and update the program to put the moustache where you click on the screen.

Hint: See 10_More_Turtle_Programs, section 'Respond to Screen Clicks'
"""
 
... # Your code hereimport pygame
import random
import sys
import math
import pygame

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_BLUE = (0, 200, 255)
LASER_GREEN = (0, 255, 100)
ENEMY_RED = (255, 50, 50)
BOSS_PURPLE = (200, 0, 255)
GOLD = (255, 215, 0)

# Screen Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Raider: Boss Rush")
clock = pygame.time.Clock()

# --- GAME OBJECT CLASSES ---

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40), pygame.SRCALPHA)
        # Draw a sleek spaceship triangle
        pygame.draw.polygon(self.image, PLAYER_BLUE, [(25, 0), (0, 40), (50, 40)])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 30
        self.speed = 6
        self.health = 100
        self.shoot_delay = 250  # milliseconds
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # Movement Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Boundary Restrictions
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # Automate / Continuous Shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            laser = Laser(self.rect.centerx, self.rect.top, -10, LASER_GREEN)
            all_sprites.add(laser)
            player_lasers.add(laser)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.image = pygame.Surface((35, 35), pygame.SRCALPHA)
        self.level = level
        
        # Level-based visual variance and stat scaling
        if level == 1:
            pygame.draw.rect(self.image, ENEMY_RED, [0, 0, 35, 35])
            self.speedy = random.randint(2, 4)
            self.speedx = 0
            self.health = 1
        else: # Level 2+ Scouts are agile and weave side-to-side
            pygame.draw.polygon(self.image, ENEMY_RED, [(17, 35), (0, 0), (35, 0)])
            self.speedy = random.randint(3, 5)
            self.speedx = random.choice([-2, -1, 1, 2])
            self.health = 2

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # Reverse horizontal direction at walls
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speedx *= -1

        # Recycle enemies passing off screen bottom
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((120, 70), pygame.SRCALPHA)
        # Giant threatening boss shape
        pygame.draw.polygon(self.image, BOSS_PURPLE, [(60, 70), (0, 0), (120, 0)])
        pygame.draw.rect(self.image, GOLD, [40, 10, 40, 15]) 
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.y = -100  # Start off-screen for entry intro
        self.speedx = 3
        self.max_health = 100
        self.health = self.max_health
        self.shoot_delay = 600
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # Entry Phase: fly down to battle position
        if self.rect.y < 60:
            self.rect.y += 2
            return

        # Regular Boss Movement (Horizontal Strafe)
        self.rect.x += self.speedx
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speedx *= -1
        
        # Fire continuous barrages
        self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            # Targeted radial burst shooting pattern
            for angle_offset in [-2, 0, 2]:
                laser = Laser(self.rect.centerx, self.rect.bottom, 6, ENEMY_RED, angle_offset)
                all_sprites.add(laser)
                enemy_lasers.add(laser)

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, speedy, color, speedx=0):
        super().__init__()
        self.image = pygame.Surface((6, 15))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = speedy
        self.speedx = speedx

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        # Kill if it moves completely off-screen
        if self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()

# --- CORE GAME FUNCTIONS ---

def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("arial", size, bold=True)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

def draw_ui(score, level, player_health, boss=None):
    # Score and Level Info
    draw_text(screen, f"SCORE: {score}", 22, 80, 25)
    draw_text(screen, f"LEVEL: {level}", 22, SCREEN_WIDTH // 2, 25, GOLD)
    
    # Player Health Bar Base
    pygame.draw.rect(screen, (100, 0, 0), [SCREEN_WIDTH - 170, 15, 150, 20])
    # Active Health fill
    if player_health > 0:
        pygame.draw.rect(screen, (0, 255, 0), [SCREEN_WIDTH - 170, 15, 1.5 * player_health, 20])
    draw_text(screen, "HP", 16, SCREEN_WIDTH - 185, 25)

    # Boss Health Bar (Rendered only on Level 3)
    if boss and level == 3:
        draw_text(screen, "BOSS ALIVE", 18, SCREEN_WIDTH // 2, 60, BOSS_PURPLE)
        pygame.draw.rect(screen, (50, 50, 50), [SCREEN_WIDTH // 4, 80, SCREEN_WIDTH // 2, 15])
        if boss.health > 0:
            health_width = (SCREEN_WIDTH // 2) * (boss.health / boss.max_health)
            pygame.draw.rect(screen, BOSS_PURPLE, [SCREEN_WIDTH // 4, 80, health_width, 15])

# --- MAIN ENGINE LOOP ---

# Sprite Groups Setup
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player_lasers = pygame.sprite.Group()
enemy_lasers = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Track Gameplay Variables
score = 0
current_level = 1
level_transition_timer = 0
boss_spawned = False
active_boss = None

# Spawn initial level 1 targets
for i in range(6):
    e = Enemy(current_level)
    all_sprites.add(e)
    enemies.add(e)

running = True
game_over = False
victory = False

while running:
    clock.tick(FPS)
    
    # 1. Input Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if (game_over or victory) and event.key == pygame.K_r:
                # Reset Core Game State variables on R restart
                all_sprites.empty()
                enemies.empty()
                player_lasers.empty()
                enemy_lasers.empty()
                player = Player()
                all_sprites.add(player)
                score = 0
                current_level = 1
                boss_spawned = False
                active_boss = None
                game_over = False
                victory = False
                for i in range(6):
                    e = Enemy(current_level)
                    all_sprites.add(e)
                    enemies.add(e)

    # 2. State & Physics Progression Updates
    if not game_over and not victory:
        all_sprites.update()

        # Progression Mechanics check (Levels 1 & 2)
        if current_level == 1 and score >= 15:
            current_level = 2
            # Add extra, faster enemies for Level 2 difficulty spike
            for i in range(3):
                e = Enemy(current_level)
                all_sprites.add(e)
                enemies.add(e)
                
        elif current_level == 2 and score >= 40:
            current_level = 3
            # Clear standard enemies out for final showdown duel
            for e in enemies:
                e.kill()

        # Boss Activation Trigger (Level 3)
        if current_level == 3 and not boss_spawned:
            active_boss = Boss()
            all_sprites.add(active_boss)
            boss_spawned = True

        # --- COLLISION PHYSICS DETECTION ---

        # Case A: Player lasers hitting normal generic enemies
        hits = pygame.sprite.groupcollide(enemies, player_lasers, False, True)
        for enemy, lasers in hits:
            enemy.health -= len(lasers)
            if enemy.health <= 0:
                enemy.kill()
                score += 5
                # Respawn normal enemies only if boss is not yet active
                if current_level < 3:
                    new_enemy = Enemy(current_level)
                    all_sprites.add(new_enemy)
                    enemies.add(new_enemy)

        # Case B: Player lasers striking active level Boss


