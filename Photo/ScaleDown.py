from imageTools import *
from imageToolsTools import *
def scaleDown(picture):
    w = getWidth(picture)
    h = getHeight(picture)
    newPic = makeEmptyPicture(w*2,h*2)
    for x in range(w*2):
        for y in range(h*2):
            originalPix = getPixel(picture, x/2, y/2)
            targetPix = getPixel(newPic, x, y)
            setColor(targetPix, getColor(originalPix))

    return newPic
pic = makePicture(pickAFile())
show(pic)
wait(pic)
for i in range(10):
    pic = scaleDown(pic)
    show(pic)
    wait(pic)


