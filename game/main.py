#Author: Jayson Abad
#(c) 2018, Noysoft
#Date: 2018.06.11
import sys
import pygame
from pygame.locals import *
from settings.constants import *
from settings.data import *
from state.states import States

class Game(object):
    def __init__(self):
        super(Game, self).__init__()
        self.initialize()
        self.state = States()
        self.mainGameLoop()

    def initialize(self):
        pygame.init()
        self.surface = pygame.display.set_mode(SIZE['window'])
        self.surface.fill(COLOR['other'])
        pygame.display.set_caption(TEXT['caption'])

    def mainGameLoop(self):
        self.surface.blit(self.state.menu(SIZE['window'], COLOR['white']), (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == KEYUP and event.key == pygame.K_a:
                    self.surface.blit(self.state.gameWorld(Data), (0, 0))
                if event.type == KEYUP and event.key == pygame.K_SPACE:
                    self.surface.blit(self.state.gameWorld(New_data), (0, 0))
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
