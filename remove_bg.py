from rembg import remove
# fornece ao interpretador python recursos de edição de imagem
from PIL import Image
from pathlib import Path

img_entrada = Path(r"C:/Users/muril\Documents/GitHub/python/PURfect_Mart.png")
img_saida = Path(r"C:/Users/muril\Documents/GitHub/python/output.png")
input = Image.open(img_entrada)
output = remove(input)
#salvando a imagem
output.save(img_saida)