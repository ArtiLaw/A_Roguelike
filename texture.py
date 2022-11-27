from tkinter import PhotoImage


def load_texture():
    #print(texture_list)
    textures = list()
    index = 0
    for file_name, name, layer in texture_list:
        image = PhotoImage(file=file_name)
        textures.append([image, index, layer, name])
        index += 1
    # print(textures)
    return textures


texture_list = [
    ['texture/dirt.png', 'Земля', 0],
    ['texture/lea.png', 'Луг', 0],
    ['texture/grass.png', 'Трава', 0],
    ['texture/wood.png', 'Лес', 1],
    ['texture/rock.png', 'Скала', 1],
    ['texture/wall.png', 'Стена', 1]
]
