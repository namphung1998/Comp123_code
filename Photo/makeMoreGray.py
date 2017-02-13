from imageTools import *
from imageToolsTools import *
picture = makePicture(pickAFile())

def makeMoreGray(pic):
    for pixel in getPixels(pic):
            r = getRed(pixel)
            g = getGreen(pixel)
            b = getBlue(pixel)

            setRed(pixel, ((3*r)+g+b)//5)
            setGreen(pixel, (r+(3*g)+b)//5)
            setBlue(pixel, (r+g+(3*b))//5)


show(picture)
wait(picture)
makeMoreGray(picture)
show(picture)
wait(picture)
makeMoreGray(picture)
show(picture)
wait(picture)