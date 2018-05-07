from wall import *
from math import *
from wall import *
import config

def returnSetWall(wall):  # WALL
    vector = wall.getVector()
    w = []
    if vector == "x":
        x = wall.start.x - (wall.start.x) % 50
        for i in range(wall.start.y, wall.end.y):
            if i % 50 == 0:
                A = Point(x, i)
                w.append(A)
    if vector == "y":
        y = wall.start.y - (wall.start.y) % 50
        for i in range(wall.start.x, wall.end.x):
            if i % 50 == 0:
                A = Point(i, y)
                w.append(A)
    return w


def nextZombiePosition(current_position, finish_position, speed):  # DUNG DE XAC DINH DUONG DI CHUYEN CUA ZOMBIE
    dx = finish_position[0] - current_position[0]
    dy = finish_position[1] - current_position[1]
    try:
        x_new = current_position[0] + dx * speed / sqrt(dx * dx + dy * dy)
        y_new = current_position[1] + dy * speed / sqrt(dx * dx + dy * dy)
    except Exception:
        return current_position
    if (((x_new - finish_position[0]) * (x_new - current_position[0]) > 0) or
            ((y_new - finish_position[1]) * (y_new - current_position[1]) > 0)):
        x = finish_position[0]
        y = finish_position[1]
    else:
        x = int(x_new)
        y = int(y_new)
    return [x, y]


def rotateAngle(A, B):
    xspeed = B[0] - A[0]
    yspeed = B[1] - A[1]
    try:
        a = -asin(xspeed / sqrt(xspeed * xspeed + yspeed * yspeed)) * 180 / pi
    except Exception:
        return 0
    if yspeed <= 0:
        return a + 180
    else:
        if a <= 0:
            return - a
        else:
            return 360 - a


def isAlive(player, zombie):
    if (player.position[0] + 60 > zombie.position[0]) and (
                player.position[0] < zombie.position[0] + zombie.size[0]) and (
                    player.position[1] + 60 > zombie.position[1]) and (
                player.position[1] < zombie.position[1] + zombie.size[1]):
        return False
    return True


def is_inside(start, size, point):
    return ((point[0] - start[0]) * (point[0] - start[0] - size[0]) < 0) and (
        (point[1] - start[1]) * (point[1] - start[1] - size[1]) < 0)


def get_wall_from_two_point(A, B):
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dx) > abs(dy):
        C = [B[0], A[1]]
        return Wall(Point(A[0], A[1]), Point(C[0], C[1]))
    else:
        C = [A[0], B[1]]
        return Wall(Point(A[0], A[1]), Point(C[0], C[1]))


def get_finish_position(A, B):
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dx) > abs(dy):
        C = [B[0], A[1]]
    else:
        C = [A[0], B[1]]
    return C


def standardized_rect(A, B):
    C = Point(min(A[0], B[0]), min(A[1], B[1]))
    D = Point(max(A[0], B[0]), max(A[1], B[1]))
    return Rect(C, D)


def draw_standardized_rect(A, B):
    C = Point(min(A[0], B[0]), min(A[1], B[1]))
    D = Point(max(A[0], B[0]), max(A[1], B[1]))
    return C.x, C.y, D.x - C.x, D.y - C.y


def standardized_obj(list_zombie_, list_spider_, walls_, map_size):
    list_zombie = list_zombie_
    list_spider = list_spider_
    walls = walls_
    for zombie in list_zombie:
        print zombie.space.A.x,zombie.space.A.y,zombie.space.C.x,zombie.space.C.y
        zombie.space.A.x = (zombie.space.A.x - config.map_create_position[0]) * map_size[0] / config.map_create_size[0]
        zombie.space.A.y = (zombie.space.A.y - config.map_create_position[1]) * map_size[1] / config.map_create_size[1]
        zombie.space.C.x = (zombie.space.C.x - config.map_create_position[0]) * map_size[0] / config.map_create_size[0]
        zombie.space.C.y = (zombie.space.C.y - config.map_create_position[1]) * map_size[1] / config.map_create_size[1]
        zombie.position = [zombie.space.A.x,zombie.space.A.y]
        zombie.fposition = [zombie.space.A.x, zombie.space.A.y]
        print zombie.space.A.x, zombie.space.A.y, zombie.space.C.x, zombie.space.C.y
    for zombie in list_spider:
        zombie.space.A.x = (zombie.space.A.x - config.map_create_position[0]) * map_size[0] / config.map_create_size[0]
        zombie.space.A.y = (zombie.space.A.y - config.map_create_position[1]) * map_size[1] / config.map_create_size[1]
        zombie.space.C.x = (zombie.space.C.x - config.map_create_position[0]) * map_size[0] / config.map_create_size[0]
        zombie.space.C.y = (zombie.space.C.y - config.map_create_position[1]) * map_size[1] / config.map_create_size[1]
        zombie.position = [zombie.space.A.x, zombie.space.A.y]
        zombie.fposition = [zombie.space.A.x, zombie.space.A.y]
    for wall in walls.setWall:
        wall.start.x = (wall.start.x - config.map_create_position[0]) * map_size[0] / config.map_create_size[0]
        wall.start.y = (wall.start.y - config.map_create_position[1]) * map_size[1] / config.map_create_size[1]
        wall.end.x = (wall.end.x - config.map_create_position[0]) * map_size[0] / config.map_create_size[0]
        wall.end.y = (wall.end.y - config.map_create_position[1]) * map_size[1] / config.map_create_size[1]
    return walls, list_zombie, list_spider
