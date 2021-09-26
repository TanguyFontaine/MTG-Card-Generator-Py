import PySimpleGUI as psg
import os.path

import ressources as rsc
import frame_colors as fc
import card as c
import card_types as ct
import card_super_types as cst
import mana_cost_factory as msf


# ***************************************************************************
def buildFrameColorsList():
    frameColorslist = []
    for frameColor in fc.FrameColors:
        frameColorslist.append(frameColor.text)
    return frameColorslist



# ***************************************************************************
def buildMainWindow():
    # Build UI elements
    cardNameLine = [psg.Text(rsc.cardNameTextboxText), psg.InputText(tooltip=rsc.cardNameTextboxTooltip, key=rsc.cardNameTextboxKey) ]
    selectTypeLine = [psg.Text(rsc.selectTypeText), psg.Checkbox(text=rsc.isCreatureCheckboxText, tooltip=rsc.isCreatureCheckboxTooltip, enable_events=True, key=rsc.isCreatureCheckboxKey),
                                                    psg.Checkbox(text=rsc.isArtifactCheckboxText, tooltip=rsc.isArtifactCheckboxTooltip, enable_events=True, key=rsc.isArtifactCheckboxKey),
                                                    psg.Checkbox(text=rsc.isEnchantmentCheckboxText, tooltip=rsc.isEnchantmentCheckboxTooltip, enable_events=True, key=rsc.isEnchantmentCheckboxKey),
                                                    psg.Checkbox(text=rsc.isPlaneswalkerCheckboxText, tooltip=rsc.isPlaneswalkerCheckboxTooltip, enable_events=True, key=rsc.isPlaneswalkerCheckboxKey),
                                                    psg.Checkbox(text=rsc.isInstantCheckboxText, tooltip=rsc.isInstantCheckboxTooltip, enable_events=True, key=rsc.isInstantCheckboxKey),
                                                    psg.Checkbox(text=rsc.isSorceryCheckboxText, tooltip=rsc.isSorceryCheckboxTooltip, enable_events=True, key=rsc.isSorceryCheckboxKey),
                                                    psg.Checkbox(text=rsc.isLandCheckboxText, tooltip=rsc.isLandCheckboxTooltip, enable_events=True, key=rsc.isLandCheckboxKey),
                                                    psg.Checkbox(text=rsc.isTribalCheckboxText, tooltip=rsc.isTribalCheckboxTooltip, enable_events=True, key=rsc.isTribalCheckboxKey)
                      ]

    selectSupertypeLine = [psg.Text(rsc.selectSupertypeText), psg.Checkbox(text=rsc.isLegendaryCheckboxText, tooltip=rsc.isLegendaryCheckboxTooltip, key=rsc.isLegendaryCheckboxKey),
                                                              psg.Checkbox(text=rsc.isSnowCheckboxText, tooltip=rsc.isSnowCheckboxTooltip, key=rsc.isSnowCheckboxKey),
                                                              psg.Checkbox(text=rsc.isBasicCheckboxText, tooltip=rsc.isBasicCheckboxTooltip, key=rsc.isBasicCheckboxKey),
                                                              psg.Checkbox(text=rsc.isTokenCheckboxText, tooltip=rsc.isTokenCheckboxTooltip, key=rsc.isTokenCheckboxKey)
                      ]
    subtypesLine = [psg.Text(rsc.subtypesTextboxText), psg.InputText(tooltip=rsc.subtypesTextboxTooltip, key=rsc.subtypesTextboxKey) ]      
    frameColorLine = [psg.Text(rsc.frameColorsComboboxText), psg.Combo(buildFrameColorsList(), tooltip=rsc.frameColorsComboboxTooltip, key=rsc.frameColorsComboboxKey) ]      
    manaSymbolsLine = [psg.Text(rsc.manaSymbolsText), psg.InputText(tooltip=rsc.manaSymbolsTooltip, key=rsc.manaSymbolsKey) ]      
    abilitiesLine = [psg.Text(rsc.abilitiesTextboxText), psg.Multiline(size=(50, 8), tooltip=rsc.abilitiesTextboxTooltip, key=rsc.abilitiesTextboxKey) ]      
    flavorTextLine = [psg.Text(rsc.flavorTextboxText), psg.Multiline(size=(50, 4), tooltip=rsc.flavorTextboxTooltip, key=rsc.flavorTextboxKey) ]      
    powerToughnessLine = [psg.Text(rsc.powerTextboxText), psg.InputText(tooltip=rsc.powerTextboxTooltip, key=rsc.powerTextboxKey, disabled=True), 
                          psg.Text(rsc.toughnessTextboxText), psg.InputText(tooltip=rsc.toughnessTextboxTooltip, key=rsc.toughnessTextboxKey, disabled=True)]      
    loyaltyLine = [psg.Text(rsc.loyaltyTextboxText), psg.InputText(tooltip=rsc.loyaltyTextboxTooltip, key=rsc.loyaltyTextboxKey, disabled=True) ]      
    selectImageLine = [psg.Text(rsc.imageSelectorText), psg.In(size=(50, 1), enable_events=True, key=rsc.imageFileKey), psg.FileBrowse(tooltip=rsc.imageSelectorTooltip) ]

    generateButtonLine = [psg.Button(button_text=rsc.generateButtonText, tooltip=rsc.generateButtonTooltip), psg.Button(button_text=rsc.helpButtonText, pad=((700, 0), (0, 0)) )]

    # inside [[ ]] each list of elements inside [] will be on a new line
    layout = [[ [cardNameLine, selectTypeLine, selectSupertypeLine, subtypesLine, frameColorLine, manaSymbolsLine, abilitiesLine, flavorTextLine, powerToughnessLine, loyaltyLine, selectImageLine], 
                [psg.HorizontalSeparator()], 
                [generateButtonLine] ]]

    # Create the window
    window = psg.Window(rsc.mainWindowTitle, layout, margins=(rsc.mainWindowWidth, rsc.mainWindowHeight), location=(0, 0))

    return window