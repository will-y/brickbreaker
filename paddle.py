import pygame as pg
import sys

class Paddle():
    def __init__(self, screen):
        self.paddleWidth = 150
        self.paddleHeight = 25
        self.paddleColor = pg.Color(250, 0, 255)
        self.backgroundColor = pg.Color(140, 166, 209)
        self.screen = screen
        self.paddleX = 0
        

    def drawPaddle(self, x):
        pg.draw.rect(self.screen, self.backgroundColor, (self.paddleX, 700, self.paddleWidth, self.paddleHeight))
        pg.draw.rect(self.screen, self.paddleColor, (x, 700, self.paddleWidth, self.paddleHeight))

        self.paddleX = x

    def movePaddle(self, direction):
        if(direction == "left" and self.paddleX > 10):
            self.drawPaddle(self.paddleX - 4)
        elif(direction == "right" and self.paddleX < 590):
            self.drawPaddle(self.paddleX + 4)

    def getPos(self):
        print(self.paddleX)
        sys.stdout.flush()
        return self.paddleX, self.paddleX + self.paddleWidth