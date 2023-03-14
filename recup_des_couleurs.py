from PIL import Image


repertoire = input("Veuillez me donner le répètoire de l'image :")

img = Image.open(repertoire)

largeur, hauteur = img.size
pixels = []

for y in range(hauteur):
    for x in range(largeur):
        couleur = img.getpixel((x, y))
        pixel = {"couleur": couleur, "coord": (x, y)}
        pixels.append(pixel)
    
print(pixels)