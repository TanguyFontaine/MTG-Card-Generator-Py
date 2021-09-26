import PySimpleGUI as psg
import os.path

import ressources as rsc
import frame_colors as fc
import card as c
import card_types as ct
import card_super_types as cst
import mana_cost_factory as msf

import image_rendering as ir
import image_paths as IP
import ui


# ***************************************************************************
def buildCardTypes(windowValues):
    cardTypes = []
    for t in ct.CardTypes:
        if (windowValues[t.key]):
            cardTypes.append(t.text)
    return cardTypes


# ***************************************************************************
def buildCardSuperTypes(windowValues):
    cardSuperTypes = []
    for st in cst.SuperTypes:
        if (windowValues[st.key]):
            cardSuperTypes.append(st.text)
    return cardSuperTypes



# ***************************************************************************
def createNewCardWithAttributes(name, cardTypes, cardSuperTypes, cardSubTypes, frameColor, manaSymbols, abilities, abilitiesSymbols, power, toughness, loyalty, flavorText):
    newCard = c.Card(name)
    newCard.types = cardTypes
    newCard.superTypes = cardSuperTypes
    newCard.subTypes = cardSubTypes
    newCard.frameColor = frameColor
    newCard.manaCost = manaSymbols
    newCard.abilities = abilities
    newCard.abilitiesSymbols = abilitiesSymbols
    newCard.power = power
    newCard.toughness = toughness
    newCard.loyalty = loyalty
    newCard.flavorText = flavorText

    return newCard

 
# ***************************************************************************
# insert \n characters so that the abilities can fit in the frame
# transform symbols code into symbols
def recalibrateText(abilitiesText, lineLength):

    symbols = []

    index = 0
    textLentgh = len(abilitiesText)
    lastSpaceIndex = 0 # to avoid spliting a word in half

    lineNb = 0
    columnNb = 0  # counter of characters, once it reach a given value (50), insert a \n 1 char == 1 column

    symbolStr = ""
    isParsingSymbol = False
    symbolPos = 0
    startSymbolStrIndex = 0

    while index < textLentgh:
        if columnNb == lineLength:
            abilitiesText = abilitiesText[:lastSpaceIndex] + '\n' + abilitiesText[lastSpaceIndex + 1:]
            textLentgh = len(abilitiesText)
            columnNb = index - lastSpaceIndex # to keep the count of the word currently parsed
            lineNb += 1

        if abilitiesText[index] == '\n':
            columnNb = -1 # set to -1 becaus eof the +1 at the end of the loop
            lineNb += 1
        elif abilitiesText[index] == ' ':
            lastSpaceIndex = index
        elif abilitiesText[index] == '[':
            isParsingSymbol = True
            symbolPos = columnNb
            startSymbolStrIndex = index
        elif abilitiesText[index] == ']':
            symbolStr += abilitiesText[index]

            symbol = msf.extractSymbols(symbolStr)[0]
            if symbol == "error":
                return "error", ["error"]

            symbolWithPosition = (symbol[0], symbol[1], symbolPos, lineNb)
            symbols.append(symbolWithPosition)

            # update the text
            abilitiesText = abilitiesText[:startSymbolStrIndex] + msf.getNeededSpace(symbol[0], symbol[1]) + abilitiesText[index + 1:]
            textLentgh = len(abilitiesText)

            # We replace the symbol code by spaces, so we go back a little to avoid missing chars
            index = startSymbolStrIndex - 1
            columnNb = symbolPos - 1

            # reset symbol string
            symbolStr = ""
            isParsingSymbol = False

        if isParsingSymbol:
            symbolStr += abilitiesText[index]

        columnNb += 1
        index += 1

    return abilitiesText, symbols


# ***************************************************************************
def buildCard(windowValues):
    types = buildCardTypes(windowValues)
    superTypes = buildCardSuperTypes(windowValues)
    manaCost = msf.extractSymbols(windowValues[rsc.manaSymbolsKey])
    frameColor = fc.getFrameColorFromText(windowValues[rsc.frameColorsComboboxKey])
    abilities, abilitiesSymbols = recalibrateText(windowValues[rsc.abilitiesTextboxKey], IP.abilitiesLineLength)
    flavorTextWithSymbols = recalibrateText(windowValues[rsc.flavorTextboxKey], IP.flavorTextLineLength)
    card = createNewCardWithAttributes(windowValues[rsc.cardNameTextboxKey], types, superTypes, windowValues[rsc.subtypesTextboxKey], 
                                       frameColor, manaCost, abilities, abilitiesSymbols, windowValues[rsc.powerTextboxKey], 
                                       windowValues[rsc.toughnessTextboxKey], windowValues[rsc.loyaltyTextboxKey], flavorTextWithSymbols[0])
    return card



# Main program
# ******************************************************************************************************************************************************
# ******************************************************************************************************************************************************

window = ui.buildMainWindow()

# Main loop
while True:
    event, values = window.read()

    if event == rsc.generateButtonText:

        #retrieve UI data
        card = buildCard(values)

        if card.isValid():
            imageFile = values[rsc.imageFileKey]

            # build card image
            if imageFile and imageFile.lower().endswith(("jpg", ".png", ".gif")):
                ir.displayImageFromFilename(imageFile, card)
            else:
                errorWindow = psg.Window(rsc.errorWindowTitle, layout=[[psg.Text(rsc.wrongFileTypeErrorMessage)]], margins=(200, 50)).read()
    
    elif event == rsc.isCreatureCheckboxKey:
        window[rsc.powerTextboxKey].update(disabled= not values[rsc.isCreatureCheckboxKey])
        window[rsc.toughnessTextboxKey].update(disabled= not values[rsc.isCreatureCheckboxKey])

    elif event == rsc.isPlaneswalkerCheckboxKey:
        window[rsc.loyaltyTextboxKey].update(disabled= not values[rsc.isPlaneswalkerCheckboxKey])

    elif event == rsc.helpButtonText:
        helpWindow = psg.Window(rsc.helpWindowTitle, layout=[[psg.Text(rsc.helpText)]], margins=(200, 120)).read()

    elif event == psg.WIN_CLOSED:
        break

window.close()
