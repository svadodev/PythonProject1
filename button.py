import pygame

class Button:
    active = True
    rect = pygame.Rect(0,0,0,0)
    color = (0, 0, 0)
    defaultColor = (0,0,0)
    txtColor = (0, 0, 0)
    defaultTxtColor = (0,0,0)

    hoverColor = (0,0,0)
    hoverTxtColor = (0,0,0)
    hoverWidth = 0
    hoverHeight = 0

    x = 0
    y = 0
    width = 0
    height = 0

    font = None
    txtObject = None
    txt =  "No Text"
    callback = None
    screen = None
    txtCenterX = 0
    txtCenterY = 0

    def __init__(self, screen, x, y, width, height, color, font, txt, txtColor):
        self.screen = screen
        self.x = x
        self.defaultX = x
        self.y = y
        self.defaultY = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.defaultColor = color
        self.font = font

        self.txt = txt
        self.txtColor = txtColor
        self.defaultTxtColor = txtColor
        self.txtObject = self.font.render(self.txt, True, self.txtColor)

        self.txtCenterX = x+(width / 2) - (self.txtObject.get_width() / 2)
        self.txtCenterY = y+(height / 2) - (self.txtObject.get_height() / 2)

    def SetHoverData(self, width, height, color, txtColor):
        self.hoverWidth = width
        self.hoverHeight = height
        self.hoverColor = color
        self.hoverTxtColor = txtColor

    def OnHoverEnter(self):
        self.color = self.hoverColor
        self.x = (self.defaultX) - (self.hoverWidth / 2)
        self.y = (self.defaultY) - (self.hoverHeight / 2)
        self.rect = pygame.Rect(self.x, self.y, self.hoverWidth, self.hoverHeight)
        self.txtCenterX = self.x + (self.hoverWidth / 2) - (self.txtObject.get_width() / 2)
        self.txtCenterY = self.y + (self.hoverHeight / 2) - (self.txtObject.get_height() / 2)
        self.txtColor = self.hoverTxtColor
        self.txtObject = self.font.render(self.txt, True, self.txtColor)


    def OnHoverExit(self):
        self.color = self.defaultColor
        self.x = (self.defaultX) - (self.width / 2)
        self.y = (self.defaultY) - (self.height / 2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.txtCenterX = self.x + (self.width / 2) - (self.txtObject.get_width() / 2)
        self.txtCenterY = self.y + (self.height / 2) - (self.txtObject.get_height() / 2)
        self.txtColor = self.defaultTxtColor
        self.txtObject = self.font.render(self.txt, True, self.txtColor)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.txtObject, (self.txtCenterX, self.txtCenterY))
