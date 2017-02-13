from imageTools import *
from imageToolsTools import *
import math
import random



def mirrorImage(pic):
    targetPicture = duplicatePicture(pic)
    for sourceX in range(math.ceil(getWidth(pic)/2), getWidth(pic)):
        for sourceY in range(getHeight(pic)):
            targetX = getWidth(pic) - 1 - sourceX
            targetY = sourceY
            sourcePix = getPixel(pic, sourceX, sourceY)
            targetPix = getPixel(targetPicture, targetX, targetY)
            col = getColor(sourcePix)
            setColor(targetPix, col)
    return targetPicture


def rotateImage(pic):
    """a function that takes in a picture and rotates it 90 degrees to the left"""
    targetPicture = makeEmptyPicture(getHeight(pic), getWidth(pic))
    for sourceX in range(getWidth(pic)):
        for sourceY in range(getHeight(pic)):
            targetY = sourceX
            targetX = getHeight(pic)-1-sourceY
            sourcePixel = getPixel(pic, sourceX, sourceY)
            targetPixel = getPixel(targetPicture, targetX, targetY)
            col = getColor(sourcePixel)
            setColor(targetPixel, col)
    return targetPicture
#picture = makePicture(pickAFile())
#mirroredImage = rotateImage(picture)
#show(mirroredImage)
#wait(mirroredImage)


def copyDemo(smallPic, bigPic):
    targetX = random.randrange(getWidth(bigPic))
    for sourceX in range(getWidth(smallPic)):
        targetY = random.randrange(getHeight(bigPic))
        for sourceY in range(getHeight(smallPic)):
            srcPixel = getPixel(smallPic, sourceX, sourceY)
            tgtPixel = getPixel(bigPic, targetX, targetY)
            setColor(tgtPixel, getColor(srcPixel))
            targetY = targetY + 1
        targetX = targetX + 1
    return bigPic
sPic = makePicture(pickAFile())
bPic = makePicture(pickAFile())
newPic = copyDemo(sPic, bPic)
show(newPic)
wait(newPic)


def scaleDown(pic):
    newPic = makeEmptyPicture(math.ceil(getWidth(pic)/2), math.ceil(getHeight(pic)/2))
    for sourceX in range(getWidth(pic)):
        for sourceY in range(getHeight(pic)):
            targetX = sourceX/2
            targetY = sourceY/2
            sourcePixel = getPixel(pic, sourceX, sourceY)
            targetPixel = getPixel(newPic, targetX, targetY)
            setColor(targetPixel, getColor(sourcePixel))
    return newPic




def scaleUp(pic):
    newPic = makeEmptyPicture(2*getWidth(pic), 2*getHeight(pic))
    for sourceX in range(getWidth(pic)):
        for sourceY in range(getHeight(pic)):
            targetX1 = sourceX*2
            targetX2 = sourceX*2+1
            targetY1 = sourceY*2
            targetY2 = sourceY*2+1
            sourcePixel = getPixel(pic, sourceX, sourceY)
            targetPixel1 = getPixel(newPic, targetX1, targetY1)
            targetPixel2 = getPixel(newPic, targetX1, targetY2)
            targetPixel3 = getPixel(newPic, targetX2, targetY1)
            targetPixel4 = getPixel(newPic, targetX2, targetY2)
            setColor(targetPixel1, getColor(sourcePixel))
            setColor(targetPixel2, getColor(sourcePixel))
            setColor(targetPixel3, getColor(sourcePixel))
            setColor(targetPixel4, getColor(sourcePixel))
    return newPic
#picture = makePicture(pickAFile())
#show(picture)
#wait(picture)
#mirroredImage = scaleUp(picture)
#show(mirroredImage)
#wait(mirroredImage)





