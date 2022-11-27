import pygame
from pygame.sprite import Sprite
from pygame import Surface
from config import *


d = {'1': 'skeleton',
     '2': ''}


class Creature(Sprite):
    def __init__(self, x, y, id):
        Sprite.__init__(self)
        self.image = pygame.image.load('texture/' + d[id] + '.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.is_move = False
        self.speed = 6
        self.x = x
        self.y = y
        self.test = pygame.Surface((self.x, self.y))
        self.test.fill((255, 0, 0))
        self.x_ani = self.x * TILE_SIZE
        self.y_ani = self.y * TILE_SIZE
        self.text_ani_x = 0
        self.text_ani_y = 0
        self.x_targ = self.x
        self.y_targ = self.y

    def collision(self, level_map, x, y):
        # print(f'X-{x}, Y-{y}')
        if x > len(level_map)-1 or x < 0 or y > len(level_map[0])-1 or y < 0:
            return True
        tile = level_map[x][y]
        if tile == 3 or tile == 5:
            return True
        else:
            return False

    def move(self, level_map, x, y):
        if not self.is_move:
            if not self.collision(level_map, x, y):
                self.is_move = True
                self.x = x
                self.y = y

    def update(self):
        self.is_move = True


    def draw(self, surf, player):
        # surf.blit(self.image, (self.x_ani, self.y_ani))
        x_slide = player.x_ani - (player.x * TILE_SIZE)
        y_slide = player.y_ani - (player.y * TILE_SIZE)
        # if x_slide != 0 or y_slide != 0:
        #     print(f'[A] x_slide ({x_slide}), y_slide ({y_slide})')
        surf.blit(self.image, (((self.x+4)-player.x)*TILE_SIZE-x_slide, ((self.y+4)-player.y)*TILE_SIZE-y_slide))
