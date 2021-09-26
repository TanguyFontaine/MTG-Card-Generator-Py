import skimage
from skimage import data, io, color, transform, img_as_ubyte
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.color import rgba2rgb
import matplotlib.pyplot as plt

import numpy as np
from PIL import Image

import image_paths as IP
import card as c

def replacePixels(baseImage, layerImage, startRow, startColumn, heigth, width):

    # compute idexes to ensure we stay in stage of arrays
    maxi = min(heigth, layerImage.shape[0]) + startRow
    maxj = min(width, layerImage.shape[1]) + startColumn

    #update image
    for i in range(startRow, maxi):
        for j in range(startColumn, maxj):
            baseImage[i, j] = layerImage[i - startRow, j - startColumn]


def cropeImageToCardFrame(imageData):

    newImageHeight = int(imageData.shape[1] // IP.imageHeightWidtRatio)

    newImageData = imageData[:newImageHeight+1]
    return newImageData



#remove the transparency dimension so that different image files can be compatible
def getImageInThreeDimensions(imageFileName):

    imageFile = io.imread(imageFileName)

    if imageFile.shape[2] == 4:  # test on the number of dimensions : 4 = rgba
        imageFile = img_as_ubyte(rgba2rgb(imageFile)) # reconvert to ubyte

    return imageFile



def displayImageFromFilename(filename, card):
    if filename:

        #retrieveFramePath 
        framePath = card.getFramePath()

        # load image data
        imageFrame = getImageInThreeDimensions(framePath)
        imageFile = getImageInThreeDimensions(filename)

        # resize the image loaded to the frame 
        # !!!!!!!!!!! (check the best way, crop an image or rescale it) !!!!!!!!!!!!!!!!!!!
        # resize method convert pixel values to float. calling img_as_ubyte reconverts it ton integers
        imageFile = cropeImageToCardFrame(imageFile)

        imageFileResizedToFrame = img_as_ubyte(resize(imageFile, (IP.imageFrameHeight, IP.imageFrameWidth), anti_aliasing=True))

        replacePixels(imageFrame, imageFileResizedToFrame, IP.startFrameRow, IP.startFrameColumn, IP.imageFrameHeight, IP.imageFrameWidth)

        # showing image
        plt.imshow(imageFrame)

        plt.show() # display opened elements
