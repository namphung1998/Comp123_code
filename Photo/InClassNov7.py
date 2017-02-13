from imageTools import *
from imageToolsTools import *
import math


def simpleBlend(pic1, pic2):
    newPic = makeEmptyPicture(getWidth(pic1), getHeight(pic1))
    for x in range(getWidth(newPic)):

        for y in range(getHeight(newPic)):
            pix1 = getPixel(pic1, x, y)
            r1, g1, b1 = getRGB(pix1)
            pix2 = getPixel(pic2, x, y)
            r2, g2, b2 = getRGB(pix2)
            pix = getPixel(newPic, x, y)
            setRed(pix, (r1+r2)/2)
            setGreen(pix, (g1+g2)/2)
            setBlue(pix, (b1+b2)/2)
        repaint(newPic)

    return newPic


def blendPicture(pic1, pic2):
    width = min(getWidth(pic1), getWidth(pic2))
    height = min(getHeight(pic1), getHeight(pic2))
    newPic = makeEmptyPicture(width, height)
    for x in range(getWidth(newPic)):

        for y in range(getHeight(newPic)):
            pix1 = getPixel(pic1, x, y)
            r1, g1, b1 = getRGB(pix1)
            pix2 = getPixel(pic2, x, y)
            r2, g2, b2 = getRGB(pix2)
            pix = getPixel(newPic, x, y)
            setRed(pix, (r1+r2)/2)
            setGreen(pix, (g1+g2)/2)
            setBlue(pix, (b1+b2)/2)
        repaint(newPic)

    return newPic
#picture1 = makePicture(pickAFile())
#show(picture1)
#wait(picture1)
#picture2 = makePicture(pickAFile())
#show(picture2)
#wait(picture2)
#pic = blendPicture(picture1, picture2)
#show(pic)
#wait(pic)


def weightedBlend(pic1, pic2, w1):
    w2 = 1.0-w1
    width = min(getWidth(pic1), getWidth(pic2))
    height = min(getHeight(pic1), getHeight(pic2))
    newPic = makeEmptyPicture(width, height)
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            pix1 = getPixel(pic1, x, y)
            r1, g1, b1 = getRGB(pix1)
            pix2 = getPixel(pic2, x, y)
            r2, g2, b2 = getRGB(pix2)
            pix = getPixel(newPic, x, y)
            setRed(pix, w1*r1+w2*r2)
            setGreen(pix, w1*g1+w2*g2)
            setBlue(pix, w1*b1+w2*b2)
        repaint(newPic)

    return newPic
picture1 = makePicture(pickAFile())
picture2 = makePicture(pickAFile())
pic = weightedBlend(picture1, picture2, 0.1)
show(pic)
wait(pic)

