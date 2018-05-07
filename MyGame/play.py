import pygame
from player import *
from wall import *
from map import *
from zombie import *
import config
import temp
import random
import pickle


def return_random_images():
    bush_img = pygame.transform.scale(pygame.image.load('Images/bg/bush.png'), [16, 16])
    goccay1 = pygame.transform.scale(pygame.image.load('Images/bg/goccay1.png'), [25, 25])
    goccay2 = pygame.transform.scale(pygame.image.load('Images/bg/goccay2.png'), [30, 30])
    goccay3 = pygame.transform.scale(pygame.image.load('Images/bg/goccay3.png'), [20, 20])
    da1 = pygame.transform.scale(pygame.image.load('Images/bg/da.png'), [30, 30])
    a = random.randint(0, 7)
    if a == 0:
        return da1
    if a == 1 or a == 5 or a == 6:
        return bush_img
    if a == 2:
        return goccay1
    if a == 3:
        return goccay2
    if a == 4 or a == 7:
        return goccay3


def load_map(fo):
    f = file(fo, 'rb+')
    list_zombie = []
    list_spider = []
    list_ojb = []
    walls = None
    for i in xrange(100000):
        try:
            pl = pickle.load(f)
        except Exception:
            break
        list_ojb.append(pl)
    map_size = list_ojb.pop(0)
    flag = list_ojb.pop(0)
    for ojb in list_ojb:
        if isinstance(ojb, GroundZombie):
            list_spider.append(ojb)
        if isinstance(ojb, AZombie):
            list_zombie.append(ojb)
        if isinstance(ojb, Walls):
            walls = ojb
    return walls, list_zombie, list_spider, map_size, flag


