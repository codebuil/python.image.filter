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
for x in range(width):
    for y in range(height):
        # obtém o valor RGB do pixel atual
        r, g, b = image.getpixel((x, y))
        rg=r-g
        rb=r-b
        gb=g-b
        if rb<0:
            rb=-rb

        if rg<0:
            rg=-rg

        if gb<0:
            gb=-gb
        
        
        if rb<50 and rg<50  and gb<50:
            image.putpixel((x, y), (r,g,255 ))

# salva a imagem modificada
image.save(current_dir+"\image13.jpg")
