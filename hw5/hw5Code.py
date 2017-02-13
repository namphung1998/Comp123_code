#  Homework 3
#  Nam Phung
#  COMP123 - 03


from imageTools import *
from imageToolsTools import *

# Question 1
def encrypt(fileName1, fileName2, cipher):
    """a function that takes in a text file, encrypts it using the cipher dictionary and writes the
    encrypted text to another file"""
    file1 = open(fileName1, "r")
    file2 = open(fileName2, "w")
    for line in file1:
        for el in line:
            i = el.lower()
            if i in cipher.keys():
                file2.write(cipher[i])
            else:
                file2.write(i)
    file1.close()
    file2.close()


# Question 2
def colorSwap(picture):
    """a function that takes a picture object, make a copy of it and edit that copy
    so that the color channels are swapped"""
    newPic = duplicatePicture(picture)
    for pix in getPixels(newPic):
        r = getRed(pix)
        g = getGreen(pix)
        b = getBlue(pix)
        setBlue(pix, r)
        setRed(pix, g)
        setGreen(pix, b)
    return newPic



# Question 3
def redToCyan(Picture):
    """a function that takes a picture and modify certain pixels (those that are
    red enough) to change their colors to cyan"""
    pic = duplicatePicture(Picture)
    for pixel in getPixels(pic):
        r = getRed(pixel)
        b = getBlue(pixel)
        g = getGreen(pixel)
        if (r>b) and (r>g):
            r = 0
            g = 255
            b = 255
    return pic

