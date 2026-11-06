import pygame

class Plant:
    planted = 0

    screen = None
    rect = pygame.Rect(0, 0, 0, 0)
    x = 0
    y = 0
    width = 0
    height = 0
    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    plantGrowthTxt = font.render("0", True, (200, 155, 23))
    stage = 0
    growthSpeed = 0
    growthTimer = 0
    maxGrowth= False
    harvestMoney = 0
    cost = 0

    def __init__(self, screen, x, y, width, height, image):
        self.screen = screen
        self.x = x
        self.defaultX = x
        self.y = y
        self.defaultY = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.image = image
        if self.image is not None:
            self.image = pygame.transform.scale(self.image,
                                                   (self.image.get_width() * 4, self.image.get_height() * 4))

    def Planting(self):
        while self.planted == 0:
            mousePos = pygame.mouse.get_pos()
            self.x = mousePos[0]
            self.y = mousePos[1]
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.planted = 1

    def drawData(self):
        self.screen.blit(self.plantGrowthTxt, (self.x,self.y))

    def UpdateGrowth(self):
        self.growthTimer += 1
        if self.growthTimer > self.growthSpeed:
            self.growthTimer = 0
            self.stage += 1
            if self.stage >= 5:
                self.maxGrowth = True
                self.plantGrowthTxt = self.font.render("MAX", True, (200, 155, 23))
            else:
                self.plantGrowthTxt = self.font.render(f"{self.stage}", True, (200, 155, 23))