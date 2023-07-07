from PIL import Image

#Ouverture de toutes les images
img_atheme = Image.open('retouche/Athemes.png')
img_BB = Image.open('retouche/BB.png')
img_bg = Image.open('retouche/carte_bg.png')
img_carte = Image.new(mode="RGB", size=(240,378),color=(255,255,255))

#Calculs des positions des images
pos_athemes = (int((img_carte.size[0] - img_atheme.size[0]) / 2), 0)
pos_BB= (int((img_carte.size[0] - img_BB.size[0]) / 2), img_carte.size[1] - img_BB.size[1])
pos_bg = (img_carte.size[0] - img_bg.size[0], img_carte.size[1] - img_bg.size[1] - 20)

#Fusion et sauvegarde des images
img_carte.paste(img_atheme,pos_athemes, img_atheme)
img_carte.paste(img_bg,pos_bg,img_bg)
img_carte.paste(img_BB,pos_BB,img_BB)
img_carte.save('cartes de visite/modele_carte.png')