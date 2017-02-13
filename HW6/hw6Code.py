from imageTools import *
from imageToolsTools import *

# =======================================
# hw6Code.py
#
# This file contains code I've provided to you.  You may use this file
# to put your answers in, as well.
# =======================================



# ---------------------------------------
# Question 1
def wallpaper(pic, row, column):
    w = getWidth(pic)
    h = getHeight(pic)
    newPic = makeEmptyPicture(column*w, row*h)
    for x in range(w):
        for y in range(h):
            pix = getPixel(pic,x,y)
            for x1 in range(x,(column)*w,w):
                for y1 in range(y,(row)*h,h):
                    newPix = getPixel(newPic,x1,y1)
                    setColor(newPix,getColor(pix))

    return newPic
picture = makePicture(pickAFile())
newPicture = wallpaper(picture,8,2)
show(newPicture)
wait(newPicture)

# Put your definition of wallpaper here,  use the test function in hw6Tests.py to test it 



# ---------------------------------------
# Question 2

def rotateLeft(pic):
    """Takes in a picture object, and it creates a new picture object that has been rotated 90 degrees
   to the left (counter-clockwise) from the original.  It returns the new picture object."""
    newPic = makeEmptyPicture(getHeight(pic), getWidth(pic))
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            newPix = getPixel(newPic, x, y)
            oldX = getWidth(pic) - y - 1
            oldY = x
            oldPix = getPixel(pic, oldX, oldY)
            setColor(newPix, getColor(oldPix))
        repaint(newPic)
    return newPic


# Put your definition of upsideDown here, and use the testing function in hw6Tests.py to test it
def upsideDown(pic):
    newPic = makeEmptyPicture(getWidth(pic),getHeight(pic))
    for x in range(getWidth(newPic)):
        for y in range(getHeight(newPic)):
            newPix = getPixel(newPic,x,y)
            oldX = getWidth(pic)-x-1
            oldY = getHeight(pic)-y-1
            oldPix = getPixel(pic,oldX,oldY)
            setColor(newPix, getColor(oldPix))
        repaint(newPic)
    return newPic