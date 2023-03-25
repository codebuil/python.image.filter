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
        
        # verifica se o pixel é azul (R=0, G=0, B=255) e o substitui por vermelho (R=255, G=0, B=0)
        #if r == 0 and g == 0 and b == 255:
        image.putpixel((x, y), (255-r, 255-g, 255))

# salva a imagem modificada
image.save(current_dir+"\image3.jpg")
