from imageTools import *
from imageToolsTools import *
def changeRed(picture, factor):
    for pix in getPixels(picture):
        redVal = getRed(pix) #gets the red value of every pixel in the picture
        newVal = factor * redVal  #changes the red value of every pixel in a picture
        setRed(pix, newVal)
#horsePic = makePicture("horse.jpg")
#show(horsePic)
#wait(horsePic)
#changeRed(horsePic, -2.0)
#repaint(horsePic)
#wait(horsePic)


##Grayscale Variations
def grayscale(pic):
    newPic = copyPicture(pic)
    for pixel in getPixels(newPic):
        r = getRed(pixel)
        g = getGreen(pixel)
        b = getBlue(pixel)
        lumin = (r+g+b)/3
        setColor(pixel, makeColor(lumin,lumin,lumin))
    return newPic

#show(grayscale(a))

#wait(a)

##Image Manipulation
def removeBlue(pic):
    for pixel in getPixels(pic):
        setBlue(pixel,0)


##fixGreen:
def fixGreen(pic, val):
    for pixel in getPixels(pic):
        setGreen(pixel, val)
a = makePicture(pickAFile())
show(a)
wait(a)
fixGreen(a, 5)
repaint(a)
wait(a)


