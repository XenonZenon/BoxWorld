#Author: Jayson Abad
#(c) 2018, Noysoft
#Date: 2018.06.11
import pygame
from settings.constants import *

class States(object):
    def __init__(self):
        super(States, self).__init__()

    def menu(self, size ,color):
        menu = pygame.Surface(size)
        menu.fill(color)
        pygame.draw.rect(menu, COLOR['other'], ((SIZE['height']/2) - 500/2, (SIZE['width']/2) - 310/2, 500, 310))
        return menu

    def gameWorld(self, data):
        game_world = pygame.Surface(data[0])
        game_world.fill(data[1])
        return game_world

    def gameOver(self, data):
        game_over = pygame.Surface(data[0])
        game_over.fill(data[1])
        return game_over
