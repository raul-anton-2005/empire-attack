#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
Empire Attack
"""

# Built-in/Generic Imports

import pygame
import random
import os

# Own modules

from characters import Cube
from characters import Enemy
from characters import Heart
from characters import Reward

__authors__ = ["Raúl Antón Echevarría"]
__contact__ = ["raulantonechevarria@gmail.com"]
__copyright__ = "Free To Use"
__credits__ = ["Raúl Antón Echevarría"]
__date__ = "2024/08/22"
__email__ = ["raulantonechevarria@gmail.com"]
__license__ = "GPLv3"
__maintainer__ = "Developer"
__status__ = "Production"
__version__ = "0.0.2"


pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Empire Attack')

def manage_keys(keys):
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        cube.x -= cube.speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        cube.x += cube.speed


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)     
FPS = 60   
FONT = pygame.font.SysFont("Cascadia Code", 40)
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(MAIN_DIR, 'assets')
USER_FOLDER = os.path.expanduser("~")
GAME_FOLDER = os.path.join(USER_FOLDER, 'EmpireAttack')


clock = pygame.time.Clock()

time_spent = 0
time_between_enemies = 1000
last_bullet = 0
time_between_bullets = 350
last_reward = 0
time_between_rewards = 45000
time_infinite_bullets = 10000


playing = True

cube = Cube(WIDTH/2, HEIGHT-120)
pew = pygame.mixer.Sound(f'{ASSETS_DIR}/pew.mp3')
pew.set_volume(0.25)
explotion = pygame.mixer.Sound(f'{ASSETS_DIR}/explotion.mp3')
heal = pygame.mixer.Sound(f'{ASSETS_DIR}/heal.mp3')
enemies = []
lives = 3
points = 0
heart_spawned = False
current_points = None
enemies_destroyed = 0
take_life = False
reward_spawned = False
infinite_bullets = False
number_infinite_bullets = 0

lose_text = FONT.render('YOU LOST', True, 'white')

pygame.mixer.music.load(f'{ASSETS_DIR}/sw_theme.mp3')
pygame.mixer.music.set_volume(0.85)
pygame.time.delay(500)
pygame.mixer.music.play(loops=-1)

while playing:

    WINDOW.fill('black')
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    life_text = FONT.render(f'Lives: {lives}', True, 'white')
    points_text = FONT.render(f'Points: {points}', True, 'white')

    ### MANAGE EVENTS ###
    for event in events:
            if event.type == pygame.QUIT:
                playing = False
                pygame.mixer.music.stop()
            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                WINDOW = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            
    area = HEIGHT * WIDTH
    cube.speed = 7.5 * (area / (1000 * 800))

    ### INCREASE SPEED ###

    if points != 0 and points % 10 == 0:
        Enemy.speed += 0.005
    
    if lives > 0:

        ### MANAGE ENEMIES ###

        time_spent += clock.tick(FPS)

        if time_spent > time_between_enemies:
            enemies.append(Enemy(random.randint(5, WIDTH - Enemy.width), - 80))
            time_spent = 0

        for enemy in enemies:
            enemy.draw(WINDOW)
            enemy.movement()
            if pygame.Rect.colliderect(cube.rect, enemy.rect):
                lives -= 1
                explotion.play()
                enemies.remove(enemy)
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                enemies_destroyed += 1
            if enemy.life == 0:
                enemies.remove(enemy)
                enemies_destroyed = 0
                points += 1

        if enemies_destroyed % 20 == 0 and enemies_destroyed != 0 and current_points != points:
            current_points = points
            take_life = True
        if take_life:
            take_life = False
            lives -= 1
            explotion.play()

        ### MANAGE BULLETS ###

        for bullet in cube.bullets:
            bullet.draw(WINDOW)
            bullet.movement()
            for enemy in enemies:
                if pygame.Rect.colliderect(enemy.rect, bullet.rect):
                    enemy.life -= 10
                    cube.bullets.remove(bullet)

        if pygame.time.get_ticks() - last_bullet > time_between_bullets:
            cube.generate_bullets()
            pew.play()
            last_bullet = pygame.time.get_ticks()
        manage_keys(keys)

        ### MANAGE CUBE ###

        if cube.x > WIDTH - cube.width:
            cube.x = WIDTH - cube.width
        if cube.x < 0:
            cube.x = 0 
        cube.draw(WINDOW)

        ### MANAGE REWARDS ###

        if pygame.time.get_ticks() - last_reward > time_between_rewards:
            reward_spawned = True
            pos_x_r = random.randint(5, WIDTH - Enemy.width)
            pos_y_r = 25
            last_reward = pygame.time.get_ticks()
            reward = Reward(pos_x_r, pos_y_r)
        if reward_spawned:
            reward.draw(WINDOW)
            reward.movement()
            if pygame.Rect.colliderect(cube.rect, reward.rect):
                reward_spawned = False
                pos_x_r = None
                pos_y_r = None
                infinite_bullets = True
                time_between_bullets = 175
        if infinite_bullets:
            number_infinite_bullets += 10
            if number_infinite_bullets > time_infinite_bullets:
                infinite_bullets = False
                time_between_bullets = 350
                number_infinite_bullets = 0

        ### MANAGE LIVES ###

        if points != 0:
            if points % 50 == 0 and not heart_spawned and points != current_points:
                current_points = points
                heart_spawned = True
                pos_x_h = random.randint(5, WIDTH - Enemy.width)
                pos_y_h = 25
                heart = Heart(pos_x_h, pos_y_h)
            if heart_spawned:
                heart.draw(WINDOW)
                heart.movement()
                if pygame.Rect.colliderect(cube.rect, heart.rect):
                    heart_spawned = False
                    if time_between_enemies > 800:
                        time_between_enemies -= 50
                    pos_x_h = None
                    pos_y_h = None
                    lives += 1
                    heal.play()
            if heart_spawned and heart.y > HEIGHT:
                heart_spawned = False
                pos_x_h = None
                pos_y_h = None
    else:    
        WINDOW.blit(lose_text, (WIDTH/2.3, HEIGHT/2))

    WINDOW.blit(life_text, (15, 15))
    WINDOW.blit(points_text, (15, 60))
    pygame.display.update()

pygame.display.quit()

if not os.path.exists(GAME_FOLDER):
    os.makedirs(GAME_FOLDER)

ranking_path = os.path.join(GAME_FOLDER, "ranking.txt")

name = input('Enter your name: ')

if name != '':
    with open(ranking_path, 'a') as ranking:
        ranking.write(f'{name}#{points}#{__version__}\n')

table = []
with open(ranking_path, 'r') as file:
    for line in file:
        table.append(line.strip().split('#'))

table = sorted(table, key=lambda x: int(x[1]), reverse=True)

print('\n\n\n\n\n\n')
for element in table:
    print(f'{element[0]}: {element[1]} -> {element[2]}')
print('\n\n\n\n\n\n')

print(f"Ranking guardado en: {ranking_path}")
