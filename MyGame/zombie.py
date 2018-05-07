from random import *
from function import *


class Zombie():
    def __init__(self, speed, space):
        self.speed = speed
        self.space = space  # KHONG GIAN HOAT DONG CUA ZOMBIE (HINH CHU NHAT)


class FlyZombie(Zombie):
    def __init__(self, speed, space):
        Zombie.__init__(self, speed, space)

        self.ani = ["Images/Zombie/zombie1.png", "Images/Zombie/zombie2.png", "Images/Zombie/zombie3.png",
                    "Images/Zombie/zombie4.png", "Images/Zombie/zombie5.png"]
        self.ani_ = 0
        self.size = [130, 60]
        self.position = [(self.space.A.x + self.space.C.x) / 2, (self.space.A.y + self.space.C.y) / 2]
        self.fposition = [(self.space.A.x + self.space.C.x) / 2, (self.space.A.y + self.space.C.y) / 2]

    def nextAni(self):
        self.ani_ = (self.ani_ + 1)
        if self.ani_ == 15:
            self.ani_ = 0
        if self.ani_ < 3:
            self.size = [160, 90]
            return self.ani[0]
        if self.ani_ < 6:
            self.size = [140, 140]
            return self.ani[1]
        if self.ani_ < 9:
            self.size = [140, 90]
            return self.ani[2]
        if self.ani_ < 12:
            self.size = [150, 100]
            return self.ani[3]
        if self.ani_ < 15:
            self.size = [120, 100]
            return self.ani[4]

    def move(self):
        if self.position == self.fposition:
            self.fposition = [randint(self.space.A.x, self.space.C.x), randint(self.space.A.y, self.space.C.y)]
            image = pygame.transform.scale(pygame.image.load(self.nextAni()), self.size)
            image = pygame.transform.rotate(image, rotateAngle(self.position, self.fposition))
        else:
            image = pygame.transform.scale(pygame.image.load(self.nextAni()), self.size)
            image = pygame.transform.rotate(image, rotateAngle(self.position, self.fposition))
            self.position = nextZombiePosition(self.position, self.fposition, self.speed)
        return image


class GroundZombie(Zombie):
    def __init__(self, speed, space):
        Zombie.__init__(self, speed, space)

        self.ani = ["Images/Spider/s1.png", "Images/Spider/s2.png", "Images/Spider/s3.png", "Images/Spider/s4.png",
                    "Images/Spider/s5.png", "Images/Spider/s6.png", "Images/Spider/s7.png"]
        self.ani_ = 0
        self.position = [self.space.A.x, self.space.A.y]
        self.fposition = [self.space.A.x, self.space.A.y]
        self.size = [30,30]

    def nextAni(self):
        self.ani_ = (self.ani_ + 1)
        if self.ani_ == 21:
            self.ani_ = 0
        if self.ani_ < 3:
            return self.ani[0]
        if self.ani_ < 6:
            return self.ani[1]
        if self.ani_ < 9:
            return self.ani[2]
        if self.ani_ < 12:
            return self.ani[3]
        if self.ani_ < 15:
            return self.ani[4]
        if self.ani_ < 18:
            return self.ani[5]
        if self.ani_ < 21:
            return self.ani[6]

    def move(self,walls):
        if self.position == self.fposition:
            self.fposition = [randint(self.space.A.x, self.space.C.x), randint(self.space.A.y, self.space.C.y)]
            image = pygame.transform.scale(pygame.image.load(self.nextAni()), [30, 30])
            image = pygame.transform.rotate(image, rotateAngle(self.position, self.fposition) - 180)
        else:
            image = pygame.transform.scale(pygame.image.load(self.nextAni()), [30, 30])
            image = pygame.transform.rotate(image, rotateAngle(self.position, self.fposition) - 180)
            last_position = [self.position[0],self.position[1]]
            self.position = nextZombiePosition(self.position, self.fposition, self.speed)
            for wall in walls:
                if self.position[0] + 30 > wall.x and self.position[0] < wall.x + 55 and self.position[
                    1] + 30 > wall.y and self.position[1] < wall.y + 55:
                    self.position = last_position
                    self.fposition = [randint(self.space.A.x, self.space.C.x), randint(self.space.A.y, self.space.C.y)]
                    break

        return image


class AZombie(Zombie):
    def __init__(self, speed, space):
        Zombie.__init__(self, speed, space)

        self.ani = ["Images/Zombie2/a0.png", "Images/Zombie2/a1.png", "Images/Zombie2/a2.png", "Images/Zombie2/a3.png",
                    "Images/Zombie2/a4.png", "Images/Zombie2/a5.png", "Images/Zombie2/a6.png", "Images/Zombie2/a7.png"]
        self.ani_ = 0
        self.position = [self.space.A.x, self.space.A.y]
        self.fposition = [self.space.A.x, self.space.A.y]
        self.size = [100, 100]

    def nextAni(self):
        self.ani_ = (self.ani_ + 1)
        if self.ani_ == 24:
            self.ani_ = 0
        if self.ani_ < 3:
            return self.ani[0]
        if self.ani_ < 6:
            return self.ani[1]
        if self.ani_ < 9:
            return self.ani[2]
        if self.ani_ < 12:
            return self.ani[3]
        if self.ani_ < 15:
            return self.ani[4]
        if self.ani_ < 18:
            return self.ani[5]
        if self.ani_ < 21:
            return self.ani[6]
        if self.ani_ < 24:
            return self.ani[7]

    def move(self,walls):
        image = pygame.transform.scale(pygame.image.load(self.nextAni()), self.size)
        image = pygame.transform.rotate(image, rotateAngle(self.position, self.fposition) - 90)
        self.position = nextZombiePosition(self.position, self.fposition, self.speed)
        if self.position == self.fposition:
            if self.fposition == [self.space.A.x,self.space.A.y]:
                self.fposition = [self.space.C.x,self.space.C.y]
            else:
                self.fposition = [self.space.A.x,self.space.A.y]
        else:
            self.position = nextZombiePosition(self.position, self.fposition, self.speed)
        return image