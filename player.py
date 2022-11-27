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

    def update(self, up, right, down, left, level_map: list):
        if up and self.y > 0:
            # print('up')
            #self.is_move = True
            self.move(level_map, self.x, self.y - 1)
            #self.y = self.y - 1
        elif right and self.x < 576:
            # print('right')
            #self.is_move = True
            #self.x = self.x + 1
            self.move(level_map, self.x + 1, self.y)
        elif down and self.y < 456:
            # print('down')
            #self.is_move = True
            #self.y = self.y + 1
            self.move(level_map, self.x, self.y + 1)
        elif left and self.x > 0:
            # print('left')
            #self.is_move = True
            #self.x = self.x - 1
            self.move(level_map, self.x - 1, self.y)
        if self.x_ani < self.x * TILE_SIZE:
            self.x_ani += self.speed
        elif self.x_ani > self.x * TILE_SIZE:
            self.x_ani -= self.speed
        if self.y_ani < self.y * TILE_SIZE:
            self.y_ani += self.speed
        elif self.y_ani > self.y * TILE_SIZE:
            self.y_ani -= self.speed
        if self.x_ani == self.x * TILE_SIZE and self.y_ani == self.y * TILE_SIZE:
            self.is_move = False

    # def animation(self):

    def draw(self, surf):
        # surf.blit(self.image, (self.x_ani, self.y_ani))
        surf.blit(self.image, (4*TILE_SIZE, 4*TILE_SIZE))
