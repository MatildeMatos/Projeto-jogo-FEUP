from random import randrange as rnd
from itertools import cycle
from random import choice
from PIL import  Image
import pygame
import time


pygame.init()
speed = 3



# extracting game items and characters form the resource.png image.
player_init = Image.open("zombiegood2.png").convert("RGBA")
player_init = player_init.resize(list(map(lambda x:x//2 , player_init.size)))

player_frame_1 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_1 = player_frame_1.resize(list(map(lambda x:x//2 , player_frame_1.size)))

player_frame_2 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_2 = player_frame_2.resize(list(map(lambda x:x//2 , player_frame_2.size)))

player_frame_3 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_3 = player_frame_3.resize(list(map(lambda x:x//2 , player_frame_3.size)))

player_frame_31 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_31 = player_frame_31.resize(list(map(lambda x:x//2 , player_frame_31.size)))

player_frame_4 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_4 = player_frame_4.resize(list(map(lambda x:x//2 , player_frame_4.size)))

player_frame_5 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_5 = player_frame_5.resize(list(map(lambda x:x//2 , player_frame_5.size)))

player_frame_6 = Image.open("zombiegood2.png").convert("RGBA")
player_frame_6 = player_frame_6.resize(list(map(lambda x:x//2 , player_frame_6.size)))

bgimg = Image.open("fundo.png").convert("RGBA")
bgimg = bgimg.resize(list(map(lambda x:x//2 , bgimg.size)))

size = (1200,50)

ground1 = Image.open("estradafinal.png").convert("RGBA")
ground1 = ground1.resize(size)

ground2 = Image.open("estradafinal.png").convert("RGBA")
ground2 = ground2.resize(size)

obstacle1 = Image.open("pneu.png").convert("RGBA")
obstacle1 = obstacle1.resize(list(map(lambda x:x//2 -25 , obstacle1.size)))

obstacle2 = Image.open("pneu.png").convert("RGBA")
obstacle2 = obstacle2.resize(list(map(lambda x:x//2 -25, obstacle2.size)))

obstacle3 = Image.open("carro.png").convert("RGBA")
obstacle3 = obstacle3.resize(list(map(lambda x:x//2 -2 , obstacle3.size)))

obstacle4 = Image.open("carro.png").convert("RGBA")
obstacle4 = obstacle4.resize(list(map(lambda x:x//2 -2, obstacle4.size)))

obstacle5 = Image.open("buraco.png").convert("RGBA")
obstacle5 = obstacle5.resize(list(map(lambda x:x//1 , obstacle5.size)))

obstacle5 = Image.open("buraco.png").convert("RGBA")
obstacle5 = obstacle5.resize(list(map(lambda x:x//1 -30, obstacle5.size)))

obstacle6 = Image.open("buraco.png").convert("RGBA")
obstacle6 = obstacle6.resize(list(map(lambda x:x//1 -20, obstacle6.size)))


speed_identifier = lambda x: 2 if x >= 30 else 8 if x < 8 else 5
cust_speed = speed_identifier(speed)
running = cycle([player_frame_3]*cust_speed+[player_frame_31]*cust_speed)
crouch = cycle([player_frame_5]*cust_speed+ [player_frame_6]*cust_speed)
crouch_scope = [player_frame_5]+[player_frame_6]
obstacles = [obstacle1,obstacle2, obstacle3,obstacle4,obstacle5,obstacle6]


gameDisplay = pygame.display.set_mode((600,200))
pygame.display.set_caption('T-Rex Runner')
clock = pygame.time.Clock()
state = player_frame_1
crashed = False
lock = False
bg = (0, 150)
bg1 = (600,150)
start = False
height = 110
jumping = False
slow_motion = False
c1 = (0, 0)
c2 = (380, 0)
c3 = (790,0)
obs1 = (rnd(600, 600+500), 130)
obs2 = (rnd(600+100+500, 1200+500), 130)
obs3 = (rnd(1700, 2000), 130)
obast1 = choice(obstacles)
if obast1 in [obstacle4, obstacle5, obstacle6]:obs1 = (obs1[0], 115)
obast2 = choice(obstacles)
if obast2 in [obstacle4, obstacle5, obstacle6]:obs2 = (obs2[0], 115)
obast3 = choice(obstacles)
if obast3 in [obstacle4, obstacle5, obstacle6]:obs3 = (obs3[0], 115)

while not crashed:
    gameDisplay.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type==pygame.KEYDOWN:
            start = True
            if event.key == pygame.K_DOWN:
                slow_motion = True
                state = crouch
            if event.key == pygame.K_UP:
                if height >= 110:jumping = True
        if event.type==pygame.KEYUP:
            slow_motion = False
            if event.key == pygame.K_DOWN:
                state = running
    player = state if type(state) != cycle else next(state)

    gameDisplay.blit(pygame.image.fromstring(bgimg.tobytes(), bgimg.size, 'RGBA'), c1)
    gameDisplay.blit(pygame.image.fromstring(bgimg.tobytes(), bgimg.size, 'RGBA'), c2)
    gameDisplay.blit(pygame.image.fromstring(bgimg.tobytes(), bgimg.size, 'RGBA'), c3)


    c1 = (c1[0]-1, c1[1])
    c2 = (c2[0]-1, c2[1])
    c3 = (c3[0]-1, c3[1])
    if c1[0]<= -400:
        c1 = (640, c1[1])
    if c2[0]<= -400:
        c2 = (700, c2[1])
    if c3[0]<= -400:
        c3 = (700, c3[1])
    gameDisplay.blit(pygame.image.fromstring(ground1.tobytes(), ground1.size, 'RGBA'), bg)
    gameDisplay.blit(pygame.image.fromstring(ground1.tobytes(), ground1.size, 'RGBA'), bg1)

    gameDisplay.blit(pygame.image.fromstring(ground2.tobytes(), ground2.size, 'RGBA'), bg)
    gameDisplay.blit(pygame.image.fromstring(ground2.tobytes(), ground2.size, 'RGBA'), bg1)

    if jumping:
        if height>=110-100:
            height -= 4
        if height <= 110-100:
            jumping = False
    if height<110 and not jumping:
        if slow_motion == True:
            height += 1.5
        else:height += 3
    player = gameDisplay.blit(pygame.image.fromstring(player.tobytes(), player.size, 'RGBA'), (5,height))
    gameDisplay.blit(pygame.image.fromstring(obast1.tobytes(), obast1.size, 'RGBA'), obs1)
    gameDisplay.blit(pygame.image.fromstring(obast2.tobytes(), obast2.size, 'RGBA'), obs2)
    gameDisplay.blit(pygame.image.fromstring(obast3.tobytes(), obast3.size, 'RGBA'), obs3)
    if obs1[0]<=-50:
        obs1 = (rnd(600, 600+500), 130)
        obast1 = choice(obstacles)
        if obast1 in [obstacle4, obstacle5, obstacle6]:obs1 = (obs1[0], 115)
    if obs2[0]<=-50:
        obs2 = (rnd(600+100+500, 1200+500), 130)
        obast2 = choice(obstacles)
        if obast2 in [obstacle4, obstacle5, obstacle6]:obs2 = (obs2[0], 115)
    if obs3[0]<=-50:
        obs3 = (rnd(1700, 2000), 130) 
        obast3 = choice(obstacles) 
        if obast3 in [obstacle4, obstacle5, obstacle6]:obs3 = (obs3[0], 115)
    player_stading_cub = (5, height, 5+43,height+46)
    if height< 100:
        start=True
    if start:
        obs1 = (obs1[0]-speed, obs1[1])
        obs2 = (obs2[0]-speed, obs2[1])
        obs3 = (obs3[0]-speed, obs3[1])
        obs1_cub = (obs1[0], obs1[1], obs1[0]+obast1.size[0],obs1[1]+obast1.size[1])
        obs2_cub = (obs2[0], obs2[1], obs2[0]+obast2.size[0],obs2[1]+obast2.size[1])
        obs3_cub = (obs3[0], obs3[1], obs3[0]+obast3.size[0],obs3[1]+obast3.size[1])
        if not lock:
            bg = (bg[0]-speed, bg[1])
            if bg[0]<=-(600):
                lock = 1
        if -bg[0]>=600 and lock:
            bg1 = (bg1[0]-speed, bg1[1])
            bg = (bg[0]-speed, bg[1])
            if -bg1[0]>=600:bg = (600,150)
        if -bg1[0]>=600 and lock:
            bg = (bg[0]-speed, bg1[1])
            bg1 = (bg1[0]-speed, bg1[1])
            if -bg[0]>=600:bg1 = (600,150)

        if obs1_cub[0]<=player_stading_cub[2]-10<=obs1_cub[2] and obs1_cub[1]<=player_stading_cub[3]-10<=obs1_cub[3]-5:
            start=False
            state = player_frame_4
        if obs2_cub[0]<=player_stading_cub[2]-10<=obs2_cub[2] and obs2_cub[1]<=player_stading_cub[3]-10<=obs2_cub[3]-5:
            start=False
            state = player_frame_4
        if obs3_cub[0]<=player_stading_cub[2]-10<=obs3_cub[2] and obs3_cub[1]<=player_stading_cub[3]-10<=obs3_cub[3]-5:
            start=False
            state = player_frame_4
    pygame.display.update()
    clock.tick(120)