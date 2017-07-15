import pygame as pg
import paddle

class Ball():
    def __init__(self, screen):
        self.ballColor = pg.Color("White")
        self.ballRadius = 15
        self.screen = screen
        self.velocityX = 3
        self.velocityY = 3
        self.ballX = 100
        self.ballY = 120
        self.backgroundColor = pg.Color(140, 166, 209)

        #Bounds
        

    def drawBall(self, position):
        self.ballX = position[0]
        self.ballY = position[1]

        pg.draw.circle(self.screen, self.ballColor, position, self.ballRadius)

    def moveBall(self, paddlePos):
        #Colliding
        ballLeftBound = self.ballX - self.ballRadius
        ballRightBound = self.ballX + self.ballRadius
        ballUpBound = self.ballY - self.ballRadius
        ballDownBound = self.ballY + self.ballRadius


        if(ballRightBound > 740):
            self.velocityX = self.velocityX * -1

        if(ballLeftBound < 10):
            self.velocityX = self.velocityX * -1

        if(705 > ballDownBound > 701 and ballLeftBound >= paddlePos[0] and ballRightBound <= paddlePos[1]):
            self.velocityY = self.velocityY * -1

        if(ballUpBound < 12):
            self.velocityY = self.velocityY * -1

        pg.draw.circle(self.screen, self.backgroundColor, (self.ballX, self.ballY), self.ballRadius)

        self.ballX = self.ballX + self.velocityX
        self.ballY = self.ballY + self.velocityY

        pg.draw.circle(self.screen, self.ballColor, (self.ballX, self.ballY), self.ballRadius)