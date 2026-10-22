import pygame
from gameobject import GameObject
from framehandler import GetFrames

class Player(GameObject):
    def __init__(self, screens, x, y, width, height, speed, color, bnsSpeed,image, bnsSize):
        super().__init__()
        self.screen = screens
        self.leftoriginalImage = image

        self.rightoriginalImage = pygame.transform.flip(self.leftoriginalImage,True,False)

        self.rect = pygame.Rect(x,y,width,height)
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.bnsSpeed = bnsSpeed
        self.isBnsSpeed = False
        self.bnsSpeedRemain = 0
        self.bnsSpeedTime = 300

        self.bnsSize = bnsSize
        self.isBnsSize = False
        self.bnsSizeRemain = 0
        self.bnsSizeTime = 300

        self.frameY = 0
        self.frameX = 0
        self.animSpeed = 5
        self.animTimer = 0

        self.movement = False

        self.leftframes = GetFrames(self.leftoriginalImage, self.width, self.height)
        self.rightframes = GetFrames(self.rightoriginalImage, self.width, self.height)
        self.currentframe = 0
        self.image = self.leftframes[0]
        self.image = pygame.transform.scale(self.image, (self.width * 2, self.height * 2))


    def update(self):
        self.rect.x += self.velocity[0] * self.speed * self.bnsSpeed
        self.rect.y += self.velocity[1] * self.speed


        if self.velocity[0] != 0:
            self.movement = True
        else:
            self.movement = False

        if self.movement:
            self.animTimer += 1
            if self.animTimer >= self.animSpeed:
                self.animTimer = 0
                self.currentframe += 1
                if self.currentframe >= len(self.leftframes):
                    self.currentframe = 0
                if self.velocity[0] > 0:
                    self.image = self.rightframes[self.currentframe]
                elif self.velocity[0] < 0:
                    self.image = self.leftframes[self.currentframe]

        self.image = pygame.transform.scale(self.image, (self.width * self.bnsSize, self.height * self.bnsSize))
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x >= self.screen.get_width() - self.width:
            self.rect.x = self.screen.get_width() - self.width

        if self.isBnsSpeed:
            self.bnsSpeedRemain -= 1
            if self.bnsSpeedRemain == 0:
                self.isBnsSpeed = False
                self.bnsSpeed = 1

        if self.isBnsSize:
            self.bnsSizeRemain -= 1
            self.rect.width = self.width * self.bnsSize
            self.rect.height = self.height * self.bnsSize
            if self.bnsSizeRemain == 0:
                self.isBnsSize = False
                self.bnsSize = 2
                self.rect.y = 400


    def applyBnsSpeed(self):
        self.isBnsSpeed = True
        self.bnsSpeedRemain = self.bnsSpeedTime
        self.bnsSpeed = 2

    def applyBnsSize(self):
        self.isBnsSize = True
        self.bnsSizeRemain = self.bnsSizeTime
        self.bnsSize = 4
