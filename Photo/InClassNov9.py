from imageTools import *
from imageToolsTools import *

def backSubstitute(forePic, oldBack, newBack):
    newPic = makeEmptyPicture(getWidth(forePic), getHeight(forePic))
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            pix1 = getPixel(forePic, x, y)
            pix2 = getPixel(oldBack, x, y)
            pix3 = getPixel(newBack,x ,y)
            pix4 = getPixel(newPic, x, y)
            col1 = getColor(pix1)
            col2 = getColor(pix2)
            d = abs(distance(col1, col2))
            if d <100:
                setColor(pix4, getColor(pix3))
            else:
                setColor(pix4, col1)
    return newPic
pic1 = makePicture(pickAFile())
show(pic1)
pic2 = makePicture(pickAFile())
pic3 = makePicture(pickAFile())
pic = backSubstitute(pic1, pic2, pic3)
show(pic)
wait(pic)

def chromakey(forePic, newBack):
    newPic = makeEmptyPicture(getWidth(forePic), getHeight(forePic))
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            forePix = getPixel(forePic, x, y)
            newPix = getPixel(newPic, x, y)
            backPix = getPixel(newBack, x, y)
