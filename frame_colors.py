from enum import Enum

import image_paths as IP

class FrameColors(Enum):
    # (text, spell frame, creature frame)
    # planeswalkers use spell frames

    White = ("White", IP.white_frame_image, IP.white_creature_frame_image)
    Blue = ("Blue", IP.blue_frame_image, IP.blue_creature_frame_image)
    Black = ("Black", IP.black_frame_image, IP.black_creature_frame_image)
    Red = ("Red", IP.red_frame_image, IP.red_creature_frame_image)
    Green = ("Green", IP.green_frame_image, IP.green_creature_frame_image)
    Grey =  ("Grey", IP.grey_frame_image, IP.grey_creature_frame_image)
    Golden = ("Golden", IP.golden_frame_image, IP.golden_creature_frame_image)
    Colorless = ("Colorless" , IP.colorless_frame_image, IP.colorless_creature_frame_image)
    HybridWhiteBlue = ("Hybrid White/Blue", IP.hybrid_white_blue_frame_image, IP.hybrid_white_blue_creature_frame_image)
    HybridWhiteBlack = ("Hybrid White/Black", IP.hybrid_white_black_frame_image, IP.hybrid_white_black_creature_frame_image)
    HybridRedWhite = ("Hybrid Red/White", IP.hybrid_red_white_frame_image, IP.hybrid_red_white_creature_frame_image)
    HybridRedGreen = ("Hybrid Red/Green", IP.hybrid_red_green_frame_image, IP.hybrid_red_green_creature_frame_image)
    HybridGreenBlue = ("Hybrid Green/Blue", IP.hybrid_green_blue_frame_image, IP.hybrid_green_blue_creature_frame_image)
    HybridGreenWhite = ("Hybrid Green/White", IP.hybrid_green_white_frame_image, IP.hybrid_green_white_creature_frame_image)
    HybridBlueBlack = ("Hybrid Blue/Black", IP.hybrid_blue_black_frame_image, IP.hybrid_blue_black_creature_frame_image)
    HybridBlueRed = ("Hybrid Blue/Red", IP.hybrid_blue_red_frame_image, IP.hybrid_blue_red_creature_frame_image)
    HybridBlackRed = ("Hybrid Black/Red", IP.hybrid_black_red_frame_image, IP.hybrid_black_red_creature_frame_image)
    HybridBlackGreen = ("Hybrid Black/Green", IP.hybrid_black_green_frame_image, IP.hybrid_black_green_creature_frame_image)

    def __init__(self, text, framePath, creatureFramePath):
        self.text = text
        self.framePath = framePath
        self.creatureFramePath = creatureFramePath


def getFrameColorFromText(frameColorText):
    
    if frameColorText:
        for frameColor in FrameColors:
            if frameColor.text == frameColorText:
                return frameColor

    return FrameColors.Colorless #defaul frame color is colorless
