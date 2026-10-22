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

    showHoverSquare = True

    plantMenuState = 0


    gridSize = 32

    background = pygame.image.load("idle deez nuts ahahaha/Minifantasy_FarmTileset.png")

    #crops = pygame.transform.scale(crops, (gridSize, gridSize))

    gameState = "game"
    states = {}

    plantBtnColor = (200, 200, 200)
    plantBtnTxtColor = (0, 0, 0)
    plantBtnHoverColor = (255, 255, 255)
    plantBtnHoverTxtColor = (0, 0, 0)

    plantBtnWidth = 56
    plantBtnHeight = 56
    plantBtnX = 100
    plantBtnY = 100

    plantBtn = Button(screen, plantBtnX, plantBtnY,
                          plantBtnWidth, plantBtnHeight, plantBtnColor,
                          exitfont, "PLANT", plantBtnTxtColor)
    plantBtn.SetHoverData(plantBtnWidth + 32, plantBtnHeight + 32, plantBtnHoverColor, plantBtnHoverTxtColor)

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
        self.plantBtn.callback = self.OnClickPlantBtn

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
        if self.plantMenuState == 0:
            self.plantBtn.draw()
            self.UpdateBtnHover(self.plantBtn)

#ye
        #self.screen.blit(self.crops, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.plantMenuState == 0:
                    self.UpdateBtnCallback(self.plantBtn)

        mousePos = pygame.mouse.get_pos()
        gridX = (mousePos[0] // self.gridSize) * self.gridSize
        gridY = (mousePos[1] // self.gridSize) * self.gridSize
        if self.showHoverSquare:
            pygame.draw.rect(self.screen, (150, 150, 0), (gridX, gridY, self.gridSize, self.gridSize))



        pygame.display.flip()

    def OnClickPlantBtn(self):
        self.plantMenuState = 1

