import pygame as pg

class Paddle():
    def __init__(self, screen):
        self.paddleWidth = 150
        self.paddleHeight = 25
        self.paddleColor = pg.Color(250, 0, 255)
        self.screen = screen

    def drawPaddle(self, x, y):
        pg.draw.rect(self.screen, self.paddleColor, (x, y, self.paddleWidth, self.paddleHeight))