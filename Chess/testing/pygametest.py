import pygame
from pygame.locals import *
import os

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
EDGE_LENGTH = 500

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode([EDGE_LENGTH, EDGE_LENGTH])
pygame.display.set_caption("Chess")

while True:
    screen.fill(white)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()