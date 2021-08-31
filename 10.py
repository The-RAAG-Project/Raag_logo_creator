from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

img = Image.open("10.png")
img2 = Image.open("102.png")
draw = ImageDraw.Draw(img2)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("C:/Users/Ankit/Downloads/Bitstream-Vera-Sans-Mono/VeraMono.ttf", 20)
# draw.text((x, y),"Sample Text",(r,g,b))
X, Y = img.size
print(X, Y)
_1_or_0 = "1"
counter = 255
for x in range(X):
    if x%22 == 0:
        for y in range(Y-5):
            if y%22 == 0:
                rgba = img.getpixel((x, y))
                #print(rgb)
                if rgba == (255, 255, 255, 255):
                    draw.text((x, y),"1",(255-counter, counter, counter),font=font)
                    counter -= 1
                else:
                    draw.text((x, y),"0",(0,255,0),font=font)
                #_1_or_0 = random.choice("10")
        print(x, y)
img2.save('xyz.png')
