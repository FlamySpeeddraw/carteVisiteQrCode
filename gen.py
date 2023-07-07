import qrcode
from PIL import Image

#Création de la carte de visite
img_test = Image.new(mode="RGB", size=(240,378),color=(255,255,255))
img_atheme = Image.open('retouche/Athemes.png')
pos = (int((img_test.size[0] - img_atheme.size[0]) / 2), 0)
img_atheme.convert("RGBA")
img_test.convert("RGBA")
img_test.paste(img_atheme,pos)
img_test.show()

#Paramétrage du qr code
qr = qrcode.QRCode(version=1,box_size=1)

#Construction des données du qr code
img_bg = Image.open('logo/Athemes Logo 2023_sigle seul Noir et blanc.png')
img_bg = img_bg.convert('RGB')
qr.add_data(img_bg.tobytes())

#Construction du qr code
qr.make()
img_qr = qr.make_image(fill_color="white", back_color="#2daae1")

#Placement du qr code au centre d'une image
img_bg_qr = Image.open('logo/Athemes Logo 2023_sigle seul Noir et blanc copie.png')
pos = (int(img_bg_qr.size[0] / 2) - int(img_qr.size[0] / 2), int(img_bg_qr.size[1] / 2) - int(img_qr.size[1] / 2))
img_bg_qr.paste(img_qr, pos)

#Sauvegarde de l'image
img_bg_qr.save('test.png')