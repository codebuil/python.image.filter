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
        
        
        #if r >200 and g > 200  and b >200:
        image.putpixel((x, y), (b,b,g ))

# salva a imagem modificada
image.save(current_dir+"\image12.jpg")
