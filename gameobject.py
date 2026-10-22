import pygame
class GameObject(pygame.sprite.Sprite):
    width = 32
    height = 32
    posX = 0
    posY = 0
    speed = 0
    velocity = [0, 0]
    screen = None
    image = None
    color = (0,0,0)