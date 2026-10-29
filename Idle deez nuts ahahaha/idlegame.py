import pygame
import random
import sys
from button import Button
from player import Player


class IdleGame:
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Game Running Idle")
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    titlefont = pygame.font.SysFont(None, 64)
    exitfont = pygame.font.SysFont(None, 24)
    plantfont = pygame.font.SysFont(None, 12)

    showHoverSquare = True

    plantMenuState = 0


    gridSize = 32

    moneyTxt = font.render("$0", True, (200, 155, 23))

    background = pygame.image.load("idle deez nuts ahahaha/Minifantasy_FarmTileset.png")
    sunflower = pygame.image.load("idle deez nuts ahahaha/sunflower.png")

    #crops = pygame.transform.scale(crops, (gridSize, gridSize))

    gameState = "game"
    states = {}

    buttons = {
        "plantBtn": Button(screen=screen, x=100, y=100,
                          width=56, height=56, color=(255,255,255),
                          font=exitfont, txt="PLANT", txtColor=(0,0,0)),
        "plantCancelBtn" : Button(screen, x=100, y=100,
                      width=65, height=65, color=(6,6,6),
                      font=exitfont, txt="DON'T", txtColor=(255,255,255)),
        "sunflowerBtn" : Button(screen, x=195, y=100,
                      width=65, height=65, color=(125,125,125),
                      font=plantfont, txt="Sunflower: $5", txtColor=(255,255,255))

    }
    buttons["plantBtn"].SetHoverData(56 + 32, 56 + 32, (255,255,255), (0,0,0))
    buttons["plantCancelBtn"].SetHoverData(65 + 23, 65 + 23, (6,6,6), (255,255,255))
    buttons["plantCancelBtn"].active = False
    buttons["sunflowerBtn"].SetHoverData(65 + 23, 65 + 23, (125,125,125), (255,255,255))
    buttons["sunflowerBtn"].active = False


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
        self.screen.blit(self.moneyTxt, (self.screen.get_width()-self.moneyTxt.get_width() - 10,10))

        for k in self.buttons:
            if self.buttons[k].active:
                self.buttons[k].draw()
                self.UpdateBtnHover(self.buttons[k])
#ye
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

        mousePos = pygame.mouse.get_pos()
        gridX = (mousePos[0] // self.gridSize) * self.gridSize
        gridY = (mousePos[1] // self.gridSize) * self.gridSize
        if self.showHoverSquare:
            pygame.draw.rect(self.screen, (150, 150, 0), (gridX, gridY, self.gridSize, self.gridSize))

        pygame.display.flip()

    def OnClickPlantBtn(self):
        self.buttons["plantBtn"].active = False
        self.buttons["plantCancelBtn"].active = True
        self.buttons["sunflowerBtn"].active = True
    def OnClickPlantCancelBtn(self):
        self.buttons["plantCancelBtn"].active = False
        self.buttons["plantBtn"].active = True
        self.buttons["sunflowerBtn"].active = False
