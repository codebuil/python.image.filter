from PIL import Image, ImageDraw
import os


# obtém o diretório atual
current_dir = os.getcwd()
print("O diretório atual é:", current_dir)
# carrega a imagem
image = Image.new('RGB', (800, 600), color = 'blue')
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, 20, 600), fill=(255, 0, 0))
draw.rectangle((20, 0, 40, 600), fill=(0,255, 0))
draw.rectangle((40, 0, 60, 600), fill=(0,0,255))
draw.rectangle((60, 0, 80, 600), fill=(255, 255, 0))
draw.rectangle((80, 0, 100, 600), fill=(255,0, 255))
draw.rectangle((100, 0, 120, 600), fill=(0,255, 255))
draw.rectangle((120, 0, 140, 600), fill=(0,0, 0))
draw.rectangle((140, 0, 160, 600), fill=(255,255, 255))
image.save(current_dir+"\image21.jpg")
