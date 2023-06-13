from PIL import Image
from random import randint
import ctypes
from progress.bar import IncrementalBar
import time
import keyboard as k


path = "C:/Users/Romain/Documents/code/python/dataInImage/bg_changing/exe/dist/main"

def generate():
    sizeex = randint(1,3)
    sizeey = randint(1,3)
    sizee = (sizeex,sizeey)
    im = Image.new(mode="RGBA",size=sizee)
    pixels = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixels[i,j] = (randint(0,255),randint(0,255),randint(0,255))
    im.save(f"{path}/bg.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0,f"{path}/bg.png", 0)

while not k.is_pressed("1"):
    time.sleep(10)
    generate()