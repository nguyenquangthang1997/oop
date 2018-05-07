import pygame
import math
class Player():
    def __init__(self, v, a):
        self.maxSpeed = v
        self.xspeed = 0.0
        self.yspeed = 0.0
        self.acceleration = a
        self.xstatus = "stop"
        self.ystatus = "stop"
        self.img = "Images/Player/stop.png"
        self.ani = ["Images/Player/move2.png", "Images/Player/move3.png", "Images/Player/move4.png",
                    "Images/Player/move1.png"]
        self.ani_ = 0
        self.isAlive = True
        self.position = [0,0]
        self.angle = 0

    def setStauts(stt):
        self.status = stt

    def updateXSpeed(self):
        if self.xstatus == "stop":
            if self.xspeed > 0:
                self.xspeed = self.xspeed - self.acceleration
                if self.xspeed < 0:
                    self.xspeed = 0
            if self.xspeed < 0:
                self.xspeed = self.xspeed + self.acceleration
                if self.xspeed > 0:
                    self.xspeed = 0
        if self.xstatus == "right":
            self.xspeed = self.xspeed + 2 * self.acceleration
            if self.xspeed > self.maxSpeed:
                self.xspeed = self.maxSpeed
        if self.xstatus == "left":
            self.xspeed = self.xspeed - 2 * self.acceleration
            if self.xspeed < -self.maxSpeed:
                self.xspeed = -self.maxSpeed

    def updateYSpeed(self):
        if self.ystatus == "stop":
            if self.yspeed > 0:
                self.yspeed = self.yspeed - self.acceleration
                if self.yspeed < 0:
                    self.yspeed = 0
            if self.yspeed < 0:
                self.yspeed = self.yspeed + self.acceleration
                if self.yspeed > 0:
                    self.yspeed = 0
        if self.ystatus == "down":
            self.yspeed = self.yspeed + 2 * self.acceleration
            if self.yspeed > self.maxSpeed:
                self.yspeed = self.maxSpeed
        if self.ystatus == "up":
            self.yspeed = self.yspeed - 2 * self.acceleration
            if self.yspeed < -self.maxSpeed:
                self.yspeed = -self.maxSpeed

    def nextAni(self):
        self.ani_ = (self.ani_ + 1)
        if self.ani_ == 12:
            self.ani_ = 0
        if self.ani_ < 3:
            return self.ani[0]
        if self.ani_ < 6:
            return self.ani[1]
        if self.ani_ < 9:
            return self.ani[2]
        if self.ani_ < 12:
            return self.ani[3]

    def move(self, walls,map_size):
        self.updateXSpeed()
        self.updateYSpeed()
        if not (self.xspeed == 0 and self.yspeed == 0):
            self.position[0] = self.position[0] + math.fabs(self.xspeed) * self.xspeed / math.sqrt(
                self.xspeed * self.xspeed + self.yspeed * self.yspeed)
            self.position[1] = self.position[1] + math.fabs(self.yspeed) * self.yspeed / math.sqrt(
                self.xspeed * self.xspeed + self.yspeed * self.yspeed)
            for wall in walls:
                if self.position[0] + 60 > wall.x and self.position[0] < wall.x + 50 and self.position[
                    1] + 60 > wall.y and self.position[1] < wall.y + 50:
                    self.position[0] = self.position[0] - math.fabs(self.xspeed) * self.xspeed / math.sqrt(
                        self.xspeed * self.xspeed + self.yspeed * self.yspeed)
                    self.position[1] = self.position[1] - math.fabs(self.yspeed) * self.yspeed / math.sqrt(
                        self.xspeed * self.xspeed + self.yspeed * self.yspeed)
            if self.position[0]<0 or self.position[0]> map_size[0] or self.position[1]<0 or self.position[1]>map_size[1]:
                self.position[0] = self.position[0] - math.fabs(self.xspeed) * self.xspeed / math.sqrt(
                    self.xspeed * self.xspeed + self.yspeed * self.yspeed)
                self.position[1] = self.position[1] - math.fabs(self.yspeed) * self.yspeed / math.sqrt(
                    self.xspeed * self.xspeed + self.yspeed * self.yspeed)
                image = pygame.transform.scale(pygame.image.load(self.img), [60, 36])
                image = pygame.transform.rotate(image, self.angle)
                return image

            image = pygame.transform.scale(pygame.image.load(self.nextAni()), [60, 60])
            a = -math.asin(
                self.xspeed / math.sqrt(self.xspeed * self.xspeed + self.yspeed * self.yspeed)) * 180 / math.pi
            if self.yspeed <= 0:
                self.angle = a
            else:
                if a <= 0:
                    self.angle = -180 - a
                else:
                    self.angle = 180 - a
            image = pygame.transform.rotate(image, self.angle)
            return image

        else:
            image = pygame.transform.scale(pygame.image.load(self.img), [60, 36])
            image = pygame.transform.rotate(image, self.angle)
            return image
