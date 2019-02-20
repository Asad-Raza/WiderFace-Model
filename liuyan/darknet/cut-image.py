from PIL import Image

img=Image.open("/home/liuyan/Desktop/darknet/data/dog.jpg")
area=(132,214,313,542)
cropped_img= img.crop(area)

cropped_img.show()

