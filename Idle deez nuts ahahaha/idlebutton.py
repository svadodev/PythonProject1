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

    def __init__(self, screen, x, y, width, height, color, font, txt, txtColor, alignment = 0, btnImage = None):
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
        self.borderSize = 4

        self.btnImage = btnImage
        self.btnImageX = 0
        self.btnImageY = 0
        if self.btnImage is not None:
            self.btnImage = pygame.transform.scale(self.btnImage,
                                                   (self.btnImage.get_width() * 4, self.btnImage.get_height() * 4))

        self.alignment = alignment
        self.AlignButton()



    def AlignButton(self, hover = False):
        w = self.width
        h = self.height
        if hover:
            w = self.hoverWidth
            h = self.hoverHeight

        if self.btnImage is not None:
            self.btnImageX = self.x + (w/2) - (self.btnImage.get_width() / 2)
            self.btnImageY = self.y + (h / 2) - (self.btnImage.get_height() / 2)

        # center
        if self.alignment == 0:
            self.txtCenterX = self.x + (w / 2) - (self.txtObject.get_width() / 2)
            self.txtCenterY = self.y + (h / 2) - (self.txtObject.get_height() / 2)
        #bottom center
        if self.alignment == 1:
            self.txtCenterX = self.x + (w / 2) - (self.txtObject.get_width() / 2)
            self.txtCenterY = self.y + h - self.txtObject.get_height()

        pass

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
        self.AlignButton(hover = True)
        self.txtColor = self.hoverTxtColor
        self.txtObject = self.font.render(self.txt, True, self.txtColor)


    def OnHoverExit(self):
        self.color = self.defaultColor
        self.x = (self.defaultX) - (self.width / 2)
        self.y = (self.defaultY) - (self.height / 2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.AlignButton()
        self.txtColor = self.defaultTxtColor
        self.txtObject = self.font.render(self.txt, True, self.txtColor)

    def draw(self):
        borderRect = pygame.Rect(self.rect.x - self.borderSize ,
                                 self.rect.y - self.borderSize ,
                                 self.rect.width + self.borderSize *2,
                                 self.rect.height + self.borderSize *2)
        borderColor = (0,0,0)
        pygame.draw.rect(self.screen, borderColor,borderRect)
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.txtObject, (self.txtCenterX, self.txtCenterY))
        if self.btnImage is not None:
            self.screen.blit(self.btnImage, (self.btnImageX, self.btnImageY))

