import pygame as pg
import sys
import paddle
import ball
import bricks

class Main():
    def __init__(self):
        self.windowHeight = 750
        self.windowWidth = 750
        self.backgroundColor = pg.Color(0, 0, 0)
        self.borderWidth = 10
        self.borderColor = pg.Color(91, 98, 109)
        self.screen = pg.display.set_mode((self.windowWidth, self.windowHeight))
        pg.display.set_caption("Brick Breaker")
        self.background = pg.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.screen.fill(self.backgroundColor)
        self.clock = pg.time.Clock()
    
    def runGame(self):
        paddleInstance = paddle.Paddle(self.screen, self.windowWidth, self.windowHeight)
        paddleInstance.drawPaddle(300)

        ballInstance = ball.Ball(self.screen, self.windowWidth, self.windowHeight)
        ballInstance.drawBall((350, 690))

        brickInstance = bricks.Bricks(self.screen, ballInstance)
        brickInstance.drawBricks()

        pg.draw.rect(self.screen, self.borderColor, (0, 0, self.windowWidth, self.windowHeight), self.borderWidth)
        
        ballFree = False

        while True:
            self.clock.tick(60)
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()

            key = pg.key.get_pressed()
            if key[pg.K_RIGHT]:
                paddleInstance.movePaddle("right")
                if(ballInstance.stuckToPaddle):
                    ballInstance.moveBall(paddleInstance.getPos(), paddleInstance.getRect(), "right")
            if(key[pg.K_LEFT]):
                paddleInstance.movePaddle("left")
                if(ballInstance.stuckToPaddle):
                    ballInstance.moveBall(paddleInstance.getPos(), paddleInstance.getRect(), "left")
            if(not ballFree):
                if(key[pg.K_SPACE]):
                    ballInstance.freeBall()
                    ballFree = True

            brickInstance.checkBallHit(ballInstance.getCollider())

            if(not ballInstance.stuckToPaddle):
                ballInstance.moveBall(paddleInstance.getPos(), paddleInstance.getRect(), "")

            pg.display.update()

def main():
    mainClass = Main()
    mainClass.runGame()

main()