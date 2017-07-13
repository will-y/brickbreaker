import pygame as pg
import sys
import paddle

class Main():
    def __init__(self):
        self.windowHeight = 750
        self.windowWidth = 750
        self.backgroundColor = pg.Color(140, 166, 209)
        self.borderWidth = 10
        self.borderColor = pg.Color(91, 98, 109)
        self.screen = pg.display.set_mode((self.windowWidth, self.windowHeight))
        pg.display.set_caption("Brick Breaker")
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill(self.backgroundColor)
        self.clock = pg.time.Clock()
    
    def runGame(self):
        paddleInstance = paddle.Paddle(self.screen)
        paddleInstance.drawPaddle(300, 700)
        pg.draw.rect(self.screen, self.borderColor, (0, 0, self.windowWidth, self.windowHeight), self.borderWidth)
        while True:
            self.clock.tick(10)
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()
            pg.display.update()


def main():
    mainClass = Main()
    mainClass.runGame()

main()