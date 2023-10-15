from PIL import Image, ImageFilter

def watermark(a,b):

    img1 = Image.open(a).convert("RGBA")
    img2 = Image.open(b).convert("RGBA")
    img1 = img1.convert("L")
    threshold = 50
    img1 = img1.point(lambda x: 255 if x > threshold else 0)
    img1 = img1.resize((img1.width//6, img1.height//6))
    img1 = img1.filter(ImageFilter.CONTOUR)
    img1 = img1.point(lambda x: 0 if x == 255 else 255)
    img2.paste(img1, (img2.width//30, img2.height//10), img1)
    img2.show()

watermark("logo1.png","pejaz.jpg")
watermark("logo4.png","original.jpg")