import sys
from idlegame import IdleGame
import pygame

# 1. Initialize Pygame
pygame.init()
g = IdleGame()
g.Initialize()
#
#
running = True
while running:
    pygame.display.flip()
    g.states[g.gameState]()
    # Cap the frame rate at 60 FPS
    g.clock.tick(60)

# 4. Clean up
pygame.quit()
sys.exit()