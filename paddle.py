import pygame as pg
import sys

class Paddle():
    def __init__(self, screen, width, height):
        self.paddleWidth = 100
        self.paddleHeight = 15
        self.paddleColor = pg.Color(250, 0, 255)
        self.backgroundColor = pg.Color(140, 166, 209)
        self.screen = screen
        self.paddleX = 0
        self.screenWidth = width
        self.screenHeight = height

    def drawPaddle(self, x):
        self.paddleRect = pg.Rect((x, 700, self.paddleWidth, self.paddleHeight))
        pg.draw.rect(self.screen, self.backgroundColor, (self.paddleX, 700, self.paddleWidth, self.paddleHeight))
        pg.draw.rect(self.screen, self.paddleColor, self.paddleRect)

        self.paddleX = x

    def movePaddle(self, direction):
        if(direction == "left" and self.paddleX > 10):
            self.drawPaddle(self.paddleX - 6)
        elif(direction == "right" and self.paddleX < self.screenWidth - 10 -self.paddleWidth):
            self.drawPaddle(self.paddleX + 6)

    def getPos(self):
        return self.paddleX, self.paddleX + self.paddleWidth, self.paddleX + self.paddleWidth/2

    def getRect(self):
        return self.paddleRect