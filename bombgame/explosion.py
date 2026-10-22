import pygame
from gameobject import GameObject
from framehandler import GetFrames

class Explosion(GameObject):
    def __init__(self, screens, x, y, width, height, id, image):
        super().__init__()
        self.screen = screens
        self.originalImage = image
        self.image = self.originalImage.subsurface(0,0,width,height)
        self.rect = pygame.Rect(x,y,width,height)
        self.width = width
        self.height = height
        self.id = id
        self.frameX = 0
        self.frameY = 0
        self.animSpeed = 5
        self.animTimer = 0
        self.animDoneCallback = None
        self.size = 2

        self.frames = GetFrames(self.originalImage, self.width, self.height)
        self.currentframe = 0

    def update(self):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
        self.animTimer += 1
        if self.animTimer >= self.animSpeed:
            self.animTimer = 0
            self.currentframe += 1
            if self.currentframe >= len(self.frames):
                self.currentframe = 0
                self.animDoneCallback(self)
            self.image = self.frames[self.currentframe]
            self.image = pygame.transform.scale(self.image, (self.width * self.size, self.height * self.size))
        # self.image = self.originalImage.subsurface(0 + self.frameX * self.width, 0 + self.frameY * self.height,self.width,self.height)
        # self.image = pygame.transform.scale(self.image, (self.width * 2, self.height * 2))

    def SetSize(self, size):
        self.size = size