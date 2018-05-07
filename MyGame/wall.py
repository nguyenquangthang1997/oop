import pygame
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
class Rect():
    def __init__(self,A,C):             #A---------------------------
        self.A = A                      #|                          |
        self.C = C                      #|                          |
    def isInside(self,P):               #|--------------------------C
        return (self.A.x - P.x)(self.C.x - P.x) < 0 and (self.A.y - P.y)(self.C.y - P.y) < 0
class Wall():
    def __init__(self,A,B):
        self.start = A
        self.end = B
    def getVector(self):
        if self.start.x == self.end.x:
            return "x"
        if self.start.y == self.end.y:
            return "y"
class Walls():
    def __init__(self):
        self.setWall = []
        self.image = "Images/Wall/wall.png"
    def addWall(self,wall):
        self.setWall.append(wall)
    def showWall(self):
        image = pygame.transform.scale(pygame.image.load(self.image), [55, 55])
        return image

