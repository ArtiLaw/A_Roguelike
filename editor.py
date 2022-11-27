import tkinter
from pprint import pprint
from tkinter import *
from config import *
from texture import texture_list


def click_canvas(event):
    # print(f'Координаты мыши {event.x//increase}, {event.y//increase}')
    # print(f'Координаты мыши {image_data_list[event.x//increase][event.y//increase]}')
    t_x = event.x // TILE_SIZE
    t_y = event.y // TILE_SIZE
    # print(map_data[t_x][t_y][0])
    if map_data[t_x][t_y][layer_cur] != texture_cur:
        map_data[t_x][t_y][layer_cur] = texture_cur
        # print(canvas_map.find_all())
        print(f'Текущий слой: {layer_cur}')
        canvas_map.delete(str(layer_cur) + '.' + str(t_x) + '.' + str(t_y))
        print(str(layer_cur) + '.' + str(t_x) + '.' + str(t_y))
        tile = canvas_map.create_image(event.x // 24 * 24, event.y // 24 * 24, anchor=NW, image=texture[texture_cur][0],
                                       tags=str(layer_cur) + '.' + str(t_x) + '.' + str(t_y))
        if layer_cur == 0:
            canvas_map.tag_lower(tile)


def create_grid():
    for draw_x in range(map_x + 1):
        canvas_map.create_line(draw_x * TILE_SIZE, 0, draw_x * TILE_SIZE, map_y * TILE_SIZE + 1)
    for draw_y in range(map_y + 1):
        canvas_map.create_line(0, draw_y * TILE_SIZE, map_x * TILE_SIZE, draw_y * TILE_SIZE)


def create_toollbar(canvas):
    for tile in texture:
        canvas.create_image(10, 34 * tile[1] + 10, anchor=NW, image=tile[0], tags=tile[1])


def click_tool(event):
    global texture_cur
    global layer_cur
    get_tag = canvas_tool.gettags("current")
    texture_cur = int(get_tag[0])
    layer_cur = texture[texture_cur][2]
    print(f'Слой: {layer_cur}')
    # print(texture_cur)


def print_map():
    file = 'my_map.txt'
    save_map(map_data, file)
    new_map = open_map(file)
    print('load map')
    pprint(new_map)
    for t in map_data:
        print(t)


def save_map(new_map: list, file_name='file.txt') -> None:
    with open(file_name, 'w') as file:
        for row in new_map:
            file.write(' '.join([str(tile) for tile in row]) + '\n')


def open_map(file_name: str) -> list:
    read_map = list()
    with open(file_name, 'r') as file:
        for line in file.readlines():
            read_map.append([int(tile) for tile in line.split()])
    #print(read_map)
    return read_map


def load_texture(list_file: list):
    textures = list()
    index = 0
    for file_name, name, layer in list_file:
        photo = PhotoImage(file=file_name)
        textures.append([photo, index, layer, name])
        index += 1
    return textures

def resize(event):
    #print(event.height, event.width)
    region = canvas_map.bbox(ALL)
    canvas_map.configure(scrollregion=region)

def resize_frame(event):
    #frame.itemconfig(canvas_map, height=event.height, width=event.width)
    print(event.height, event.width)


if __name__ == '__main__':
    map_x = 40
    map_y = 30
    map_data = [[[-1, -1, ] for i in range(map_y)] for j in range(map_x)]
    window = Tk()
    window.title("Редактор карт")
    window.geometry("800x600+500+200")
    window.grab_set()
    texture_cur = 0
    layer_cur = 0
    texture_dirt = PhotoImage(file='texture/dirt.png')
    texture_grass = PhotoImage(file='texture/grass.png')
    texture_wood = PhotoImage(file='texture/wood.png')
    # texture = [texture_dirt, texture_grass, texture_wood]

    texture = load_texture(texture_list)

    frame = LabelFrame(master=window, text='Карта', width=100, height=100, bg='white')
    frame.pack(side=LEFT, expand=False, anchor=N)


    scroll_x = Scrollbar(frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(frame, orient=VERTICAL)

    canvas_map = Canvas(frame, width=481, height=361, bg='white',
                        highlightthickness=0,
                        xscrollcommand=scroll_x.set,
                        yscrollcommand=scroll_y.set,
                        scrollregion=(0, 0, map_x * TILE_SIZE + 1, map_y * TILE_SIZE + 1)
                        )

    scroll_x.config(command=canvas_map.xview)
    scroll_y.config(command=canvas_map.yview)

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    # canvas_map.bind('<Button-1>', lambda event, c=john: click_canvas(event, c))
    # canvas_map.bind('<Button-1>', lambda event: click_canvas(event))
    canvas_map.bind('<B1-Motion>', lambda event: click_canvas(event))
    canvas_map.pack(side=LEFT, anchor=N, padx=5, pady=5)

    print(map_y)
    create_grid()
    frame_orig_img = LabelFrame(master=window, text='Инструменты', width=100, height=100, bg='white')
    frame_orig_img.pack(side=LEFT, expand=False, anchor=N)
    button_replace = Button(master=window, text='Создать', command=print_map)
    canvas_tool = Canvas(frame_orig_img,
                         width=80,
                         height=360,
                         bg='white')
    canvas_tool.pack(side=LEFT, anchor=N)
    canvas_tool.create_image(10, 10, anchor=NW, image=texture_dirt, tags=0)
    canvas_tool.create_image(10, 44, anchor=NW, image=texture_grass, tags=1)
    canvas_tool.create_image(10, 78, anchor=NW, image=texture_wood, tags=2)
    canvas_tool.bind('<Button-1>', click_tool)
    window.update_idletasks()
    window.bind("<Configure>", resize_frame)
    #canvas_map.bind("<Configure>", resize_frame)
    window.update_idletasks()
    window.minsize(window.winfo_width(), window.winfo_height())
    print(window.winfo_width(), window.winfo_height())
    create_toollbar(canvas_tool)
    button_replace.pack()

    window.mainloop()
