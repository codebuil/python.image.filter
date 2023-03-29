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
        rb=r-b
        rg=r-g
        gb=g-b
        if rb>25 and rg > 25:
            image.putpixel((x, y), (b,g,r ))

# salva a imagem modificada
image.save(current_dir+"\image16.jpg")
