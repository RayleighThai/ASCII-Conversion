# In order to run, OpenCV, Ascii_magic and img_kit must but install. Can be install via pip instal [module]
# Install wkhtmltoX program for translate HTML file into img file for collate into final product video
import cv2
import ascii_magic
import imgkit
from PIL import ImageEnhance
import os
import shutil

# If folder not exists, create them to store files.
if not os.path.exists('ascii'):
    os.makedirs('ascii')
if not os.path.exists('html'):
    os.makedirs('html')
if not os.path.exists('images'):
    os.makedirs('images')

# density can be change. If no given density, ascii_magic will use default ascii density (check its manual)
#density = 'Ñ@#W$9876543210?!abc;:+=-,._ '

vid = cv2.VideoCapture("rickroll.mp4")  #Insert Video file here.
count = 0
flag =1 

# This is Video convert each frame into still images
while flag:
    flag, image = vid.read()
    try:
        cv2.imwrite("images/frame%d.jpg" % count, image)
    except:
        break
    count += 1

# This is from each Images, conversion to HTML as Ascii_magic properties. 
for i in range(count):
    s = "images/frame" + str(i) + ".jpg"
    #print(s)
    output = ascii_magic.from_image(s)
    output.image = ImageEnhance.Brightness(output.image).enhance(1.85) #enhance image
    output.to_html_file("html/frame" + str(i) + ".html", columns=200, width_ratio= 2)

# Create a path to wkhtmltoX executable for the program to run
path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe' 

# Convert HTML file back to image for compilation into video
config = imgkit.config(wkhtmltoimage = path)
for i in range(count):
    imgkit.from_file("html/frame" + str(i) + ".html", "ascii/frame" + str(i) + ".jpg", config=config)
frame = cv2.imread("ascii/frame0.jpg")
ih, iw, il = frame.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# Change 24.08 to Fps frame of original video by checking its property
video = cv2.VideoWriter("product.mp4", fourcc, 24.08, (iw, ih)) 

# Compile frame into one single video
for i in range(count):
    image = "ascii/frame" + str(i) + ".jpg"
    video.write(cv2.imread(image))

# Remove file to prevent residues from previous video conversion compile with new video conversion. 
shutil.rmtree("html")
shutil.rmtree("ascii")
shutil.rmtree("images")

cv2.destroyAllWindows() # Clean up all 
video.release()