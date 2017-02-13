from imageTools import *
from imageToolsTools import *
import math



def mirrorImage(pic):
    targetPicture = duplicatePicture(pic)
    targetX = math.floor((getWidth(pic)-1)/2)
    targetY = 0
    for sourceX in range(math.ceil(getWidth(pic)/2), getWidth(pic)):
        for sourceY in range(getHeight(pic)):
            sourcePix = getPixel(pic, sourceX, sourceY)
            targetPix = getPixel(targetPicture, targetX, targetY)
            col = getColor(sourcePix)
            setColor(targetPix, col)
            targetY = targetY +1
        targetX = targetX - 1
    return targetPicture
picture = makePicture(pickAFile())
mirroredImage = mirrorImage(picture)
show(mirroredImage)
wait(mirroredImage)