def distance(A,B):
    return sqrt((A[0]-B[0])*(A[0]-B[0])+(A[1]-B[1])*(A[1]-B[1]))
def is_intersect(A,B,C,D):
    dAB = [B[0]-A[0],B[1]-A[1]]
    dCD = [D[0]-C[0],D[1]-C[1]]
    if dAB[0]*dCD[0]+dAB[1]*dCD[1] == 0:
        if dAB[0] == 0:
            if ((C[1] - A[1])*(C[1]- B[1])<0) and ((A[0] - C[0])*(A[0] - D[0])<0):
                return A[0],C[1]
            else:
                return False
        if dAB[1] == 0:
            if ((C[0] - A[0]) * (C[0] - B[0]) < 0) and ((A[1] - C[1]) * (A[1] - D[1]) < 0):
                return C[0],A[1]
            else:
                return False
    else:
        return False

def get_intersection(start,finish_):
    intsc = is_intersect(start, finish_, config.map_create_position, [config.map_create_position[0],
                                                                      config.map_create_position[1] +
                                                                      config.map_create_size[1]])
    if intsc != False:
       return intsc
    intsc = is_intersect(start, finish_, config.map_create_position,
                         [config.map_create_position[0] + config.map_create_size[0],
                          config.map_create_position[1]])
    if intsc != False:
       return intsc
    intsc = is_intersect(start, finish_, [config.map_create_position[0] + config.map_create_size[0],
                                          config.map_create_position[1] + config.map_create_size[1]],
                         [config.map_create_position[0] + config.map_create_size[0],
                          config.map_create_position[1]])
    if intsc != False:
       return intsc
    intsc = is_intersect(start, finish_, [config.map_create_position[0] + config.map_create_size[0],
                                          config.map_create_position[1] + config.map_create_size[1]],
                         [config.map_create_position[0],
                          config.map_create_position[1] +
                          config.map_create_size[1]])
    if intsc != False:
       return intsc
    return False
def abc(mapsize,start,finish):
    temp = [finish[0],finish[1]]
    if start[0]<finish[0] or start[1] < finish[1]:
        if start[0] == finish[0]:
            if mapsize == 'TINY':
                temp[1] = finish[1] - 40
            elif mapsize == 'SMALL':
                temp[1] = finish[1] - 24
            elif mapsize == 'MEDIUM':
                temp[1] = finish[1] - 16
            else:
                temp[1] = finish[1] - 12
        else:
            if mapsize == 'TINY':
                temp[0] = finish[0] - 40
            elif mapsize == 'SMALL':
                temp[0] = finish[0] - 24
            elif mapsize == 'MEDIUM':
                temp[0] = finish[0] - 16
            else:
                temp[0] = finish[0] - 12
    else:
        if start[0] == finish[0]:
            if mapsize == 'TINY':
                temp[1] = finish[1] + 10
            elif mapsize == 'SMALL':
                temp[1] = finish[1] + 6
            elif mapsize == 'MEDIUM':
                temp[1] = finish[1] + 4
            else:
                temp[1] = finish[1] + 3
        else:
            if mapsize == 'TINY':
                temp[0] = finish[0] + 10
            elif mapsize == 'SMALL':
                temp[0] = finish[0] + 6
            elif mapsize == 'MEDIUM':
                temp[0] = finish[0] + 4
            else:
                temp[0] = finish[0] + 3
    return temp