with open("lineBreak.txt","r") as myfile:
    texte = myfile.read()
    texte = texte.replace("\n","_<>_")
with open("lineBreak.txt","w") as myfile:
    myfile.write(texte)