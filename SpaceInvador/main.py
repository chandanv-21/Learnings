import pygame
import random
import math
from pygame import mixer

pygame.init()

# creat the screen
screen = pygame.display.set_mode((800, 600))

running = True
mixer.music.load('background.wav')
mixer.music.play(-1)
# Title of Game
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

background = pygame.image.load('background.png')
backgroundX = 0
backgroundY = 0

playerImage = pygame.image.load('spaceship2.png')
playerx = 370
playery = 480
playerx_change = 0


# Enemy
enemyImage = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
for i in range(num_of_enemies):

    enemyImage.append(pygame.image.load('enemy1.png'))
    enemyx .append(random.randint(0, 735))
    enemyy .append(random.randint(50, 150))
    enemyx_change.append(0.3)
    enemyy_change.append(20)

# bullet

# Ready -Cant see bullet on the screen
# Fire - The bullet is currently moving
bulletImage = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
# bulletx_change=0
bullety_change = 5
bulletState = "ready"
# Score text
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 0
# Game over text
game_over = pygame.font.Font('freesansbold.ttf', 64)

# Score function


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
# Game over function


def game_over_text():
    over_text = game_over.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))


def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x+16, y+10))


def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) +(math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True

    else:
        return False


# Game Loop
while running:
    # filling color to backgroung
    screen.fill((0, 0, 0))
    screen.blit(background, (backgroundX, backgroundY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # moving the spaceship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -1

            if event.key == pygame.K_RIGHT:
                playerx_change = 1

            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # Gets the current x coordinate og spaceship
                    bulletx = playerx
                    fireBullet(bulletx, bullety)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    # Checking the boundry of Spacesheep
    playerx += playerx_change
    if playerx < 0:
        playerx = 0

    elif playerx > 736:
        playerx = 736

    # Enemy movement
    for i in range(num_of_enemies):
        # Game Over

        if enemyy[i] >= 440:
            for j in range(num_of_enemies):
                enemyy[j] = 1500
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] < 0:
            enemyy[i] += enemyy_change[i]
            enemyx_change[i] = 1

        elif enemyx[i] > 736:
            enemyy[i] += enemyy_change[i]
            enemyx_change[i] = -1

        # collision
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            explo_sound = mixer.Sound('explosion.wav')
            explo_sound.play()
            bullety = 480
            bulletState = "ready"
            score_value += 1
            # print(f"your score is {score_value}")
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)

    # Bullet Movement
    if bulletState is "fire":
        fireBullet(bulletx, bullety)
        bullety -= bullety_change

    if bullety <= 0:
        bullety = 480
        bulletState = "ready"

    player(playerx, playery)
    show_score(textX, textY)

    pygame.display.update()