def play(walls, list_zombie, list_spider, screen, map_size,flag):
    clock = pygame.time.Clock()
    number_of_bush = random.randint(map_size[0] * map_size[1] / 20000, map_size[0] * map_size[1] / 10000)
    list_bush = []
    list_imgb = []
    for i in xrange(number_of_bush):
        bush_pos = [random.randint(0, map_size[0] - 16), random.randint(0, map_size[1] - 16)]
        list_imgb.append(return_random_images())
        list_bush.append(bush_pos)
    water_img = pygame.transform.scale(pygame.image.load('Images/bg/water.png'), [50, 50])
    map = Map(map_size, walls)
    abc = map.showMap()
    player = Player(10, 2)
    gameExit = False
    screen_size = config.screen_size
    while not gameExit:
        # GET EVENT
        if is_inside([flag[0],flag[1]],[flag[2],flag[3]],player.position):
            #CHIEN THANG
            1
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                player.xstatus = "stop"
                player.ystatus = "stop"
            if event.type == pygame.QUIT:
                gameExit = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            break
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.ystatus = "up"
            if not (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                player.xstatus = "stop"
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.ystatus = "down"
            if not (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]):
                player.xstatus = "stop"
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.xstatus = "left"
            if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]):
                player.ystatus = "stop"
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.xstatus = "right"
            if not (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_DOWN] or keys[pygame.K_s]):
                player.ystatus = "stop"

        # CHON CAC VAT THE HIEN THI LEN MAN HINH
        list_water_ = []
        list_zombie_ = []
        list_spider_ = []
        abc_ = []
        list_b = []
        for zombie in list_zombie:
            d = distance(player.position, zombie.position)
            if d < 600:
                list_zombie_.append(zombie)

        for zombie in list_spider:
            d = distance(player.position, zombie.position)
            if d < 600:
                list_spider_.append(zombie)

        for w in abc:
            if distance(player.position, [w.x, w.y]) < 600:
                abc_.append(w)
        for i in xrange(0, len(list_bush)):
            if distance(player.position, list_bush[i]) < 600:
                list_b.append(i)
        if player.position[0] < 600:
            for i in range(int(player.position[1] / 30) - 12, int(player.position[1] / 30) + 12):
                for j in range(int(player.position[0] / 30) - 18, 0):
                    list_water_.append([30 * j, 30 * i])
        if player.position[1] < 450:
            for i in range(int(player.position[0] / 30) - 20, int(player.position[0] / 30) + 21):
                for j in range(int(player.position[1] / 30) - 15, 0):
                    list_water_.append([30 * i, 30 * j])
        if player.position[0] > map_size[0] - 600:
            for i in range(int(player.position[1] / 30) - 12, int(player.position[1] / 30) + 12):
                for j in range(int(map_size[0] / 30), int((player.position[0] + 600)/30)):
                    list_water_.append([30 * j, 30 * i])
        if player.position[1] > map_size[1] - 450:
            for i in range(int(player.position[0] / 30) - 20, int(player.position[0] / 30) + 21):
                for j in range(int(map_size[1] / 30), int((player.position[1] + 450)/30)):
                    list_water_.append([30 * i, 30 * j])

        # FIX POSITION
        screen.fill(config.GREEN)

        fix_playerPosition = [screen_size[0] / 2, screen_size[1] / 2]
        fix_wall = []
        fix_zombie = []
        fix_spider = []
        fix_bush = []
        fix_water = []
        fix_flag = [flag[0]+screen_size[0]/2-player.position[0],flag[1]+screen_size[1]/2-player.position[1],100,100]
        for i in list_water_:
            temp = [i[0] + screen_size[0] / 2 - player.position[0], i[1] + screen_size[1] / 2 - player.position[1]]
            fix_water.append(temp)
        # for i in list_b:
        #    temp = [list_bush[i][0] + screen_size[0] / 2 - player.position[0], list_bush[i][1] + screen_size[1] / 2 - player.position[1]]
        #    fix_bush.append(temp)
        for i in xrange(len(list_zombie_)):
            temp = [list_zombie_[i].position[0] + screen_size[0] / 2 - player.position[0],
                    list_zombie_[i].position[1] + screen_size[1] / 2 - player.position[1]]
            fix_zombie.append(temp)
        for i in xrange(len(list_spider_)):
            temp = [list_spider_[i].position[0] + screen_size[0] / 2 - player.position[0],
                    list_spider_[i].position[1] + screen_size[1] / 2 - player.position[1]]
            fix_spider.append(temp)
        for p in abc_:
            new_p = [p.x + screen_size[0] / 2 - player.position[0], p.y + screen_size[1] / 2 - player.position[1]]
            fix_wall.append(new_p)
        # SHOW OBJECT SHOW IN SCREEN
        pygame.draw.rect(screen, config.RED, fix_flag, )
        for i in list_b:
            screen.blit(list_imgb[i], [list_bush[i][0] + screen_size[0] / 2 - player.position[0],
                                       list_bush[i][1] + screen_size[1] / 2 - player.position[1]])
        for i in fix_water:
            screen.blit(water_img, [i[0], i[1]])
        for p in fix_wall:
            screen.blit(walls.showWall(), [p[0], p[1]])
        screen.blit(player.move(abc_, map_size), fix_playerPosition)
        for i in xrange(len(list_zombie_)):
            screen.blit(list_zombie_[i].move(abc_), fix_zombie[i])
        for i in xrange(len(list_spider_)):
            screen.blit(list_spider_[i].move(abc_), fix_spider[i])
        print flag
        pygame.display.update()
        clock.tick(20)
        for zombie in list_zombie_:
            if distance([player.position[0] + 30, player.position[1] + 30],
                        [zombie.position[0] + 50, zombie.position[1] + 50]) < 50:
                gameExit = True
        for zombie in list_spider_:
            if distance([player.position[0] + 30, player.position[1] + 30],
                        [zombie.position[0] + 30, zombie.position[1] + 30]) < 40:
                gameExit = True


# =====================TEST LOAD MAP=======================
def test():
    pygame.init()
    screen = pygame.display.set_mode(config.screen_size)
    walls, list_zombie, list_spider, map_size, flag = load_map("Maps/maptest.dat")
    play(walls, list_zombie, list_spider, screen, map_size,flag)
