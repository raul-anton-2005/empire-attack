import pygame
import random
from characters import Cube
from characters import Enemy


pygame.init()
pygame.mixer.init()


def manage_keys(keys):
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cube.x -= cube.speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cube.x += cube.speed


WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])     
FPS = 60   
FONT = pygame.font.SysFont("Cascadia Code", 40)

clock = pygame.time.Clock()

time_spent = 0
time_between_enemies = 1000
last_bullet = 0
time_between_bullets = 350

playing = True

cube = Cube(WIDTH/2, HEIGHT-100)
xwing = pygame.image.load('assets/xwing.jpg')
xwing = pygame.transform.scale(xwing, (100,100))
pew = pygame.mixer.Sound('assets/pew.mp3')
enemies = []
tie = pygame.image.load('assets/tie.jpg')
tie = pygame.transform.scale(tie, (75, 75))
lives = 3
points = 0
laser = pygame.image.load('assets/laser.png')
laser = pygame.transform.scale(laser, (35, 45))

lose_text = FONT.render('YOU LOST', True, 'white')

while playing:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    life_text = FONT.render(f'Lives: {lives}', True, 'white')
    points_text = FONT.render(f'Points: {points}', True, 'white')
    if points != 0 and points % 10 == 0:
        Enemy.speed += 0.005
    for event in events:
            if event.type == pygame.QUIT:
                playing = False
                
    if lives <= 0:
        WINDOW.blit(lose_text, (WIDTH/2.3, HEIGHT/2))
    else:
        time_spent += clock.tick(FPS)

        if time_spent > time_between_enemies:
            enemies.append(Enemy(random.randint(5, WIDTH - Enemy.width), 25))
            time_spent = 0
        
        WINDOW.fill('black')
        for enemy in enemies:
            enemy.draw(WINDOW)
            WINDOW.blit(tie, (enemy.x, enemy.y))
            enemy.movement()
            if pygame.Rect.colliderect(cube.rect, enemy.rect):
                lives -= 1
                enemies.remove(enemy)
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            if enemy.life == 0:
                enemies.remove(enemy)
                points += 1
        for bullet in cube.bullets:
            bullet.draw(WINDOW)
            WINDOW.blit(laser, (bullet.x, bullet.y))
            bullet.movement()
            for enemy in enemies:
                if pygame.Rect.colliderect(enemy.rect, bullet.rect):
                    enemy.life -= 10
                    cube.bullets.remove(bullet)
        if cube.x > WIDTH - cube.width:
            cube.x = WIDTH - cube.width
        if cube.x < 0:
            cube.x = 0 
        cube.draw(WINDOW)
        WINDOW.blit(xwing, (cube.x, cube.y))
        if pygame.time.get_ticks() - last_bullet > time_between_bullets:
            cube.generate_bullets()
            pew.play()
            last_bullet = pygame.time.get_ticks()
        WINDOW.blit(life_text, (15, 15))
        WINDOW.blit(points_text, (15, 60))
        manage_keys(keys)
    pygame.display.update()

quit()