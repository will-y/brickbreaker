import pygame as pg
import random
import sys

class Bricks():
    def __init__(self, screen):
        self.brickStartingY = 30
        self.brickStartingX = 50
        self.bricksPerRow = 11
        self.bricksPerCol = 10
        self.brickWidth = 50
        self.brickHeight = 20
        self.brickPadding = 10
        self.brickBorder = 3
        self.screen = screen
        self.colorArray = (pg.Color('blue'), pg.Color('red'), pg.Color('green'), pg.Color('purple'), pg.Color('orange'), pg.Color('yellow'))
        self.brickArray = []

    def drawBricks(self):
        for i in range(self.bricksPerRow):
            rowArray = []
            for j in range(self.bricksPerCol):
                rand = random.randint(0, len(self.colorArray)-1)
                pg.draw.rect(self.screen, self.colorArray[rand], (self.brickStartingX + (self.brickWidth + self.brickPadding) * i, self.brickStartingY + (self.brickHeight + self.brickPadding) * j, self.brickWidth, self.brickHeight), 3)
                rowArray.append(1)
            self.brickArray.append(rowArray)
        print(self.brickArray)
        sys.stdout.flush()