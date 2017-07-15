import pygame as pg
import random
import sys

class Bricks():
    def __init__(self, screen, ballInstance):
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
        self.collided = False
        self.ball = ballInstance

    def drawBricks(self):
        for i in range(self.bricksPerRow):
            rowArray = []
            for j in range(self.bricksPerCol):
                rand = random.randint(0, len(self.colorArray)-1)
                rect = pg.Rect(self.brickStartingX + (self.brickWidth + self.brickPadding) * i, self.brickStartingY + (self.brickHeight + self.brickPadding) * j, self.brickWidth, self.brickHeight)
                pg.draw.rect(self.screen, self.colorArray[rand], rect, 3)
                rowArray.append(rect)
            self.brickArray.append(rowArray)

    def checkBallHit(self, ballCollider):
        for i in range(self.bricksPerRow):
            for j in range(self.bricksPerCol):
                if(not self.brickArray[i][j] == None):
                    if (self.brickArray[i][j].colliderect(ballCollider)):
                        self.removeBrick(i, j)
                        self.ball.changeY()
                    else:
                        self.collided = False

    def removeBrick(self, i, j):
        pg.draw.rect(self.screen, pg.Color('black'), (self.brickStartingX + (self.brickWidth + self.brickPadding) * i, self.brickStartingY + (self.brickHeight + self.brickPadding) * j, self.brickWidth, self.brickHeight), 3)
        self.brickArray[i][j] = None
    
    def getArray(self):
        return self.brickArray

    def getCollide(self):
        return self.collided