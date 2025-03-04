from PIL import Image
from random import randint
import ctypes
import time
import keyboard as k
from dotenv import load_dotenv
from os import getenv
from time_this_function import time_this_function
from args import arguments
from logger import Logger

LOGGER = Logger()

load_dotenv(".env")

path = getenv("BG_PATH")
try:
    if arguments.x_length:
        input_x_size = arguments.x_length
    else:
        input_x_size = abs(int(input("Taille du background en x: ")))
except:
    input_x_size = randint(1, 3)
try:
    if arguments.y_length:
        input_y_size = arguments.y_length
    else:
        input_y_size = abs(int(input("Taille du background en y: ")))
except:
    input_y_size = randint(1, 3)
try:
    if arguments.delay:
        interval = arguments.delay
    else:
        interval = abs(
            int(input("Temps entre chaque changement de background (0 pour aucun): "))
        )
except:
    interval = randint(5, 10)


@time_this_function
def generate():
    sizeex = input_x_size
    sizeey = input_y_size
    sizee = (sizeex, sizeey)
    im = Image.new(mode="RGBA", size=sizee)
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixels[i, j] = (randint(0, 255), randint(0, 255), randint(0, 255))
    im.save(f"{path}/bg.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{path}/bg.png", 0)


generate()

while not k.is_pressed("1"):
    if interval != 0:
        time.sleep(interval)
        generate()
