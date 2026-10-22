import pygame
from player import Player
from bomb import Projectile
from button import Button
from explosion import Explosion
import random
import sys

class Game:
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("My Pygame Window")
    clock = pygame.time.Clock()

    pygame.font.init()
    font = pygame.font.SysFont(None, 48)
    titlefont = pygame.font.SysFont(None, 64)
    exitfont = pygame.font.SysFont(None, 24)

    scoreText = font.render("Score: 0", True, (100, 100, 100))
    HPText = font.render("HP: 10", True, (200, 255, 175))
    titleText = titlefont.render("D3FUZ3 MY B0MB5 >:D", True, (128, 128, 128))
    thanksText = font.render("Thank you to:", True, (255, 255, 255))
    supporterText = exitfont.render("Michael Wozniak and Dillon Russo for helping make this game,", True, (128, 255, 128))
    referenceText = exitfont.render("Toby Fox, Shutterstock, Jackson Games, and Dreamstimes for reference art,", True, (255, 128, 128))
    viewerText = exitfont.render("And Thank you to You for playing this game!", True, (128, 128, 255))
    spdBnsText = font.render(f"Bonus Speed Remaining: {0}", True, (128, 128, 128))
    sizeBnsText = font.render(f"Bonus Size Remaining: {0}", True, (128, 128, 128))

    bombImage = pygame.image.load("bombgame/piskelregularbomb.png")
    playerImage = pygame.image.load("bombgame/piskelmainchara.png")
    spdBombImage = pygame.image.load("bombgame/piskelspeedbomb.png")
    explosionImage = pygame.image.load("bombgame/piskelregularexplode.png")
    spdExplosionImage = pygame.image.load("bombgame/piskelspeedexplode.png")
    sizeBombImage = pygame.image.load("bombgame/piskelsizeupbomb.png")
    sizeExplosionImage = pygame.image.load("bombgame/piskelsizeupexplode.png")

    menuBtnColor = (200,200,200)
    menuTxtColor = (150,150,150)
    menuHoverColor = (255,255,255)
    menuHoverTextCol = (0, 0, 0)

    menuBtnWidth = 300
    menuBtnHeight = 150
    menuBtnX = (screen.get_width() / 2)
    menuBtnY = (screen.get_height() / 2)

    pauseBtnColor = (200, 200, 200)
    pauseTxtColor = (0, 0, 0)
    pauseHoverColor = (255, 255, 255)
    pauseHoverTextCol = (0, 0, 0)

    pauseBtnWidth = 56
    pauseBtnHeight = 56
    pauseBtnX = 32
    pauseBtnY = 32

    exitBtnColor = (255, 10, 50)
    exitTxtColor = (0, 0, 0)
    exitHoverColor = (255, 255, 255)
    exitHoverTextCol = (0, 0, 0)

    exitBtnWidth = 250
    exitBtnHeight = 90
    exitBtnX = (screen.get_width() / 2)
    exitBtnY = (screen.get_height() - exitBtnHeight)

    resumeBtnColor = (50, 255, 10)
    resumeTxtColor = (0, 0, 0)
    resumeHoverColor = (250, 250, 250)
    resumeHoverTextCol = (0, 0, 0)

    resumeBtnWidth = 250
    resumeBtnHeight = 90
    resumeBtnX = (screen.get_width() / 2)
    resumeBtnY = resumeBtnHeight

    creditBtnColor = (35, 50, 225)
    creditTxtColor = (0, 0, 0)
    creditHoverColor = (250, 250, 250)
    creditHoverTextCol = (0, 0, 0)

    creditBtnWidth = 250
    creditBtnHeight = 90
    creditBtnX = (screen.get_width() / 2)
    creditBtnY = (screen.get_height() / 2)


    backCredBtnColor = (200, 200, 200)
    backCredTxtColor = (0, 0, 0)
    backCredHoverColor = (255, 255, 255)
    backCredHoverTextCol = (0, 0, 0)

    backCredBtnWidth = 56
    backCredBtnHeight = 56
    backCredBtnX = 32
    backCredBtnY = 32

    menuStartBtn = Button(screen, menuBtnX, menuBtnY,
                          menuBtnWidth, menuBtnHeight, menuBtnColor,
                          font, "START", menuTxtColor)
    menuStartBtn.SetHoverData(menuBtnWidth + 32, menuBtnHeight + 16, menuHoverColor, menuHoverTextCol)

    pauseStartBtn = Button(screen, pauseBtnX, pauseBtnY,
                          pauseBtnWidth, pauseBtnHeight, pauseBtnColor,
                          exitfont, "Pause", pauseTxtColor)
    pauseStartBtn.SetHoverData(pauseBtnWidth + 8, pauseBtnHeight + 8, pauseHoverColor, pauseHoverTextCol)

    exitStartBtn = Button(screen, exitBtnX, exitBtnY,
                          exitBtnWidth, exitBtnHeight, exitBtnColor,
                          font, "QUIT", exitTxtColor)
    exitStartBtn.SetHoverData(exitBtnWidth + 8, exitBtnHeight + 8, exitHoverColor, exitHoverTextCol)

    resumeStartBtn = Button(screen, resumeBtnX, resumeBtnY,
                          resumeBtnWidth, resumeBtnHeight, resumeBtnColor,
                          font, "RESUME", resumeTxtColor)
    resumeStartBtn.SetHoverData(resumeBtnWidth + 8, resumeBtnHeight + 8, resumeHoverColor, resumeHoverTextCol)

    creditStartBtn = Button(screen, creditBtnX, creditBtnY,
                            creditBtnWidth, creditBtnHeight, creditBtnColor,
                            font, "CREDITS", creditTxtColor)
    creditStartBtn.SetHoverData(creditBtnWidth + 8, creditBtnHeight + 8, creditHoverColor, creditHoverTextCol)

    backCredBtn = Button(screen, backCredBtnX, backCredBtnY,
                            backCredBtnWidth, backCredBtnHeight, backCredBtnColor,
                            exitfont, "BACK", backCredTxtColor)
    backCredBtn.SetHoverData(backCredBtnWidth + 8, backCredBtnHeight + 8, backCredHoverColor, backCredHoverTextCol)

    playerColor = (42, 255, 100)
    projectileColor = (255, 9, 15)
    speedProjColor = (0, 50, 50)

    scoreColor = (100, 100, 100)
    hpRed = 205
    hpGreen = 250
    hpBlue = 170
    HPColor = (hpRed, hpGreen, hpBlue)
    bgColor = (10, 50, 255)


    projSpawnInterval = 60
    projSpawnTimer = 0
    projAmntPerInterval = 1


    idCheck = 0
    bnsSpeed = 1
    bnsSize = 2

    player = Player(screen, 240, 400, 32, 32, 15, playerColor, bnsSpeed,playerImage,bnsSize)

    bombs = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()
    playerGroup.add(player)

    movement_stack = []
    pressingLeft = False
    pressingRight = False

    currentScore = 0
    playerHP = 10


    gameState = "menu"
    states = {}

    def Initialize(self):
        self.states["menu"] = self.RunMenu
        self.states["game"] = self.RunGame
        self.states["pause"] = self.RunPause
        self.states["credits"] = self.RunCredits

        self.menuStartBtn.callback = self.StartGame
        self.pauseStartBtn.callback = self.PauseGame
        self.exitStartBtn.callback = self.QuitGame
        self.resumeStartBtn.callback = self.StartGame
        self.creditStartBtn.callback = self.StartCredits
        self.backCredBtn.callback = self.PauseGame


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
        else:
            btn.OnHoverExit()

    def UpdateBtnCallback(self, btn):
        mouse = pygame.mouse.get_pos()
        if btn.rect.collidepoint(mouse):
            btn.callback()

    def deleteExplosion(self,explosion):
        self.explosions.remove(explosion)

    def BombOffScreen(self, bomb):
        if bomb.id == 1:
            explode = Explosion(self.screen, bomb.rect.x, self.screen.get_height() - 64 * 2, 32, 64, 1, self.spdExplosionImage)
        elif bomb.id == 2:
            explode = Explosion(self.screen, bomb.rect.x, self.screen.get_height() - 64 * 2, 33, 33, 2,
                                self.sizeExplosionImage)
            explode.SetSize(4)

        else:
            explode = Explosion(self.screen, bomb.rect.x, (self.screen.get_height() + 106) / 2, 72, 106, 0, self.explosionImage)
