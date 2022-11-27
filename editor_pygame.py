import pygame as pg
from texture import texture_list
from config import *
from win32api import GetSystemMetrics


def load_texture(list_file: list):
    textures = list()
    index = 0
    for file_name, name, layer in list_file:
        photo = pg.image.load(file_name)
        textures.append([photo, index, layer, name])
        index += 1
    return textures


def draw_grid():
    for draw_x in range(map_x + 1):
        pg.draw.line(screen, (0, 0, 0), [draw_x * TILE_SIZE, 0], [draw_x * TILE_SIZE, map_y * TILE_SIZE + 1])
    for draw_y in range(map_y + 1):
        pg.draw.line(screen, (0, 0, 0), [0, draw_y * TILE_SIZE], [map_x * TILE_SIZE, draw_y * TILE_SIZE])

def create_toollbar():
    for i, tile in enumerate(texture_data):
        frame_tool.blit((tile[0]), (10, 10+(6*i)+(i*TILE_SIZE)))


pg.init()
clock = pg.time.Clock()
FPS = 30
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
WINDOWS_SIZE = (width/1.2, height/1.2)
font = pg.font.Font(None, 30)
screen = pg.display.set_mode(WINDOWS_SIZE)
all_sprites = pg.sprite.Group()

map_x = 40
map_y = 25
map_data = [[[-1, -1, ] for i in range(map_y)] for j in range(map_x)]
texture_cur = 0
layer_cur = 0
texture_data = load_texture(texture_list)
print(texture_data)
#print(pg.display.Info())



#width, height = pg.display.Info().current_w, pg.display.Info().current_h
print(f'Ширина: {width}, Высота: {height}')

frame_map = pg.Surface((map_x*TILE_SIZE, map_y*TILE_SIZE))
frame_map.fill((255, 255, 255))
frame_tool = pg.Surface((100, map_y*TILE_SIZE))
frame_tool.fill((0, 255, 255))
run = True

while run:
    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            run = False
        if event.type == pg.KEYDOWN:
            print(map_data)
            screen.scroll(10, 10)
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse_cell_x, mouse_cell_y = mouse_x // TILE_SIZE, mouse_y // TILE_SIZE
    mouse_b1, mouse_b2, mouse_b3 = pg.mouse.get_pressed()

    if mouse_b1:
        print(mouse_x)
        if mouse_x <= map_x*TILE_SIZE and mouse_y <= map_y*TILE_SIZE:
            print(f'Тайл мыши: x-{mouse_cell_x}, y-{mouse_cell_y}')
            map_data[mouse_cell_x][mouse_cell_y][0] = texture_cur
        if mouse_x >= 970:
            if mouse_y >= 10 and mouse_y <= 34:
                texture_cur = 0
                print(texture_cur)
            elif mouse_y >= 40 and mouse_y <= 64:
                texture_cur = 1
                print(texture_cur)
            elif mouse_y >= 70 and mouse_y <= 94:
                texture_cur = 2
                print(texture_cur)
            elif mouse_y >= 100 and mouse_y <= 124:
                texture_cur = 3
                print(texture_cur)
            elif mouse_y >= 130 and mouse_y <= 154:
                texture_cur = 4
                print(texture_cur)
            elif mouse_y >= 160 and mouse_y <= 184:
                texture_cur = 5
                print(texture_cur)
    if mouse_b3:
        if mouse_x <= map_x*TILE_SIZE and mouse_y <= map_y*TILE_SIZE:
            print("УДАЛИТЬ")
            map_data[mouse_cell_x][mouse_cell_y][0] = -1

    #if self.rect.collidepoint(event.pos):

    for y in range(map_y):
        for x in range(map_x):
            #print(texture[map_data[x][y][0]])
            if map_data[x][y][0] != -1:
                tile = texture_data[map_data[x][y][0]][0]
                #print(f'Id-{texture_data[map_data[x][y][0]][3]}: x-{x}, y-{y}')
                frame_map.blit(tile, (x * TILE_SIZE, y * TILE_SIZE))
    screen.blit(frame_map, (0, 0))
    screen.blit(frame_tool, (map_x*TILE_SIZE, 0))
    draw_grid()
    create_toollbar()
    pg.display.update()
    frame_map.fill((255, 255, 255))
    clock.tick(FPS)
