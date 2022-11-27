from pprint import pprint
import pygame as pg

from editor import open_map
from texture import texture_list


FILE = 'my_map.txt'
TILE_SIZE = 24
TILES = {
    'dirt': 0,
    'grass': 1,
    'wood': 2
}
cur_map = open_map(FILE)

# def draw_map(screen, width=20, height=15):
#     tiles = load_tiles(texture_list) # fixe needed
#     for x, col in enumerate(cur_map):
#         for y, tile in enumerate(col):
#             if tile != -1:
#                 #print(f'Текстура: {tiles[tile]}')
#                 screen.blit(tiles[tile], (x * TILE_SIZE, y * TILE_SIZE))

def draw_map(screen, player, level_x_width, level_y_height):
    tiles = load_tiles(texture_list)
    a = 9
    game_screen = [[0] * a for i in range(a)]
    screen_map = list()
    x_move = player.x - 4
    y_move = player.y - 4
    # print(f'X-{x_move}, Y-{y_move}')
    for x_i in range(9):
        for y_i in range(9):
            if x_i+x_move > level_x_width-1 or y_i+y_move > level_y_height-1 or x_i+x_move < 0 or y_i+y_move < 0:
                game_screen[x_i][y_i] = -1
            else:
                # print(f'Xcur_map-{x_i + x_move}, Ycur_map-{y_i + y_move}')
                game_screen[x_i][y_i] = cur_map[x_i+x_move][y_i+y_move]
    for x, col in enumerate(game_screen):
        for y, tile in enumerate(col):
            if tile != -1:
                x_slide = player.x_ani - (player.x * TILE_SIZE)
                y_slide = player.y_ani - (player.y * TILE_SIZE)
                # if x_slide != 0 or y_slide != 0:
                #     print(f'[T] x_slide ({x_slide}), y_slide ({y_slide})')
                screen.blit(tiles[tile], ((x * TILE_SIZE)-x_slide, (y * TILE_SIZE)-y_slide))


def load_tiles(list_of_tiles: list) -> list:
    tiles = list()
    for tile in list_of_tiles:
        tiles.append(pg.image.load(tile[0]))
    return tiles


if __name__ == '__main__':
    draw_map()
