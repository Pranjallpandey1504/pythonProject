import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# background
background = pygame.image.load('back.png')

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png.'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# bullet

# ready-you can't see bullet on screen
# fire -the bullet is currently moving

bulletImg = pygame.image.load('bullet.png.')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state= "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score:" + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return  False

# game loop
running = True
while running:

    # RGB- red,green,blue
    screen.fill((0, 0, 0))
    # background img
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 playerX_change = -3
             if event.key == pygame.K_RIGHT:
                 playerX_change = 3
             if event.key == pygame.K_SPACE:
                 bulletX= playerX
                 fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
    # checking for boundaries of spaceship
    playerX += playerX_change

    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX=736

    # enemy movement
    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i]<= 0:
           enemyX_change[i] = 1
           enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
           enemyX_change[i] = -1
           enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
           bulletY = 480
           bullet_state = "ready"
           score_value += 1
           enemyX[i] = random.randint(0, 735)
           enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY=480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()