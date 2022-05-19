# IMPORT MODULES.
import pygame
from pygame.locals import *
import asyncio
import os
import random

# INITIALIZE FONTS.
pygame.font.init()

# COLOURS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# INITIALIZE MODULE
pygame.init()

# SCREEN SETUP.
FPS = (60)
WIDTH, HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Wars")
score = 0

# LOAD ASSETS.
GREEN_SPACESHIP, GREEN_LASER = pygame.image.load(os.path.join("Assets", "player.png")), pygame.image.load(os.path.join("Assets", "greenlaser.png")) # Player Ship, Player Laser.
RED_SPACESHIP, RED_LASER = pygame.image.load(os.path.join("Assets","enemy.png")), pygame.image.load(os.path.join("Assets", "redlaser.png")) # Hostile Ship, Hostile Laser.
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.png")), (WIDTH, HEIGHT)) # Game Background.

# LASER CLASS 
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, SCREEN):
        SCREEN.blit(self.img, (self.x +50, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)
  
# SHIP CLASS. (SUPER)
class Ship: 
    COOLDOWN = 20
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, SCREEN):
        SCREEN.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(SCREEN)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            if laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0 
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser) 
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

# PLAYER CLASS. 
class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = GREEN_SPACESHIP
        self.laser_img = GREEN_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, SCREEN):
        super().draw(SCREEN)
        self.healthbar(SCREEN)

    def healthbar(self, SCREEN):
        pygame.draw.rect(SCREEN, (RED), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(SCREEN, (GREEN), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))
    

# ENEMY CLASS.
class Enemy(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = RED_SPACESHIP
        self.laser_img = RED_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move(self, vel):
        self.y += vel

    def shoot(self):
        
        if self.cool_down_counter == 0:
            laser = Laser(self.x -5, self.y, self.laser_img)
            self.lasers.append(laser) 
            self.cool_down_counter = 1

def collide(obj1,obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

# MAIN LOOP.
def main():
    run = True
    lost = False
    lost_count = 0
    level = 0
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 75)
    score = 0
    enemies = []
    wave_length = 5
    enemy_vel = 0.5
    laser_vel = 5
 
    player_vel = 3

    player = Player(550, 650)

    clock = pygame.time.Clock()

    def redraw_window():

        # DRAW BACKGROUND.
        SCREEN.blit(BACKGROUND, (0,0))

        # DRAW TEXT.
        lives_label = main_font.render(f"Lives: {lives}", 1, (WHITE))
        level_label = main_font.render(f"Level: {level}", 1, (WHITE))
        enemies_label = main_font.render(f"Enemies: {wave_length}", 1, (WHITE))
        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        SCREEN.blit(enemies_label, (WIDTH/2 - enemies_label.get_width()/2 - 10, 10))

        # DRAW ENEMY SHIP.
        for enemy in enemies:
            enemy.draw(SCREEN)

        # DRAW PLAYER SHIP.
        player.draw(SCREEN)

        if lost:
            lost_label = lost_font.render(f"You lost!", 1, (WHITE))
            try_again = lost_font.render(f"Click to play again.", 1, (WHITE))
            SCREEN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
            SCREEN.blit(try_again, (WIDTH/2 - try_again.get_width()/2, 450))

        
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives < 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 5:
                run = False
            else:
                continue


        if len(enemies) == 0:
            level += 1
            enemy_vel += 0.1
            wave_length += random.randrange(1,5)
            player_vel += 0.1
            enemies_remaining = wave_length
            if level>=5:
                lives += 1
            
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-150), random.randrange(-1500, -100))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        keys = pygame.key.get_pressed()

        # PLAYER MOVEMENT.
        if keys[pygame.K_a] and player.x - player_vel > 0: # LFET
           player.x -= player_vel
        if keys[pygame.K_d] and player.x + 100 + player_vel < WIDTH: # RIGHT.
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 400: # UP.
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + 100 + player_vel < HEIGHT: # DOWN.
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        if keys[pygame.K_LSHIFT]: # BOOST WHILE HELD.
            player_vel = 5
        else: # END BOOST UPON RELEASE OF LSHIFT.
            player_vel = 3

        # ENEMY MOVEMENT.
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                score -= 10
                enemies.remove(enemy)
                wave_length -= 1

            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
                wave_length -= 1

        player.move_lasers(-laser_vel, enemies)
        
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    title_label = title_font.render("Press the mouse to begin...", 1, (WHITE))
    SCREEN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
    pygame.display.update()
    run =True
    while run:
        SCREEN.blit(BACKGROUND, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()