#
        self.explosions.add(explode)

        explode.animDoneCallback = self.deleteExplosion


        self.bombs.remove(bomb)
        self.playerHP -= 1
        self.HPText = self.font.render(f"HP: {self.playerHP}", True, self.HPColor)
        self.hpRed += 10
        self.hpGreen -= 20
        self.hpBlue -= 10
        if self.hpRed >= 255:
            self.hpRed = 255
        if self.hpGreen <= 0:
            self.hpGreen = 00
        if self.hpBlue <= 0:
            self.hpBlue = 0
        self.HPColor = (self.hpRed, self.hpGreen, self.hpBlue)

        if self.playerHP <= 0:
            scoreText = self.font.render("You Lost!", True, (255, 0, 0))
            self.screen.blit(scoreText, (16, self.screen.get_height() - 128))
            pygame.quit()
            sys.exit()

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.UpdateBtnCallback(self.menuStartBtn)

        self.UpdateBtnHover(self.menuStartBtn)

        self.screen.fill(self.bgColor)
        self.screen.blit(self.titleText, ((self.screen.get_width()  / 2) - (self.titleText.get_width() / 2) , 96))
        self.menuStartBtn.draw()

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and pygame.K_a not in self.movement_stack:
                    self.movement_stack.append(pygame.K_a)
                elif event.key == pygame.K_d and pygame.K_d not in self.movement_stack:
                    self.movement_stack.append(pygame.K_d)
                elif event.key == pygame.K_ESCAPE:
                    self.PauseGame()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and pygame.K_a in self.movement_stack:
                    self.movement_stack.remove(pygame.K_a)
                elif event.key == pygame.K_d and pygame.K_d in self.movement_stack:
                    self.movement_stack.remove(pygame.K_d)

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.UpdateBtnCallback(self.pauseStartBtn)


        if self.movement_stack:
            if self.movement_stack[-1] == pygame.K_a:
                self.player.velocity[0] = -1
            elif self.movement_stack[-1] == pygame.K_d:
                self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        # Draw everything
        self.screen.fill((30, 30, 255))
        self.playerGroup.draw(self.screen)
        self.bombs.draw(self.screen)
        self.explosions.draw(self.screen)


        self.pauseStartBtn.draw()
        self.UpdateBtnHover(self.pauseStartBtn)

        self.screen.blit(self.scoreText, (16, self.screen.get_height() - 128))
        self.screen.blit(self.HPText, (16, self.screen.get_height() - 80))

        self.spdBnsText = self.exitfont.render(f"Bonus Speed Remaining: {round(self.player.bnsSpeedRemain / 60)}", True, (128, 128, 128))
        self.sizeBnsText = self.exitfont.render(f"Bonus Size Remaining: {round(self.player.bnsSizeRemain / 60)}", True,
                                               (128, 128, 128))
        #as long as there aren't bugs and good gameplay it should be fine

        if self.player.isBnsSpeed:
            self.screen.blit(self.spdBnsText,(self.screen.get_width() - 16 - self.spdBnsText.get_width(),16))
        if self.player.isBnsSize:
            self.screen.blit(self.sizeBnsText,(self.screen.get_width() - 16 - self.sizeBnsText.get_width(),32))



        self.projSpawnTimer += 1
        if self.projSpawnTimer >= self.projSpawnInterval:
            self.projSpawnTimer = 0
            randX = random.randint(0, self.screen.get_width())
            randSpeed = random.randint(3, 6)

            idCheck = random.randint(0, 10)
            id = 0
            projColor = self.projectileColor
            if idCheck == 7:
                id = 1
                projColor = self.speedProjColor
                b = Projectile(self.screen, randX, 16, 32, 32, randSpeed, projColor, id, self.spdBombImage)
            elif idCheck == 9:
                id = 2
                projColor = self.speedProjColor
                b = Projectile(self.screen, randX, 16, 32, 32, randSpeed, projColor, id, self.sizeBombImage)
            else:
                b = Projectile(self.screen, randX, 16, 32, 32, randSpeed, projColor, id, self.bombImage)
            b.offscreencallback = self.BombOffScreen
            self.bombs.add(b)

        self.playerGroup.update()
        self.bombs.update()
        self.explosions.update()

        collided = pygame.sprite.spritecollide(self.player, self.bombs, dokill=False)

        for c in collided:
            self.currentScore += 1
            self.bombs.remove(c)
            self.scoreText = self.font.render(f"Score: {self.currentScore}", True, self.scoreColor)
            if c.id == 1:
                self.player.applyBnsSpeed()
            elif c.id == 2:
                self.player.applyBnsSize()
                self.player.rect.y = 340




        #     self.projectiles.append(
        #         Projectile(self.screen, randX, 16, 16, 16, randSpeed, projColor, id))
        #
        # for p in self.projectiles:
        #     p.updates()
        #     if self.player.hitbox.colliderect(p.hitbox):
        #         self.currentScore += 1
        #         self.projectiles.remove(p)
        #         self.scoreText = self.font.render(f"Score: {self.currentScore}", True, self.scoreColor)
        #         if p.id == 1:
        #             self.player.applyBnsSpeed()
        #     elif p.posY >= self.screen.get_height() - p.height:
        #         self.projectiles.remove(p)
        #         self.playerHP -= 1
        #         self.HPText = self.font.render(f"HP: {self.playerHP}", True, self.HPColor)
        #         self.hpRed += 10
        #         self.hpGreen -= 20
        #         self.hpBlue -= 10
        #         if self.hpRed >= 255:
        #             self.hpRed = 255
        #         if self.hpGreen <= 0:
        #             self.hpGreen = 00
        #         if self.hpBlue <= 0:
        #             self.hpBlue = 0
        #         self.HPColor = (self.hpRed, self.hpGreen, self.hpBlue)
        #
        #         if self.playerHP <= 0:
        #             scoreText = self.font.render("You Lost!", True, (255, 0, 0))
        #             self.screen.blit(scoreText, (16, self.screen.get_height() - 128))
        #             pygame.quit()
        #             sys.exit()