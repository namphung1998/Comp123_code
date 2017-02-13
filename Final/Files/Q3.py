from imageTools import *
from imageToolsTools import *
import time

# In this question you will write a function named
# mergeRGB that takes three images and returns a new
# image. The three images will be merged by taking the
# red chanel from the first image, the green chanel from
# the second image, and the blue chanel from the third
# image. This will result in a new image which will look
# pretty cool (in my opinion). The images may not be the
# same size so you should make your new image have the
# minimum width of the three images and the minimum
# height of the three images.


def mergeRGB(rImage, gImage, bImage):
    width = min(getWidth(rImage), getWidth(gImage), getWidth(bImage))
    height = min(getHeight(rImage), getHeight(gImage), getHeight(bImage))
    newPic = makeEmptyPicture(width,height)
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            pix = getPixel(newPic,x,y)
            pixR = getPixel(rImage, x, y)
            pixG = getPixel(gImage, x, y)
            pixB = getPixel(bImage, x, y)
            setRed(pix, getRed(pixR))
            setGreen(pix, getGreen(pixG))
            setBlue(pix, getBlue(pixB))
    return newPic

r = makePicture("blackcat.jpg")
g = makePicture("jungle2.jpg")
b = makePicture("blueMotorcycle.jpg")
ni = mergeRGB(r,g,b)
show(ni)
time.sleep(15)