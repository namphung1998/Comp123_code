from imageTools import *
from imageToolsTools import *
def lightenRegion(pic, ulx, uly, lrx, lry):
    for x in range(ulx, lrx+1):
        for y in range(uly, lry+1):
            pixel = getPixel(pic, x,y)
            r = getRed(pixel)
            g = getGreen(pixel)
            b = getBlue(pixel)
            setRed(pixel, r*2)
            setGreen(pixel, g*2)
            setBlue(pixel, b*2)
p1 = makePicture("shops.jpg")
show(p1)
wait(p1)
lightenRegion(p1,10,10,50,150)
show(p1)
wait(p1)

###Part 3
def mirrorHoriz(picture):
    w = getWidth(picture)
    h = getHeight(picture)
    newPic = duplicatePicture(picture)
    show(newPic)
    wait(newPic)
    for x in range(w):
        while (y<h//2):




