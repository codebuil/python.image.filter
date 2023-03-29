from PIL import Image
import os

# obtém o diretório atual
current_dir = os.getcwd()
print("O diretório atual é:", current_dir)
# carrega a imagem
image = Image.open(current_dir+"\image.jpg")

# obtém as dimensões da imagem
width, height = image.size

# percorre todos os pixels da imagem e muda a cor azul para vermelho
for y in range(height):
    for x in range(width):
        # obtém o valor RGB do pixel atual
        r, g, b = image.getpixel((x, y))
        image.putpixel((x, y),(255-r,255-g,255-b ))

# salva a imagem modificada
image.save(current_dir+"\image20.jpg")
