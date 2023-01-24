from rembg import remove
from PIL import Image


input_path = 'alcon.jpg'
output_path = 'salida.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)

print('Fondo de imagen removido!')

