import pygame as pg
import sys

class Paddle():
    def __init__(self, screen, width, height):
        self.paddleWidth = 100
        self.paddleHeight = 15
        self.paddleColor = pg.Color("green")
        self.backgroundColor = pg.Color(0, 0, 0)
        self.screen = screen
        self.paddleX = 0
        self.screenWidth = width
        self.screenHeight = height

    def drawPaddle(self, x):
        self.paddleRect = pg.Rect((x, 700, self.paddleWidth, self.paddleHeight))
        pg.draw.rect(self.screen, self.backgroundColor, (self.paddleX - 3, 700 - 3, self.paddleWidth + 6, self.paddleHeight + 6))
        pg.draw.rect(self.screen, self.paddleColor, self.paddleRect, 5)

        self.paddleX = x

    def movePaddle(self, direction):
        if(direction == "left" and self.paddleX > 12):
            self.drawPaddle(self.paddleX - 6)
        elif(direction == "right" and self.paddleX < self.screenWidth - 10 -self.paddleWidth):
            self.drawPaddle(self.paddleX + 6)

    def getPos(self):
        return self.paddleX, self.paddleX + self.paddleWidth, self.paddleX + self.paddleWidth/2

    def getRect(self):
        return self.paddleRect