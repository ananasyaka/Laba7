import os
from PIL import Image, ImageFilter

d1 = Image.open('1.jpg')
d2 = Image.open('2.jpg')
d3 = Image.open('3.jpg')
d4 = Image.open('4.jpg')
d5 = Image.open('5.jpg')

Images = [d1,d2,d3,d4,d5]
a=1
os.mkdir("c:\labanumber7\h")
for x in Images:
    img = x
    new_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    new_img.show()
    new_img.save("c:\labanumber7\h\d_new" + str(a) + ".jpg")
    a=a+1