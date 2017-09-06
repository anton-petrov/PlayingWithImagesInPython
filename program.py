# Работа с изображениями в Python.
# Коды фильтров: 0 - оттенки серого, 1 - сепия, 2 - негатив, 3 - шум, 4 - яркость, 5 - черно-белое.
# В результате работы на диске будет сохранен файл output.jpg.
# На вход подается файл input.jpg.

import random
from PIL import Image, ImageDraw
# вводим режим обработки изображения (фильтр)
mode = int(input('mode[shades of gray=0, sepia=1, negative=2, noise=3, brightness=4, black and white=5]: '))
# открываем изображение
image = Image.open("input.jpg")
# получаем объект для рисования
draw = ImageDraw.Draw(image)
# ширина картинки
width = image.size[0]
# высота картинки
height = image.size[1]
# загружаем массив пикселей
pix = image.load()
if mode == 0:
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3  # целочисленное деление
            draw.point((i, j), (S, S, S))
if mode == 1:
    depth = int(input('depth: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = (a + b + c) // 3
            a = S + depth * 2
            b = S + depth
            c = S
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))
if mode == 2:
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))
if mode == 3:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            rand = random.randint(-factor, factor)
            a = pix[i, j][0] + rand
            b = pix[i, j][1] + rand
            c = pix[i, j][2] + rand
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))
if mode == 4:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0] + factor
            b = pix[i, j][1] + factor
            c = pix[i, j][2] + factor
            if a < 0:
                a = 0
            if b < 0:
                b = 0
            if c < 0:
                c = 0
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))
if mode == 5:
    factor = int(input('factor: '))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if S > (((255 + factor) // 2) * 3):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
# сохраняем результирующее изображение
image.save("output.jpg", "JPEG")
del draw
