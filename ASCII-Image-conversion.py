# Ascii_magic, wkhtmltoX and img_kit must but install in order to run. Can be install via pip instal [module]
# Install wkhtmltoX program for translate HTML file into img file for collate into final product video
import ascii_magic
import imgkit
from PIL import ImageEnhance
import os

image = "garden.jpg" #insert file here
output = ascii_magic.from_image(image)
output.image = ImageEnhance.Brightness(output.image).enhance(1.25)
output.to_html_file("product.html", columns=200, width_ratio= 2)

# Create a path to wkhtmltoX executable for the program to run
path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe' 

config = imgkit.config(wkhtmltoimage = path)
imgkit.from_file("product.html", "product.jpg", config=config)
os.remove("product.html")