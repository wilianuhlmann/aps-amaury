from app import filtroFauna, filtroFlora
from PIL import Image
from matplotlib import pyplot as plt

imgFlora = Image.open("img/floresta-amazonia.jpg")
resfl = filtroFlora(imgFlora)
plt.imshow(resfl)
plt.show()
imgFauna = Image.open("img/arara-azul-voando.jpg")
resfa = filtroFauna(imgFauna)
plt.imshow(resfa)
plt.show()

# Juntando imagens.

plt.imgshow(resfa, resfl)
