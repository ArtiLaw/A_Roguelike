import pygame
from pygame.sprite import Sprite
from pygame import Surface
from config import *


BLOCKED_TILE = [2, 3]


class Player(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        # self.image = Surface((24, 24))
        # self.image.fill((255, 255, 255))
        self.image = pygame.image.load('texture/player.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.is_move = False
        self.speed = 6
        self.x = x
        self.y = y
        self.test = pygame.Surface((self.x, self.y))
        self.test.fill((255, 0, 0))
        self.x_ani = self.x * TILE_SIZE
        self.y_ani = self.y * TILE_SIZE
        self.x_targ = self.x
        self.y_targ = self.y

    def update(self, up, right, down, left, level_map: list):
        if not self.is_move:
            if up and self.y > 0:
                print('up')
                self.is_move = True
                #self.x_targ = self.x
                self.y_targ = self.y - 1
            elif right and self.x < 576:
                print('right')
                self.is_move = True
                self.x_targ = self.x + 1
                #self.y_targ = self.y
            elif down and self.y < 456:
                print('down')
                self.is_move = True
                #self.x_targ = self.x
                self.y_targ = self.y + 1
            elif left and self.x > 0:
                print('left')
                self.is_move = True
                self.x_targ = self.x - 1
                #self.y_targ = self.y
        if self.x_ani < self.x_targ * TILE_SIZE:
            self.x_ani += self.speed
        elif self.x_ani > self.x_targ * TILE_SIZE:
            self.x_ani -= self.speed
        if self.y_ani < self.y_targ * TILE_SIZE:
            self.y_ani += self.speed
        elif self.y_ani > self.y_targ * TILE_SIZE:
            self.y_ani -= self.speed
        if self.x_ani == self.x_targ * TILE_SIZE and self.y_ani == self.y_targ * TILE_SIZE:
            self.is_move = False
            self.x = self.x_targ
            self.y = self.y_targ

    # def animation(self):

    def draw(self, surf):
        surf.blit(self.image, (self.x_ani, self.y_ani))
        #surf.blit(self.test, (self.x_targ, self.y_targ))
