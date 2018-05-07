import pygame
from map import *
import config
from function import *
from wall import *
from zombie import *
import play
import temp
import input_box
import pickle
clock = pygame.time.Clock()
is_finish = False
pygame.font.init()
myfont = pygame.font.SysFont("impact", 20)

class Button():
    def __init__(self, normal_image, selected_image, size):
        self.images = [normal_image, selected_image]
        self.image = normal_image
        self.size = size
        self.is_selected = False

    def select(self):
        self.is_selected = True
        self.image = self.images[1]

    def de_select(self):
        if self.is_selected:
            self.is_selected = False
            self.image = self.images[0]

    def show_button(self, screen, button_position, mouse_position):
        if self.is_selected == True:
            img = pygame.transform.scale(pygame.image.load(self.image), self.size)
            screen.blit(img, button_position)
            pygame.draw.rect(screen, config.RED, [button_position[0], button_position[1], self.size[0], self.size[1]],
                             2)
        else:
            if is_inside(button_position, self.size, mouse_position):
                img = pygame.transform.scale(pygame.image.load(self.images[1]), self.size)
                screen.blit(img, button_position)
            else:
                img = pygame.transform.scale(pygame.image.load(self.image), self.size)
                screen.blit(img, button_position)


def create_map(screen):
    MAP_SIZE = config.small_map_size
    MAPSIZE = 'SMALL'
    walls = Walls()
    list_zombie = []
    list_spider = []
    flag = [920,610,10,10]
    button_play = Button('Images/Icon/play.png', 'Images/Icon/playy1.png', [60, 60])
    button_save = Button('Images/Icon/save.png', 'Images/Icon/save1.png', [60, 60])
    flag_button = Button('Images/Object/flag2.png','Images/Object/flag.png',[60,60])
    button_canc = Button('Images/Icon/cancel.png', 'Images/Icon/cancel1.png', [60, 60])
    button_wall = Button('Images/Wall/wall.png', 'Images/Wall/wall2.png', [60, 60])
    button_spider = Button('Images/Spider/s1.png', 'Images/Spider/sabc.png', [60, 60])
    button_zombie = Button('Images/Zombie2/a0123.png', 'Images/Zombie2/z343.png', [60, 60])
    minus_button = Button('Images/Object/minus1.png','Images/Object/minus2.png',[20,20])
    plus_button = Button('Images/Object/plus1.png','Images/Object/plus2.png',[20,20])
    back_button = Button('Images/Object/back1.png','Images/Object/back2.png',[60,30])
    button_wall.select()
    status = 'NONE'
    config.gameExit = False
    spider_speed = 5
    zombie_speed = 5
    while not config.gameExit:
        bg = pygame.transform.scale(pygame.image.load('Images/bg/bg.jpg'), config.screen_size)
        screen.blit(bg, [0, 0])
        pygame.draw.rect(screen, config.GREEN,
                         [config.map_create_position[0], config.map_create_position[1], config.map_create_size[0],
                          config.map_create_size[1]], )
        # GET CAC SU KIEN ===========================================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position_down = pygame.mouse.get_pos()
                start = mouse_position_down
                if is_inside(config.wall_button_position, button_wall.size, mouse_position_down) and status != 'SAVE':
                    button_wall.select()
                    button_zombie.de_select()
                    button_spider.de_select()
                    flag_button.de_select()
                if is_inside(config.spider_button_position, button_spider.size,
                             mouse_position_down) and status != 'SAVE':
                    button_wall.de_select()
                    button_zombie.de_select()
                    button_spider.select()
                    flag_button.de_select()
                if is_inside(config.zombie_button_position, button_zombie.size,
                             mouse_position_down) and status != 'SAVE':
                    button_wall.de_select()
                    button_zombie.select()
                    button_spider.de_select()
                    flag_button.de_select()
                if is_inside([20,590],[60,30],mouse_position_down):
                    status = 'FINISH'
                if is_inside([20, 500], [60, 60], mouse_position_down) and status != 'SAVE':
                    status = 'PLAY'
                if is_inside([20, 420], [60, 60], mouse_position_down) and status != 'SAVE':
                    status = 'SAVE'
                if is_inside([20, 300], [60, 60], mouse_position_down) and status != 'SAVE':
                    button_wall.de_select()
                    button_zombie.de_select()
                    button_spider.de_select()
                    flag_button.select()
                if is_inside(config.map_create_position, config.map_create_size,
                             mouse_position_down) and status != 'SAVE':
                    if button_wall.is_selected:
                        status = 'ADD_WALL'
                    if button_zombie.is_selected:
                        status = 'ADD_ZOMBIE'
                    if button_spider.is_selected:
                        status = 'ADD_SPIDER'
                    if flag_button.is_selected:
                        flag = [mouse_position_down[0]-5,mouse_position_down[1]-5,10,10]
                if button_spider.is_selected and is_inside([90,135],[20,20],mouse_position_down):
                    if spider_speed <50:
                        spider_speed = spider_speed + 1
                if button_spider.is_selected and is_inside([90,185],[20,20],mouse_position_down):
                    if spider_speed>2:
                        spider_speed = spider_speed - 1
                if button_zombie.is_selected and is_inside([90,215],[20,20],mouse_position_down):
                    if zombie_speed < 50:
                        zombie_speed = zombie_speed+1
                if button_zombie.is_selected and is_inside([90,265],[20,20],mouse_position_down):
                    if zombie_speed>2:
                        zombie_speed = zombie_speed - 1
                if is_inside([20,20],[60,30],mouse_position_down):
                    if MAPSIZE == 'TINY':
                        MAP_SIZE = config.small_map_size
                        MAPSIZE = 'SMALL'
                    elif MAPSIZE == 'SMALL':
                        MAP_SIZE = config.medium_map_size
                        MAPSIZE = 'MEDIUM'
                    elif MAPSIZE == 'MEDIUM':
                        MAP_SIZE = config.large_map_size
                        MAPSIZE = 'LARGE'
                    else:
                        MAP_SIZE = config.tiny_map_size
                        MAPSIZE = 'TINY'
        # XU LY CAC SU KIEN ===========================================
        if button_spider.is_selected:
            pos = pygame.mouse.get_pos()
            plus_button.show_button(screen, [90, 135], pos)
            minus_button.show_button(screen, [90, 185], pos)
            label = myfont.render(str(spider_speed), 1, (0, 0, 0))
            screen.blit(label, (95, 163))
        if button_zombie.is_selected:
            pos = pygame.mouse.get_pos()
            plus_button.show_button(screen, [90, 215], pos)
            minus_button.show_button(screen, [90, 265], pos)
            label = myfont.render(str(zombie_speed), 1, (0, 0, 0))
            screen.blit(label, (95, 243))
        if status == 'ADD_WALL':
            finish = pygame.mouse.get_pos()
            finish_ = get_finish_position(start, finish)
            intsc = get_intersection(start, finish_)
            if intsc != False:
                wall = get_wall_from_two_point(start, intsc)
                walls.addWall(wall)
                status = 'NONE'
            elif event.type == pygame.MOUSEBUTTONUP:
                finish = pygame.mouse.get_pos()
                wall = get_wall_from_two_point(start, finish)
                walls.addWall(wall)
                status = 'NONE'
            else:
                pygame.draw.line(screen, config.RED, start, finish_, 2)
        # ----------------------------------------------------------------------------
        if status == 'ADD_SPIDER':
            finish = pygame.mouse.get_pos()
            C = [start[0], finish[1]]
            D = [finish[0], start[1]]
            intsc1 = get_intersection(start, C)
            intsc2 = get_intersection(start, D)
            if intsc1 != False and intsc2 != False:
                space = standardized_rect(start, [intsc2[0], intsc1[1]])
                list_spider.append(GroundZombie(spider_speed, space))
                status = 'NONE'
            elif intsc1 != False and intsc2 == False:
                space = standardized_rect(start, [D[0], intsc1[1]])
                list_spider.append(GroundZombie(spider_speed, space))
                status = 'NONE'
            elif intsc2 != False and intsc1 == False:
                space = standardized_rect(start, [intsc2[0], C[1]])
                list_spider.append(GroundZombie(spider_speed, space))
                status = 'NONE'
            else:
                list_intsc1 = []
                list_intsc2 = []
                for wall in walls.setWall:
                    intsc1 = is_intersect([wall.start.x, wall.start.y], [wall.end.x, wall.end.y], start, C)
                    if intsc1:
                        list_intsc1.append(intsc1)
                    intsc2 = is_intersect([wall.start.x, wall.start.y], [wall.end.x, wall.end.y], start, D)
                    if intsc2:
                        list_intsc2.append(intsc2)
                if len(list_intsc1) > 0 or len(list_intsc2) > 0:
                    dy_max = 10000
                    dx_max = 10000
                    Y = None
                    X = None
                    for intsc1_ in list_intsc1:
                        if distance(start, intsc1_) < dy_max:
                            dy_max = distance(start, intsc1_)
                            Y = intsc1_
                    for intsc2_ in list_intsc2:
                        if distance(start, intsc2_) < dx_max:
                            dx_max = distance(start, intsc2_)
                            X = intsc2_
                    if Y != None and X == None:
                        space = standardized_rect(start, [D[0], Y[1]])
                        list_spider.append(GroundZombie(spider_speed, space))
                    if Y == None and X != None:
                        space = standardized_rect(start, [X[0], C[1]])
                        list_spider.append(GroundZombie(spider_speed, space))
                    if Y != None and X != None:
                        space = standardized_rect(start, [X[0], Y[1]])
                        list_spider.append(GroundZombie(spider_speed, space))
                    status = 'NONE'
                else:
                    if event.type == pygame.MOUSEBUTTONUP:
                        space = standardized_rect(start, finish)
                        list_spider.append(GroundZombie(spider_speed, space))
                        status = 'NONE'
                    pygame.draw.rect(screen, config.RED, draw_standardized_rect(start, finish), 1)
        # ----------------------------------------------------------------------------
        if status == 'ADD_ZOMBIE':
            finish = pygame.mouse.get_pos()
            finish_ = get_finish_position(start, finish)
            intsc = get_intersection(start, finish_)
            if intsc != False:
                abd = abc(MAPSIZE,start,intsc)
                space = Rect(Point(start[0], start[1]), Point(abd[0], abd[1]))
                list_zombie.append(AZombie(zombie_speed, space))
                status = 'NONE'
            list_intsc = []
            for wall in walls.setWall:
                intsc = is_intersect([wall.start.x, wall.start.y], [wall.end.x, wall.end.y], start, finish_)
                if intsc:
                    list_intsc.append(intsc)
            if len(list_intsc) > 0:
                d_max = 10000
                intsc_ = None
                for intsc in list_intsc:
                    if distance(start, intsc) < d_max:
                        d_max = distance(start, intsc)
                        intsc_ = intsc
                abd = abc(MAPSIZE, start, intsc_)
                space = Rect(Point(start[0], start[1]), Point(abd[0], abd[1]))
                list_zombie.append(AZombie(zombie_speed, space))
                status = 'NONE'
            elif event.type == pygame.MOUSEBUTTONUP:
                abd = abc(MAPSIZE, start, finish_)
                space = Rect(Point(start[0], start[1]), Point(abd[0], abd[1]))
                list_zombie.append(AZombie(zombie_speed, space))
                status = 'NONE'
            else:
                pygame.draw.line(screen, config.RED, start, finish_, 1)
        # ----------------------------------------------------------------------------
        if status == 'PLAY':
            zombies = []
            spiders = []
            w = Walls()
            for zombie in list_zombie:
                A = Point(zombie.space.A.x, zombie.space.A.y)
                C = Point(zombie.space.C.x, zombie.space.C.y)
                space = Rect(A, C)
                z = AZombie(zombie.speed, space)
                zombies.append(z)
            for zombie in list_spider:
                A = Point(zombie.space.A.x, zombie.space.A.y)
                C = Point(zombie.space.C.x, zombie.space.C.y)
                space = Rect(A, C)
                z = GroundZombie(zombie.speed, space)
                spiders.append(z)
            for wall in walls.setWall:
                start_ = Point(wall.start.x, wall.start.y)
                end_ = Point(wall.end.x, wall.end.y)
                w_ = Wall(start_, end_)
                w.addWall(w_)
            flag_ = []
            i_ = (flag[0] - config.map_create_position[0]) * MAP_SIZE[0] / config.map_create_size[0]
            flag_.append(i_)
            i_ = (flag[1] - config.map_create_position[0]) * MAP_SIZE[0] / config.map_create_size[0]
            flag_.append(i_)
            i_ = flag[2] * MAP_SIZE[0] / config.map_create_size[0]
            flag_.append(i_)
            i_ = flag[3] * MAP_SIZE[0] / config.map_create_size[0]
            flag_.append(i_)
            obj = standardized_obj(zombies, spiders, w, MAP_SIZE)
            temp.gameExit = False
            play.play(obj[0], obj[1], obj[2], screen, MAP_SIZE,flag_)
            temp.gameExit = True
            status = 'NONE'

        # SHOW ======================================================
        for wall in walls.setWall:
            pygame.draw.line(screen, config.BLACK, [wall.start.x, wall.start.y], [wall.end.x, wall.end.y], 4)
        for zombie in list_zombie:
            pygame.draw.line(screen, config.BLUE, [zombie.space.A.x, zombie.space.A.y],
                             [zombie.space.C.x, zombie.space.C.y], 2)
            img = pygame.transform.scale(pygame.image.load('Images/Zombie2/z343.png'), [20, 20])
            screen.blit(img,
                        [(zombie.space.A.x + zombie.space.C.x) / 2 - 10,
                         (zombie.space.A.y + zombie.space.C.y) / 2 - 10])
        for spider in list_spider:
            pygame.draw.rect(screen, config.BLUE,
                             [spider.space.A.x, spider.space.A.y, spider.space.C.x - spider.space.A.x,
                              spider.space.C.y - spider.space.A.y], 2)
            img = pygame.transform.scale(pygame.image.load('Images/Spider/s1.png'), [20, 20])
            screen.blit(img,
                        [(spider.space.A.x + spider.space.C.x) / 2 - 10,
                         (spider.space.A.y + spider.space.C.y) / 2 - 10])
        mouse_position = pygame.mouse.get_pos()
        button_play.show_button(screen, [20, 500], mouse_position)
        button_save.show_button(screen, [20, 420], mouse_position)
        button_wall.show_button(screen, config.wall_button_position, mouse_position)
        button_spider.show_button(screen, config.spider_button_position, mouse_position)
        button_zombie.show_button(screen, config.zombie_button_position, mouse_position)
        flag_button.show_button(screen, [20, 300], mouse_position)
        pygame.draw.rect(screen,config.RED,flag,)
        pygame.draw.rect(screen, config.CYAN, [20,20,60,30],)
        back_button.show_button(screen,[20,590],mouse_position)
        label = myfont.render(MAPSIZE, 1, (0, 0, 0))
        screen.blit(label, (25, 30))
        print status
        if status == 'SAVE':
            file_ = input_box.ask(screen, 'File', [320, 40])
            if file_ == None:
                status = 'NONE'
            else:
                fo = "Maps/" + file_ + ".dat"
                zombies = []
                spiders = []
                w = Walls()
                for zombie in list_zombie:
                    A = Point(zombie.space.A.x, zombie.space.A.y)
                    C = Point(zombie.space.C.x, zombie.space.C.y)
                    space = Rect(A, C)
                    z = AZombie(zombie.speed, space)
                    zombies.append(z)
                for zombie in list_spider:
                    A = Point(zombie.space.A.x, zombie.space.A.y)
                    C = Point(zombie.space.C.x, zombie.space.C.y)
                    space = Rect(A, C)
                    z = GroundZombie(zombie.speed, space)
                    spiders.append(z)
                for wall in walls.setWall:
                    start_ = Point(wall.start.x, wall.start.y)
                    end_ = Point(wall.end.x, wall.end.y)
                    w_ = Wall(start_, end_)
                    w.addWall(w_)
                walls_, list_zombie_, list_spider_ = standardized_obj(zombies, spiders, w, MAP_SIZE)
                flag_ = []
                i_ = (flag[0] - config.map_create_position[0]) * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                i_ = (flag[1] - config.map_create_position[0]) * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                i_ = flag[2] * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                i_ = flag[3] * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                f = file(fo, 'wb+')
                pickle.dump(MAP_SIZE, f, pickle.HIGHEST_PROTOCOL)
                pickle.dump(flag_, f, pickle.HIGHEST_PROTOCOL)
                for zombie in list_zombie_:
                    pickle.dump(zombie, f, pickle.HIGHEST_PROTOCOL)
                for spider in list_spider_:
                    pickle.dump(spider, f, pickle.HIGHEST_PROTOCOL)
                pickle.dump(walls_, f, pickle.HIGHEST_PROTOCOL)
                status = 'NONE'

        if status == 'FINISH':
            file_ = input_box.ask(screen, 'File', [320, 40])
            if file_ == None:
                break
            else:
                fo = "Maps/" + file_ + ".dat"
                zombies = []
                spiders = []
                w = Walls()
                for zombie in list_zombie:
                    A = Point(zombie.space.A.x, zombie.space.A.y)
                    C = Point(zombie.space.C.x, zombie.space.C.y)
                    space = Rect(A, C)
                    z = AZombie(zombie.speed, space)
                    zombies.append(z)
                for zombie in list_spider:
                    A = Point(zombie.space.A.x, zombie.space.A.y)
                    C = Point(zombie.space.C.x, zombie.space.C.y)
                    space = Rect(A, C)
                    z = GroundZombie(zombie.speed, space)
                    spiders.append(z)
                for wall in walls.setWall:
                    start_ = Point(wall.start.x, wall.start.y)
                    end_ = Point(wall.end.x, wall.end.y)
                    w_ = Wall(start_, end_)
                    w.addWall(w_)
                walls_, list_zombie_, list_spider_ = standardized_obj(zombies, spiders, w, MAP_SIZE)
                flag_ = []
                i_ = (flag[0] - config.map_create_position[0]) * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                i_ = (flag[1] - config.map_create_position[0]) * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                i_ = flag[2] * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                i_ = flag[3] * MAP_SIZE[0] / config.map_create_size[0]
                flag_.append(i_)
                f = file(fo, 'wb+')
                pickle.dump(MAP_SIZE, f, pickle.HIGHEST_PROTOCOL)
                pickle.dump(flag_, f, pickle.HIGHEST_PROTOCOL)
                for zombie in list_zombie_:
                    pickle.dump(zombie, f, pickle.HIGHEST_PROTOCOL)
                for spider in list_spider_:
                    pickle.dump(spider, f, pickle.HIGHEST_PROTOCOL)
                pickle.dump(walls_, f, pickle.HIGHEST_PROTOCOL)
                break
        pygame.display.update()


def test():
    pygame.init()
    screen = pygame.display.set_mode(config.screen_size)
    create_map(screen)
