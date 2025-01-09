from random import randint
from tkinter import filedialog
from time_this_function import time_this_function
from logger import Logger
from PIL import Image
from progress.bar import IncrementalBar
from unidecode import unidecode

LOGGER = Logger()


@time_this_function
def best_size_v1(txt: str, sizes_list: list):
    progress_bar_xy = IncrementalBar("calcul des tailles possibles (x,y)", max=len(txt))
    for i in range(1, len(txt) + 1):
        for j in range(1, len(txt) + 1):
            if i * j == len(txt):
                sizes_list.append((i, j))
        progress_bar_xy.next()
    progress_bar_xy.finish()


@time_this_function
def best_size_v2(txt: str, sizes_list: list):
    LOGGER.info("Calcul de la taille idéale (x,y)")
    for i in range(1, len(txt) // 2):
        if len(txt) % i == 0:
            sizes_list.append((i, len(txt) // i))


directory = filedialog.askdirectory()
print(directory)

texte = ""

fileOrText = input("depuis:\nfichier texte[1]\nmanuel[2]\n")
if fileOrText == "1":
    file = filedialog.askopenfile(
        # initialdir="/",
        title="text to encode",
        filetypes=(("txt", "*.txt"), ("md", "*.md")),
    )
    with open(file.name, "r", encoding="utf8") as myfile:
        texte = myfile.read()
        texte = texte.replace("\n", " ")
        texte = unidecode(texte)
elif fileOrText == "2":
    texte = input("to encode:\n")
    texte = unidecode(texte)


liste = []

best_size_v1(texte, liste)

lower = len(texte)
best = ()

for k in liste:
    if k[0] - k[1] >= 0 and k[0] - k[1] <= lower:
        lower = k[0] - k[1]
        best = (k[0], k[1])
    if k[1] - k[0] >= 0 and k[1] - k[0] <= lower:
        lower = k[1] - k[0]
        best = (k[1], k[0])

print(f"Le fichier contient {len(texte)} caractères")
# print(liste)
print(f"la taille optimale (x,y) est {best}")

im = Image.new(mode="RGBA", size=best)
pixels = im.load()

bits = bytes(texte, "utf-8")

npix = 0

progress_bar_encoding = IncrementalBar("Encoding", max=im.size[0] * im.size[1])


for y in range(im.size[1]):
    for x in range(im.size[0]):
        pixels[x, y] = (bits[npix], randint(0, 255), randint(0, 255))
        npix += 1
        progress_bar_encoding.next()

progress_bar_encoding.finish()

savename = input("nom du fichier\n")

im.save(f"{directory}/{savename}.png")
