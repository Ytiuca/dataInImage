# # texte = "aberuheikfdnbfdj"

# # liste = []

# # for i in range(1,len(texte)+1):
# #     for j in range(1,len(texte)+1):
# #         if i*j == len(texte):
# #             liste.append((i,j))

# # lower = len(texte)
# # best = ()

# # for i in liste:
# #     if i[0] - i[1] >= 0 and i[0] - i[1] <= lower:
# #         lower = i[0] - i[1]
# #         best = (i[0],i[1])
# #     if i[1] - i[0] >= 0 and i[1] - i[0] <= lower:
# #         lower = i[1] - i[0]
# #         best = (i[1],i[0])

# # print(liste,"\n",len(texte),"\n",lower,best)

# # Python program to create
# # a file explorer in Tkinter

# # import all components
# # from the tkinter library
# from tkinter import *

# # import filedialog module
# from tkinter import filedialog

# # Function for opening the
# # file explorer window
# def browseFiles():
# 	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("PNG","*.png*"),))
	
# 	# Change label contents
# 	label_file_explorer.configure(text="File Opened: "+filename)
	
	
																								
# # Create the root window
# window = Tk()

# # Set window title
# window.title('File Explorer')

# # Set window size
# window.geometry("500x500")

# #Set window background color
# window.config(background = "white")

# # Create a File Explorer label
# label_file_explorer = Label(window,text = "File Explorer using Tkinter",
# 							width = 100, height = 4,
# 							fg = "blue")

	
# button_explore = Button(window,
# 						text = "Browse Files",
# 						command = browseFiles)

# button_exit = Button(window,text = "Exit",command = exit)

# # Grid method is chosen for placing
# # the widgets at respective positions
# # in a table like structure by
# # specifying rows and columns
# label_file_explorer.grid(column = 1, row = 1)

# button_explore.grid(column = 1, row = 2)

# button_exit.grid(column = 1,row = 3)

# # Let the window wait for any events
# window.mainloop()


# from tkinter import *
# from PIL import Image,ImageTk

# win = Tk()

# image = Image.open("new.png")
# img = image.resize((50,50),Image.NEAREST)
# my_img = ImageTk.PhotoImage(img)

# label = Label(win,image=my_img)
# label.pack()

# win.mainloop()



# import re

# content = ""
# new_content = ""

# with open("wonderland.txt",'r',encoding='utf-8') as myfile:
#     content = myfile.read()
#     new_content = re.sub("\n"," # ",content)

# print(new_content)

# with open("wonderland.txt",'w',encoding='utf8') as myfile:
#     myfile.write(new_content)


# from unidecode import unidecode

# text = "éèçà"

# text = unidecode(text)

# print(text)

# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m.width))

# print("1"*10000)

# from tkinter import filedialog
# # import os

# # file = filedialog.askopenfile(initialdir="/",title="choix",filetypes=(("PNG","*.png"),))
# # dir = os.path.split(file.name)

# # print(dir[0])

# # with open(f"{dir[0]}/test.txt","w"):
# #     print("reussi")

# from tkinter import *

# fenetre = Tk()

# # fonction appellée lorsque l'utilisateur presse une touche
# def clavier(event):
#     global coords

#     touche = event.keysym

#     if touche == "Up":
#         coords = (coords[0], coords[1] - 10)
#     elif touche == "Down":
#         coords = (coords[0], coords[1] + 10)
#     elif touche == "Right":
#         coords = (coords[0] + 10, coords[1])
#     elif touche == "Left":
#         coords = (coords[0] -10, coords[1])
#     # changement de coordonnées pour le rectangle
#     canvas.coords(rectangle, coords[0], coords[1], coords[0]+25, coords[1]+25)

# # création du canvas
# canvas = Canvas(fenetre, width=250, height=250, bg="ivory")
# # coordonnées initiales
# coords = (0, 0)
# # création du rectangle
# rectangle = canvas.create_rectangle(0,0,25,25,fill="violet")
# # ajout du bond sur les touches du clavier
# canvas.focus_set()
# canvas.bind("<Key>", clavier)
# # création du canvas
# canvas.pack()

# fenetre.mainloop()
# from tkinter import filedialog

# if input("1 ou 2 ?\n") == "1":
#     try:
#         with filedialog.askopenfile(filetypes=(("txt","*.txt"),)) as myfile:
#             print(myfile.name)
#     finally:
#         print("fdp")

print(chr(232))