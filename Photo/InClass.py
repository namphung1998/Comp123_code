from imageTools import *
import time

x = pickAFile()
image = makePicture((x))
show(image)
time.sleep(5)

pic1 = makePicture("butterfly2.jpg")
pic2 = makePicture("horse.jpg")
pic3= makePicture("redDoor.jpg")
show(pic1)
show(pic2)
show(pic3)

print(getWidth(pic2))
print(getHeight(pic2))
a = getPixel(pic3, 25,100)
print(getRGB(a))


# Compute number of pixels based on size of image
pixIt = getPixels(pic1)
pixList = list(pixIt)
print(pixList[1:3])

