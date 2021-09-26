import numpy as np
from PIL import Image, ImageDraw, ImageFont

import symbols_type as S
import image_paths as IP
import card as c


# ***************************************************************************
def cropeImageToCardFrame(image):
    imageWidthHeightRatio = image.width / image.height

    if imageWidthHeightRatio <= IP.frameWidthHeightRatio: # crop bottom
        newImageHeight = int(image.width // IP.frameWidthHeightRatio)
        image = image.crop((0, 0, image.width, newImageHeight))
    else: # crop right
        newImageWidth = int(image.height * IP.frameWidthHeightRatio)
        image = image.crop((0, 0, newImageWidth, image.height))

    return image



# ***************************************************************************
# make sure that the transparency dimension is created so that different image files can be compatible
def getImageInFourDimensions(imageFileName):

    imageFile = Image.open(imageFileName)

    if imageFile.mode != 'RGBA':  # test on the number of dimensions : 4 = rgba
        imageFile = imageFile.convert('RGBA') # reconvert to ubyte

    return imageFile



# ***************************************************************************
def addManaSymbolsToImage(imageFrame, manaSymbols, leftColumn):

    symbol = manaSymbols[0]
    nbToDisplay = manaSymbols[1]

    if symbol == S.SymbolsType.Grey:
        return imageFrame
    else:
        for i in range(nbToDisplay):
            imageManaSymbol = getImageInFourDimensions(symbol.imagePath)
            imageFrame.paste(imageManaSymbol, (leftColumn, IP.manaCostTopRaw), imageManaSymbol) 

    return imageFrame



# ***************************************************************************
def addManaSymbolToFrame(imageFrame, symbolPath, newSize, leftColumn, topLine, offset):

    # get the image of the mana symbol
    imageManaSymbol = getImageInFourDimensions(symbolPath)

    if newSize > 0:
        imageManaSymbol = imageManaSymbol.resize((newSize, newSize))

    # paste it into the frame
    imageFrame.paste(imageManaSymbol, (leftColumn, topLine), imageManaSymbol)

    # width of mana symbol + space between two symbols = 55 -> left column of the newt mana symbol
    leftColumn += offset 

    return imageFrame, leftColumn



# ***************************************************************************
def addTextToSymbol(imageFrame, fontSize, leftTopCorner, nbToDisplay, color):
    fontNumbers = ImageFont.truetype(IP.numbers2, fontSize)
    textImage = Image.new("RGBA", imageFrame.size, (255,255,255,0))
    drawingContext = ImageDraw.Draw(textImage)
    drawingContext.text(leftTopCorner, str(nbToDisplay), font=fontNumbers, fill=color)
    imageFrame = Image.alpha_composite(imageFrame, textImage)

    return imageFrame



# ***************************************************************************
def displayManaCost(imageFrame, manaCost):

    i = len(manaCost) - 1

    leftColumn = IP.manaCostRightColumn - IP.manaSymbolWidth

    # going from right to left to display the symbols
    while i >= 0:
        manaSymbols = manaCost[i]

        symbol = manaSymbols[0]
        nbToDisplay = manaSymbols[1]

        if symbol == S.SymbolsType.Grey:
            imageFrame, leftColumn = addManaSymbolToFrame(imageFrame, symbol.imagePath, 0, leftColumn, IP.manaCostTopRaw, -53)

            fontSize = IP.greyManaNumberFontSize

            if nbToDisplay == 1:
                leftColumn += 5
            elif nbToDisplay >= 10:
                leftColumn -= 5
                fontSize -= 5

            imageFrame = addTextToSymbol(imageFrame, fontSize, (leftColumn + 65, IP.manaCostTopRaw - 4), nbToDisplay, (0, 0, 0, 255))

        else:
            for j in range(nbToDisplay):
                imageFrame, leftColumn = addManaSymbolToFrame(imageFrame, symbol.imagePath, 0, leftColumn, IP.manaCostTopRaw, -53)

        i -= 1

    return imageFrame



# ***************************************************************************
def displaySymbolsImages(imageFrame, symbols):
    
    # offset between symbols on the same line
    offset = 0

    # keep track of the line we're at for the offset
    lastlLineNumber = 0

    for i in range(len(symbols)):
        symbolWithPositions = symbols[i]

        symbol = symbolWithPositions[0]
        nbToDisplay = symbolWithPositions[1]
        columnNumber = symbolWithPositions[2]
        lineNumber = symbolWithPositions[3]

        # reset offset on new lines of symbols
        if lastlLineNumber != lineNumber:
            offset = 0 

        leftPixel = IP.abilitiesTextboxTopLeftCorner[0] + offset + (columnNumber * 16) 
        topPixel = IP.abilitiesTextboxTopLeftCorner[1] + (lineNumber * 35)

        if symbol == S.SymbolsType.Grey:
            offset = 7
            imageFrame, leftPixel = addManaSymbolToFrame(imageFrame, symbol.imagePath, 35, leftPixel, topPixel, offset)

            # recalibraite because 1 is thiner than other numbers
            charOffset = 2
            if nbToDisplay == 1:
                charOffset = 5
            imageFrame = addTextToSymbol(imageFrame, IP.greyManaNumberFontSize - 12, (leftPixel + charOffset, topPixel - 4), nbToDisplay,(0, 0, 0, 255))

        elif symbol == S.SymbolsType.LoyaltyDown or symbol == S.SymbolsType.LoyaltyUp:
            leftPixel = IP.loyaltyLeftSide

            # adjust symbols and text on the frame
            symbolOffset = 8
            textOffset = 15
            offset = 7
            nbToDisplayStr = str(nbToDisplay)

            if symbol == S.SymbolsType.LoyaltyUp:
                symbolOffset = 15

            if nbToDisplay > 0:
                nbToDisplayStr = '+' + nbToDisplayStr
            elif nbToDisplay == 0:
                textOffset = 30

            imageFrame, leftPixel = addManaSymbolToFrame(imageFrame, symbol.imagePath, 0, leftPixel, topPixel - symbolOffset, offset)
            imageFrame = addTextToSymbol(imageFrame, IP.greyManaNumberFontSize - 8, (leftPixel + textOffset, topPixel), nbToDisplayStr, (255, 255, 255, 255))

        else:
            for j in range(nbToDisplay):
                offset = 37
                imageFrame, leftPixel = addManaSymbolToFrame(imageFrame, symbol.imagePath, 35, leftPixel, topPixel, offset)
            offset = 7

        lastlLineNumber = lineNumber

    return imageFrame



# ***************************************************************************
def displayPowerToughness(card, imageFrame, drawingContext):

    PTleftPos = IP.powerToughnessTextboxTopLeftCorner[0]
    PTtopPos = IP.powerToughnessTextboxTopLeftCorner[1]
    fontSize = IP.powerToughnessDefaultFontSize

    powerToughnessText = card.power + '/' + card.toughness

    # readjust the text depending on the power or toughness
    if card.power == "1":
        PTleftPos += 6
    if card.toughness == "1":
        PTleftPos += 6
    if len(card.power) > 1:
        fontSize -= 4
        PTleftPos -= 6
        PTtopPos += 3
    if len(card.toughness) > 1:
        fontSize -= 4
        PTleftPos -= 6
        PTtopPos += 3

    powerToughnessFont = ImageFont.truetype(IP.numbers2, size=fontSize)

    drawingContext.text((PTleftPos, PTtopPos), powerToughnessText, font=powerToughnessFont, fill=(0, 0, 0, 255))

    return imageFrame, drawingContext



# ***************************************************************************
def displayLoyalty(card, imageFrame, drawingContext):

    #display the frame loyalty
    loyaltyImage = getImageInFourDimensions(IP.loyalty)

    loyaltyTextboxTopLeftCorner = (0, 0)

    if card.isACreature():
        loyaltyTextboxTopLeftCorner = IP.loyaltyTextboxTopLeftCorner2
    else:
        loyaltyTextboxTopLeftCorner = IP.loyaltyTextboxTopLeftCorner
    
    imageFrame.paste(loyaltyImage, loyaltyTextboxTopLeftCorner, loyaltyImage)

    # add the loyalty number
    loyaltyFont = ImageFont.truetype(IP.numbers, size=IP.loyaltyFontSize)
    
    shifter = 55
    if card.loyalty and int(card.loyalty) > 9:
        shifter -= 12   
    if card.loyalty and int(card.loyalty) > 99:
        shifter -= 12

    drawingContext.text((loyaltyTextboxTopLeftCorner[0] + shifter, loyaltyTextboxTopLeftCorner[1] + 20), card.loyalty, font=loyaltyFont, fill=(255, 255, 255, 255))

    return imageFrame, drawingContext



# ***************************************************************************
def displayImageFromFilename(filename, card):
    if filename:

        #retrievethe file path of the frame image
        framePath = card.getFramePath()

        # load image data
        imageFrame = getImageInFourDimensions(framePath) # the base image on which everything will be paste
        imageFile = getImageInFourDimensions(filename)

        # resize the image loaded to the frame 
        # !!!!!!!!!!! (check the best way, crop an image or rescale it, take ecnter of the image ? top left corner ?) !!!!!!!!!!!!!!!!!!!
        # resize method convert pixel values to float. calling img_as_ubyte reconverts it ton integers
        imageFile = cropeImageToCardFrame(imageFile)

        # resize the image to fit the whiole frame
        imageFile = imageFile.resize((IP.imageFrameWidth, IP.imageFrameHeight))

        # fuse the 2 images
        imageFrame.paste(imageFile, (IP.startFrameColumn, IP.startFrameRow), imageFile)

        # add the logo
        imageLogo = getImageInFourDimensions(IP.logo)
        imageFrame.paste(imageLogo, (IP.logoLeftColumn, IP.logoTopRow), imageLogo)

        imageFrame = displayManaCost(imageFrame, card.manaCost)

        imageFrame = displaySymbolsImages(imageFrame, card.abilitiesSymbols)

        ###########################################################
        # make a blank image for the text, initialized to transparent text color
        textImage = Image.new("RGBA", imageFrame.size, (255,255,255,0))
        
        # compute text to display
        typeText = card.buildTypeText()
        flavorTextTopRaw = IP.flavorTextTopLeftCorner[1] - ((len(card.flavorText) / 65 )* 20 ) 

        typeFontSize = IP.typesDefaultFontSize
        if len(typeText) > 40:
            typeFontSize -= 3

        # get fonts
        nameFont = ImageFont.truetype(IP.mermaidFontPath, size=IP.nameDefaultFontSize)
        typesFont = ImageFont.truetype(IP.mermaidFontPath, size=typeFontSize)
        abilitiesFont = ImageFont.truetype(IP.monospace, size=IP.abilitiesDefaultFontSize)
        flavorTextFont = ImageFont.truetype(IP.italic, size=IP.flavorTextFontSize)



        # get a drawing context 
        drawingContext = ImageDraw.Draw(textImage)

        # draw text
        drawingContext.text(IP.nameTextboxTopLeftCorner, card.name, font=nameFont, fill=(0, 0, 0, 255))
        drawingContext.text(IP.typesTextboxTopLeftCorner, typeText, font=typesFont, fill=(0, 0, 0, 255))
        drawingContext.text(IP.abilitiesTextboxTopLeftCorner, card.abilities, font=abilitiesFont, fill=(0, 0, 0, 255))

        if card.isACreature():
            imageFrame, drawingContext = displayPowerToughness(card, imageFrame, drawingContext)

        if card.isAPlaneswalker():
            imageFrame, drawingContext = displayLoyalty(card, imageFrame, drawingContext)
        
        drawingContext.text((IP.flavorTextTopLeftCorner[0],flavorTextTopRaw), card.flavorText, font=flavorTextFont, fill=(0, 0, 0, 255))

        finalImage = Image.alpha_composite(imageFrame, textImage)
        ###########################################################

        # display the main image
        finalImage.show() 
