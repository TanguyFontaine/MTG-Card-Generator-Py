import frame_colors as fc
import card_types as t

class Card(object):
    """modelisation d'une carte"""

    name = "" 
    types = []
    superTypes = []
    subTypes = ""
    frameColor = fc.FrameColors.Colorless
    manaCost = []
    abilities = ""
    abilitiesSymbols = []
    flavorText = ""
    power = 0
    toughness = 0
    loyalty = 0

    # ***************************************************************************
    def __init__(self, newName):
        self.name = newName


    # ***************************************************************************
    def isACreature(self):
        return t.CardTypes.Creature.text in self.types

    
    # ***************************************************************************
    def isAPlaneswalker(self):
        return t.CardTypes.Planeswalker.text in self.types


    # ***************************************************************************
    def isAVehicule(self):
        if self.subTypes :
            lowerSubTypes = self.subTypes.lower()
            return "vehicule" in lowerSubTypes
        else:
            return False


    # ***************************************************************************
    def getFramePath(self):
        framePath = ""

        if self.isACreature():
            framePath = self.frameColor.creatureFramePath
        else:
            framePath = self.frameColor.framePath

        return framePath


    # ***************************************************************************
    def buildTypeText(self):
        typeText = ""

        for superType in self.superTypes:
            typeText += superType
            typeText += " "

        for types in self.types:
            if not (types == t.CardTypes.Creature.text and self.isAVehicule()):
                typeText += types
                typeText+= " "

        if self.subTypes != "":
            typeText += "- "

            typeText += self.subTypes

        return typeText

    # ***************************************************************************
    def isValid(self):
        return self.manaCost != ["error"] and not "error" in self.manaCost and self.abilities != "error" and self.abilitiesSymbols != ["error"]