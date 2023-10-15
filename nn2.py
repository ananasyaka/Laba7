
from PIL import Image
img = Image.open('original.jpg')
img.show()
# изменяем размер
new_img = img.resize((188, 231))
new_img.show()
# сохранение картинки
new_img.save('C:\Labanumber7\small.png')
new_img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
new_img1.show()
new_img1.save('C:\Labanumber7\horizont.png')
new_img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
new_img2.show()
new_img2.save('C:\Labanumber7\wertical.png')