from imageTools import *
from imageToolsTools import *

###Question 1
def blackWhite(picture, cutoff):
    targetPic = duplicatePicture(picture)
    for x in range(getWidth(targetPic)):
        for y in range(getHeight(targetPic)):
            pix = getPixel(targetPic, x, y)
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            if ((r+g+b)/3)>cutoff:
                setColor(pix, white)
            else:
                setColor(pix, black)
    return targetPic
#pic = makePicture(pickAFile())
#show(pic)
#wait(pic)
#newPic = blackWhite(pic, 205)
#show(newPic)
#wait(newPic)


###Question 2
def gradualBlend(picture1, picture2):
    width = min(getWidth(picture1), getWidth(picture2))
    height = min(getHeight(picture1), getHeight(picture2))
    newPic = makeEmptyPicture(width, height)
    w2 = 0
    for x in range(getWidth(newPic)):
        w2 = w2 + (1/getWidth(newPic))
        w1 = 1.0-w2
        for y in range(getHeight(newPic)):
            pix1 = getPixel(picture1, x, y)
            r1, g1, b1 = getRGB(pix1)
            pix2 = getPixel(picture2, x, y)
            r2, g2, b2 = getRGB(pix2)
            pix = getPixel(newPic, x, y)
            setRed(pix, w1 * r1 + w2 * r2)
            setGreen(pix, w1 * g1 + w2 * g2)
            setBlue(pix, w1 * b1 + w2 * b2)
    return newPic
pic1= makePicture(pickAFile())
pic2 = makePicture(pickAFile())
pic3 = gradualBlend(pic1, pic2)
show(pic3)
wait(pic3)
