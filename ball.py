import pygame as pg
import paddle

class Ball():
    def __init__(self, screen, width, height):
        self.ballColor = pg.Color("White")
        self.ballRadius = 10
        self.screen = screen
        self.screenWidth = width
        self.screenHeight = height
        self.velocityX = 3
        self.velocityY = 3
        self.ballX = 100
        self.ballY = 120
        self.backgroundColor = pg.Color(140, 166, 209)
        self.ballCollider = pg.Rect((self.ballX - self.ballRadius, self.ballY - self.ballRadius), (self.ballRadius * 2, self.ballRadius * 2))
        self.negativeX = False
        self.centerZone = 20

        #Bounds
        

    def drawBall(self, position):
        self.ballX = position[0]
        self.ballY = position[1]

        pg.draw.circle(self.screen, self.ballColor, position, self.ballRadius)

    def moveBall(self, paddlePos, paddleRect):
        #Colliding
        ballLeftBound = self.ballX - self.ballRadius
        ballRightBound = self.ballX + self.ballRadius
        ballUpBound = self.ballY - self.ballRadius
        ballDownBound = self.ballY + self.ballRadius


        if(ballRightBound > self.screenWidth - 10):
            self.velocityX = self.velocityX * -1
            self.switchBool(self.negativeX)

        if(ballLeftBound < 10):
            self.velocityX = self.velocityX * -1
            self.switchBool(self.negativeX)

        if(ballDownBound > 701 and self.ballCollider.colliderect(paddleRect)):
            self.velocityY = self.velocityY * -1
            if(paddlePos[0] <= self.ballX <= paddlePos[2] - self.centerZone/2):
                if(not self.negativeX):
                    self.velocityX = self.velocityX * -1
                    self.switchBool(self.negativeX)
            elif(paddlePos[2] + self.centerZone/2):
                if(self.negativeX):
                    self.velocityX = self.velocityX * -1
                    self.switchBool(self.negativeX)

        if(ballUpBound < 12):
            self.velocityY = self.velocityY * -1

        pg.draw.circle(self.screen, self.backgroundColor, (self.ballX, self.ballY), self.ballRadius)

        self.ballX = self.ballX + self.velocityX
        self.ballY = self.ballY + self.velocityY

        self.ballCollider = pg.Rect((self.ballX - self.ballRadius, self.ballY - self.ballRadius), (self.ballRadius * 2, self.ballRadius * 2))

        pg.draw.circle(self.screen, self.ballColor, (self.ballX, self.ballY), self.ballRadius)

    def switchBool(self, boolean):
        if(boolean):
            boolean = False
        else:
            boolean = True