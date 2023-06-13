from PIL import Image as img,ImageTk as imgtk
from tkinter import filedialog
from tkinter import *
import tkinter.font as f
from progress.bar import IncrementalBar
import os
from screeninfo import get_monitors

xscreen = int
yscreen = int

for m in get_monitors():
    xscreen = m.width
    yscreen = m.height

filename = filedialog.askopenfile(initialdir="/",title="image to decode",filetypes=(("PNG","*.png"),))
dir = os.path.split(filename.name)[0]


imTodec = img.open(filename.name)

newPixels = list(imTodec.getdata())

sentence = ""

compteur = 0

progress_bar_msg = IncrementalBar('reconstruction message',max=imTodec.size[0]*imTodec.size[1])

for i in newPixels:
    sentence += chr(i[0])
    progress_bar_msg.next()
progress_bar_msg.finish()

win = Tk()
win.attributes("-topmost", True)
font_size = f.Font(size=15)

def copy():
    win.clipboard_clear()
    win.clipboard_append(sentence)
    Label(win,text='copié !').pack()

def show_image():
    os.startfile(filename.name)
def show_text():
    os.startfile(f"{dir}/messageSecret.txt")
    

image = img.open(filename.name)
img = image.resize((image.size[0]*10,image.size[1]*10),img.NEAREST)
my_img = imgtk.PhotoImage(img)

if img.size[0] > 2/3*xscreen or img.size[1] > 2/3*yscreen:
    if len(sentence) > 10000:
        Label(win,text="image trop large/longue pour être chargée").pack()
        Label(win,text="texte trop long pour être affiché, enregistré dans le même dossier que l'image que vous avez pris").pack()
        Button(win,text="see image",command=show_image).pack()
        Button(win,text="see text",command=show_text).pack()
        with open(f"{dir}/messageSecret.txt","w",encoding='utf8') as myfile:
            myfile.write(sentence)
    else:
        Label(win,text="image trop large/longue pour être chargée").pack()
        Label(win,text="⇓").pack()
        Label(win,text=sentence,wraplength=2/3*xscreen).pack()
        Button(win,text="see image",command=show_image).pack()
else:
    if len(sentence) > 10000:
        Label(win,image=my_img).pack()
        Label(win,text="⇓").pack()
        Label(win,text="texte trop long pour être affiché, enregistré dans le même dossier que l'image que vous avez pris").pack()
        Button(win,text="see text",command=show_text).pack()
        with open(f"{dir}/messageSecret.txt","w",encoding="utf8") as myfile:
            myfile.write(sentence)
    else:
        Label(win,image=my_img).pack()
        Label(win,text="⇓").pack()
        Label(win,text=sentence,wraplength=img.size[0]).pack()

Button(win,text="📋",font=font_size,command=copy).pack()


win.update()
win.mainloop()
