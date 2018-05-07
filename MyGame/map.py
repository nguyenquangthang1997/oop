from function import*
from wall import*
class Map():
    def __init__(self,mapSize,walls):
        self.mapSize = mapSize
        self.walls = walls
    def showMap(self):
        x = []
        for wall in self.walls.setWall:
            x = x + returnSetWall(wall)
        return x
