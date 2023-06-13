from PIL import Image
from random import randint
from tkinter import filedialog
from progress.bar import IncrementalBar
from unidecode import unidecode



directory = filedialog.askdirectory()
print(directory)

texte = ""

fileOrText = input("depuis:\nfichier texte[1]\nmanuel[2]\n")
if fileOrText == "1":
    file = filedialog.askopenfile(initialdir="/",title="text to encode",filetypes=(("txt","*.txt"),))
    with open(file.name,"r",encoding='utf8') as myfile:
        texte = myfile.read()
        texte = texte.replace("\n"," ")
        texte = unidecode(texte)
        input()
elif fileOrText == "2":
    texte = input("to encode:\n")
    texte = unidecode(texte)


liste = []

progress_bar_xy = IncrementalBar('calcul des tailles possibles (x,y)',max=len(texte))

for i in range(1,len(texte)+1):
    for j in range(1,len(texte)+1):
        if i*j == len(texte):
            liste.append((i,j))
    progress_bar_xy.next()

progress_bar_xy.finish()

lower = len(texte)
best = ()

progress_bar_best = IncrementalBar('choix de la meilleure taille',max=len(liste))

for i in liste:
    if i[0] - i[1] >= 0 and i[0] - i[1] <= lower:
        lower = i[0] - i[1]
        best = (i[0],i[1])
    if i[1] - i[0] >= 0 and i[1] - i[0] <= lower:
        lower = i[1] - i[0]
        best = (i[1],i[0])
    progress_bar_best.next()

progress_bar_best.finish()

print(len(texte))
print(liste)
print(best)

im = Image.new(mode="RGBA",size=best)
pixels = im.load()

bits = bytes(texte,'utf-8')

npix = 0

progress_bar_encoding = IncrementalBar('Encoding',max=im.size[0]*im.size[1])


for y in range(im.size[1]):
    for x in range(im.size[0]):
        pixels[x,y] = (bits[npix],randint(0,255),randint(0,255))
        npix += 1
        progress_bar_encoding.next()

progress_bar_encoding.finish()

savename = input("nom du fichier\n")

im.save(f"{directory}/{savename}.png")