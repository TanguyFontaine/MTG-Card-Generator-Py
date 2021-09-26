from enum import Enum

import image_paths as IP

class SymbolsType(Enum):

    # code, imagePath
    Grey =  ("Gy", IP.greyMana)
    White = ("W", IP.whiteMana)
    Blue = ("Be", IP.blueMana)
    Black = ("Bk", IP.blackMana)
    Red = ("R", IP.redMana)
    Green = ("Gn", IP.greenMana)
    Colorless = ("Cl", IP.colorlessMana)
    HybridWhiteBlue = ("HWBe", IP.hybridWhiteBlueMana)
    HybridWhiteBlack = ("HWBk", IP.hybridWhiteBlackMana)
    HybridBlueBlack = ("HBeBk", IP.hybridBlueBlackMana)
    HybridBlueRed = ("HBeR", IP.hybridBlueRedMana)
    HybridBlackRed = ("HBkR", IP.hybridBlackRedMana)
    HybridBlackGreen = ("HBkGn", IP.hybridBlackGreenMana)
    HybridRedGreen = ("HRGn", IP.hybridRedGreenMana)
    HybridRedWhite = ("HRW", IP.hybridRedWhiteMana)
    HybridGreenWhite = ("HGnW", IP.hybridGreenWhiteMana)
    HybridGreenBlue = ("HGnBe", IP.hybridGreenBlueMana)
    PhyrexianGrey =  ("PhGy", IP.phyrexianGreyMana)
    PhyrexianWhite = ("PhW", IP.phyrexianWhiteMana)
    PhyrexianBlue = ("PhBe", IP.phyrexianBlueMana)
    PhyrexianBlack = ("PhBk" , IP.phyrexianBlackMana)
    PhyrexianRed = ("PhR", IP.phyrexianRedMana)
    PhyrexianGreen = ("PhGn", IP.phyrexianGreenMana)
    PhyrexianColorless = ("PhCl", IP.phyrexianColorlessMana)
    PhyrexianHybridWhiteBlue = ("PhHWBe", IP.phyrexianHybridWhiteBlueMana)
    PhyrexianHybridWhiteBlack = ("PhHWBk", IP.phyrexianHybridWhiteBlackMana)
    PhyrexianHybridBlueBlack = ("PhHBeBk", IP.phyrexianHybridBlueBlackMana)
    PhyrexianHybridBlueRed = ("PhHBeR", IP.phyrexianHybridBlueRedMana)
    PhyrexianHybridBlackRed = ("PhHBkR", IP.phyrexianHybridBlackRedMana)
    PhyrexianHybridBlackGreen = ("PhHBkGn", IP.phyrexianHybridBlackGreenMana)
    PhyrexianHybridRedGreen = ("PhHRGn", IP.phyrexianHybridRedGreenMana)
    PhyrexianHybridRedWhite = ("PhHRW", IP.phyrexianHybridRedWhiteMana)
    PhyrexianHybridGreenWhite = ("PhHGnW", IP.phyrexianHybridGreenWhiteMana)
    PhyrexianHybridGreenBlue = ("PhHGnBe", IP.phyrexianHybridGreenBlueMana)
    XGrey = ("XGy", IP.xGreyMana)
    XWhite = ("XW", IP.xWhiteMana)
    XBlue = ("XBe", IP.xBlueMana)
    XBlack = ("XBk" , IP.xBlackMana)
    XRed = ("XR", IP.xRedMana)
    XGreen = ("XGn", IP.xGreenMana)
    XColorless = ("XCl" , IP.xColorlessMana)
    SnowMana = ("S", IP.snowMana)

    Energy = ("E", IP.energy)

    LoyaltyUp = ("Lu", IP.loyaltyUp)
    LoyaltyDown = ("Ld", IP.loyaltyDown)

    Tap = ("Tap", IP.tap)
    Untap = ("Untap", IP.untap)

    def __init__(self, code, imagePath):
        self.code = code
        self.imagePath = imagePath


def findSymbolFromCode(code):
    for symbol in SymbolsType:
        if symbol.code == code:
            return symbol