
from PIL import Image
myimage = Image.open('kovver.jpg')
myimage.show()
print("Данные об изображении:")
print(myimage.format, myimage.size, myimage.mode)