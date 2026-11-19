import pygame
from idlebutton import Button
from plant import Plant


class IdleGame:
    screen = pygame.display.set_mode((1280, 960))
    pygame.display.set_caption("Game Running Idle")
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    titlefont = pygame.font.SysFont(None, 64)
    exitfont = pygame.font.SysFont(None, 24)
    plantfont = pygame.font.SysFont(None, 12)

    showHoverSquare = True
    mousePos = (0,0)
    gridX = 0
    gridY = 0

    plantMenuState = 0


    gridSize = 64

    moneyTxt = font.render("$0", True, (200, 155, 23))
    money = 0



    background = pygame.image.load("idle deez nuts ahahaha/Minifantasy_FarmTileset.png")
    sunflower = pygame.image.load("idle deez nuts ahahaha/sunflower.png")
    radish = pygame.image.load("idle deez nuts ahahaha/radish.png")
    radishes = [pygame.image.load(f"idle deez nuts ahahaha/radish_{i}.png") for i in range(5)]




    gameState = "game"
    states = {}

    buttons = {
        "plantBtn": Button(screen=screen, x=100, y=64,
                          width=56, height=56, color=(255,255,255),
                          font=exitfont, txt="PLANT", txtColor=(0,0,0)),
        "plantCancelBtn" : Button(screen, x=100, y=64,
                      width=65, height=65, color=(6,6,6),
                      font=exitfont, txt="DON'T", txtColor=(255,255,255)),
        "sunflowerBtn" : Button(screen, x=195, y=64,
                      width=65, height=65, color=(125,125,125),
                      font=plantfont, txt="Sunflower: $5", txtColor=(255,255,255), alignment=1, btnImage=sunflower),
        "radishBtn": Button(screen, x=290, y=64,
                               width=65, height=65, color=(125, 125, 125),
                               font=plantfont, txt="Radish: $10", txtColor=(255, 255, 255), alignment=1,
                               btnImage=radish)

    }
    buttons["plantBtn"].SetHoverData(56 + 32, 56 + 32, (255,255,255), (0,0,0))
    buttons["plantCancelBtn"].SetHoverData(65 + 23, 65 + 23, (6,6,6), (255,255,255))
    buttons["plantCancelBtn"].active = False
    buttons["sunflowerBtn"].SetHoverData(65 + 23, 65 + 23, (125,125,125), (255,255,255))
    buttons["sunflowerBtn"].active = False
    buttons["radishBtn"].SetHoverData(65 + 23, 65 + 23, (125, 125, 125), (255, 255, 255))
    buttons["radishBtn"].active = False

    currentSelectPlant = None
    plantGrid = {}

    def Initialize(self):
        self.states["menu"] = self.RunMenu
        self.states["game"] = self.RunGame
        self.states["pause"] = self.RunPause
        self.states["credits"] = self.RunCredits

        # self.menuStartBtn.callback = self.StartGame
        # self.pauseStartBtn.callback = self.PauseGame
        # self.exitStartBtn.callback = self.QuitGame
        # self.resumeStartBtn.callback = self.StartGame
        # self.creditStartBtn.callback = self.StartCredits
        # self.backCredBtn.callback = self.PauseGame
        self.buttons["plantBtn"].callback = self.OnClickPlantBtn
        self.buttons["plantCancelBtn"].callback = self.OnClickPlantCancelBtn
        self.buttons["sunflowerBtn"].callback = self.OnClickSunflowerBtn
        self.buttons["radishBtn"].callback = self.OnClickRadishBtn
        self.radishes = self.ScalePlants(self.radishes)


    def StartGame(self):
        self.gameState = "game"

    def PauseGame(self):
        self.gameState = "pause"

    def StartCredits(self):
        self.gameState = "credits"

    def QuitGame(self):
        pygame.quit()

    def UpdateBtnHover(self, btn):
        mouse = pygame.mouse.get_pos()
        if btn.rect.collidepoint(mouse):
            btn.OnHoverEnter()
            self.showHoverSquare = False

        else:
            btn.OnHoverExit()
            self.showHoverSquare = True


    def UpdateBtnCallback(self, btn):
        mouse = pygame.mouse.get_pos()
        if btn.rect.collidepoint(mouse):
            btn.callback()
            return True
        else:
            return False

    def RunPause(self):
        self.screen.fill((30, 30, 255))
        self.exitStartBtn.draw()
        self.resumeStartBtn.draw()
        self.creditStartBtn.draw()

        self.UpdateBtnHover(self.exitStartBtn)
        self.UpdateBtnHover(self.resumeStartBtn)
        self.UpdateBtnHover(self.creditStartBtn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.UpdateBtnCallback(self.exitStartBtn)
                self.UpdateBtnCallback(self.resumeStartBtn)
                self.UpdateBtnCallback(self.creditStartBtn)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.StartGame()

    def RunMenu(self):
        pass
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         self.UpdateBtnCallback(self.menuStartBtn)
        #
        # self.UpdateBtnHover(self.menuStartBtn)
        #
        # self.screen.fill(self.bgColor)
        # self.screen.blit(self.titleText, ((self.screen.get_width()  / 2) - (self.titleText.get_width() / 2) , 96))
        # self.menuStartBtn.draw()

    def RunCredits(self):

        self.UpdateBtnHover(self.backCredBtn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.UpdateBtnCallback(self.backCredBtn)

        self.screen.fill(self.bgColor)
        self.screen.blit(self.titleText, (20, 80))
        self.screen.blit(self.thanksText, (20, 166))
        self.screen.blit(self.supporterText, (20, 206))
        self.screen.blit(self.referenceText, (20, 246))
        self.screen.blit(self.viewerText, (20, 286))
        self.backCredBtn.draw()



    def RunGame(self):
        self.screen.fill((111,164,48))
        self.moneyTxt = self.font.render(f"${self.money}", True, (200, 155, 23))
        self.screen.blit(self.moneyTxt, (self.screen.get_width()-self.moneyTxt.get_width() - 10,10))

        for k in self.buttons:
            if self.buttons[k].active:
                self.buttons[k].draw()
                self.UpdateBtnHover(self.buttons[k])

        #self.screen.blit(self.crops, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for k in self.buttons:
                    if self.buttons[k].active:
                        clicked = self.UpdateBtnCallback(self.buttons[k])
                        if clicked:
                            break
                if self.currentSelectPlant is not None and self.currentSelectPlant.planted == 0 and self.showHoverSquare:
                    self.currentSelectPlant.planted = 1
                    self.currentSelectPlant.x = self.gridX
                    self.currentSelectPlant.y = self.gridY
                    self.plantGrid[(self.gridX, self.gridY)] = self.currentSelectPlant
                    self.money -= self.currentSelectPlant.cost
                    self.currentSelectPlant = None
                if self.currentSelectPlant is None and (self.gridX, self.gridY) in self.plantGrid:
                    if self.plantGrid[(self.gridX, self.gridY)].maxGrowth:
                        self.money += self.plantGrid[(self.gridX, self.gridY)].harvestMoney
                        del self.plantGrid[(self.gridX, self.gridY)]



        self.mousePos = pygame.mouse.get_pos()
        self.gridX = (self.mousePos[0] // self.gridSize) * self.gridSize
        self.gridY = (self.mousePos[1] // self.gridSize) * self.gridSize
        if self.showHoverSquare:
            pygame.draw.rect(self.screen, (150, 150, 0), (self.gridX, self.gridY, self.gridSize, self.gridSize))
        if self.currentSelectPlant is not None and self.currentSelectPlant.planted == 0:
            self.screen.blit(self.currentSelectPlant.images[0], (self.gridX+20, self.gridY +10))
        for pos in self.plantGrid:
            planted = self.plantGrid[pos]
            self.screen.blit(planted.images[planted.stage], (planted.x+20, planted.y+10))
            # planted.drawData()
            planted.UpdateGrowth()
        pygame.display.flip()

    def OnClickPlantBtn(self):
        self.buttons["plantBtn"].active = False
        self.buttons["plantCancelBtn"].active = True
        self.buttons["sunflowerBtn"].active = True
        self.buttons["radishBtn"].active = True
    def OnClickPlantCancelBtn(self):
        self.buttons["plantCancelBtn"].active = False
        self.buttons["plantBtn"].active = True
        self.buttons["sunflowerBtn"].active = False
        self.buttons["radishBtn"].active = False
    def OnClickSunflowerBtn(self):
        self.currentSelectPlant = Plant(self.screen, self.mousePos[0], self.mousePos[1], 7, 11, self.sunflower)
        self.currentSelectPlant.growthSpeed = 50
        self.currentSelectPlant.harvestMoney = 10
        self.currentSelectPlant.cost = 5
    def OnClickRadishBtn(self):
        self.currentSelectPlant = Plant(self.screen, self.mousePos[0], self.mousePos[1], 7, 11, self.radishes)
        self.currentSelectPlant.growthSpeed = 75
        self.currentSelectPlant.harvestMoney = 20
        self.currentSelectPlant.cost = 10
    def ScalePlants(self, images):
        for i in range(0, len(images)):
            if images[i] is not None:
                images[i] = pygame.transform.scale(images[i],
                                                   (images[i].get_width() * 4, images[i].get_height() * 4))
        return images
