import pygame as pg

from player import Player
from creature import Creature
from map import draw_map
from editor import open_map

pg.init()
clock = pg.time.Clock()
FPS = 20
WINDOWS_SIZE = (600, 480)
font = pg.font.Font(None, 30)
screen = pg.display.set_mode(WINDOWS_SIZE)
game_space = pg.Surface((216, 216))
game_space.fill((255, 60, 60))
all_sprites = pg.sprite.Group()
all_enemy = pg.sprite.Group()

cur_map = open_map('my_map.txt')
level_x_width = len(cur_map)
level_y_height = len(cur_map[0])
print(level_x_width, level_y_height)

player = Player(4, 4)
crea1 = Creature(8, 8, '1')
crea2 = Creature(5, 3, '1')
crea3 = Creature(10, 15, '1')
all_enemy.add(crea1, crea2, crea3)

up = right = down = left = False
pause = 10
all_sprites.add(player)

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                up = True
                #print('up')
            if event.key == pg.K_LEFT:
                left = True
                #print('left')
            if event.key == pg.K_DOWN:
                down = True
                #print('down')
            if event.key == pg.K_RIGHT:
                right = True
                #print('right')
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                up = False
            if event.key == pg.K_LEFT:
                left = False
            if event.key == pg.K_DOWN:
                down = False
            if event.key == pg.K_RIGHT:
                right = False
    screen.fill((40, 40, 40))
    game_space.fill((40, 40, 40))
    # for y in range(15):
    #     for x in range(20):
    #         pg.draw.rect(screen, (0, 0, 0), (x * 32, y * 32, 32, 32), 1)
    draw_map(screen=game_space, player=player, level_x_width=level_x_width, level_y_height=level_y_height)
    data = {
        'up': up,
        'right': right,
        'down': down,
        'left': left,
        'level_map': cur_map
    }
    player.update(**data)
    # all_sprites.draw(screen)
    for sprite in all_sprites:
        sprite.draw(game_space)
    for enemy in all_enemy:
        enemy.draw(game_space, player)
    # player.update(up, right, down, left)
    # player.draw(screen)
    text = font.render(
        f'x_tar {player.x_ani-(player.x*24)}, y_tar {player.y_ani-(player.y*24)}', True, (255, 255, 255))
    text2 = font.render(
        f'x {player.x}, y {player.y}', True, (255, 255, 255))
    screen.blit(text, (20, 460))
    screen.blit(text2, (20, 440))
    screen.blit(game_space, (192, 132))
    pg.display.update()
    clock.tick(FPS)

