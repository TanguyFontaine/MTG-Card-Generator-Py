import PySimpleGUI as psg

import frame_colors as fc
import card_types as t
import card_super_types as st

# main window
mainWindowTitle = "Card Generator"
mainWindowWidth = 300
mainWindowHeight = 200

# card name textbox
cardNameTextboxText = "name :"
cardNameTextboxTooltip = "enter card name"
cardNameTextboxKey = "-CARD NAME-"

# type selection
selectTypeText = "select types :"

# tribal type checkbox
isCreatureCheckboxText = "creature "
isCreatureCheckboxTooltip = "tick if the card is a creature"
isCreatureCheckboxKey = t.CardTypes.Creature.value[0]
# tribal type checkbox
isArtifactCheckboxText = "artifact "
isArtifactCheckboxTooltip = "tick if the card is an artifact"
isArtifactCheckboxKey = t.CardTypes.Artifact.value[0]
# tribal type checkbox
isEnchantmentCheckboxText = "enchantment "
isEnchantmentCheckboxTooltip = "tick if the card is an enchantment"
isEnchantmentCheckboxKey = t.CardTypes.Enchantment.value[0]
# tribal type checkbox
isPlaneswalkerCheckboxText = "planeswalker "
isPlaneswalkerCheckboxTooltip = "tick if the card is a planeswalker"
isPlaneswalkerCheckboxKey = t.CardTypes.Planeswalker.value[0]
# tribal type checkbox
isInstantCheckboxText = "instant "
isInstantCheckboxTooltip = "tick if the card is an instant"
isInstantCheckboxKey = t.CardTypes.Instant.value[0]
# tribal type checkbox
isSorceryCheckboxText = "sorcery "
isSorceryCheckboxTooltip = "tick if the card is a sorcery"
isSorceryCheckboxKey = t.CardTypes.Sorcery.value[0]
# tribal type checkbox
isLandCheckboxText = "land "
isLandCheckboxTooltip = "tick if the card is a land"
isLandCheckboxKey = t.CardTypes.Land.value[0]
# tribal type checkbox
isTribalCheckboxText = "tribal "
isTribalCheckboxTooltip = "tick if the card is tribal"
isTribalCheckboxKey = t.CardTypes.Tribal.value[0]

# super types
selectSupertypeText = "select super types :"

# legendary supertype checkbox
isLegendaryCheckboxText = "legendary "
isLegendaryCheckboxTooltip = "tick if the card is legendary"
isLegendaryCheckboxKey = st.SuperTypes.Legendary.value[0]
# snow supertype checkbox
isSnowCheckboxText = "snow "
isSnowCheckboxTooltip = "tick if the card is snow"
isSnowCheckboxKey = st.SuperTypes.Snow.value[0]
# basic supertype checkbox
isBasicCheckboxText = "basic "
isBasicCheckboxTooltip = "tick if the card is basic"
isBasicCheckboxKey = st.SuperTypes.Basic.value[0]
# token supertype checkbox
isTokenCheckboxText = "token "
isTokenCheckboxTooltip = "tick if the card is a token"
isTokenCheckboxKey = st.SuperTypes.Token.value[0]

# subtypes textbox
subtypesTextboxText = "subtypes :"
subtypesTextboxTooltip = "enter card subtypes"
subtypesTextboxKey = "-SUBTYPES-"

# frame colors selection
frameColorsComboboxText = "frame color :"
frameColorsComboboxTooltip = "select the color of the frame for your card"
frameColorsComboboxKey = "-FRAME-"

# mana symbols selection
manaSymbolsText = "select mana symbols :"
manaSymbolsKey = "-MANA-"
manaSymbolsTooltip = "check help page for symbols"

# abilities textbox
abilitiesTextboxText = "abilities or description of your spell :"
abilitiesTextboxTooltip = "check help page for symbols"
abilitiesTextboxKey = "-ABILITIES-"

# flavor text textbox
flavorTextboxText = "flavor text :"
flavorTextboxTooltip = ""
flavorTextboxKey = "-FLAVOR-"

# power
powerTextboxText = "power :"
powerTextboxTooltip = ""
powerTextboxKey = "-POWER-"

# toughness 
toughnessTextboxText = "toughness :"
toughnessTextboxTooltip = ""
toughnessTextboxKey = "-TOUGHNESS-"

# loyalty textbox
loyaltyTextboxText = "loyalty :"
loyaltyTextboxTooltip = "The loyalty of your planeswalker"
loyaltyTextboxKey = "-LOYALTY-"

# upload image
imageSelectorText = "Image file path"
imageSelectorTooltip = "select an image for your card"
imageFileKey = "-FILE LIST-"
imageSelectorKey = "-IMAGE-"

# generate card button
generateButtonText = "Generate"
generateButtonTooltip = "Generate the image of your card"

# generate card button
helpButtonText = "Help symbols"

# help window
helpWindowTitle = "Help Window"
helpText = " symbols must be between [] with the number of symbols followed by the symbol code \n if no number is set for a symbol, 1 of this symbol is understood by default \n Grey =  Gy \n White = W \n Blue = Be \n Black = Bk \n Red = R \n Green = Gn \n Colorless = Cl  \n Hybrid White Blue = HWBe \n Hybrid White Black = HWBk \n Hybrid Blue Black = HBeBk \n Hybrid Blue Red = HBeR \n Hybrid Black Red = HBkR \n Hybrid Black Green = HBkGn \n Hybrid Red Green = HRGn \n Hybrid Red White = HRW \n Hybrid Green White = HGnW \n Hybrid Green Blue = HGnBe \n Phyrexian Grey =  PhGy \n PhyrexianWhite = PhW \n PhyrexianBlue = PhBe \n Phyrexian Black = PhBk \n Phyrexian Red = PhR \n Phyrexian Green = PhGn \n Phyrexian Colorless = PhCl \n Phyrexian Hybrid White Blue = PhHWBe \n Phyrexian Hybrid White Black = PhHWBk \n Phyrexian Hybrid Blue Black = PhHBeBk \n Phyrexian Hybrid Blue Red = PhHBeR \n Phyrexian Hybrid Black Red = PhHBkR \n Phyrexian Hybrid Black Green = PhHBkGn \n Phyrexian Hybrid Red Green = PhHRGn \n Phyrexian Hybrid Red White = PhHRW \n Phyrexian Hybrid Green White = PhHGnW \n Phyrexian Hybrid Green Blue = PhHGnBe \n X Grey = XGy \n X White = XW \n X Blue = XBe \n X Black = XBk \n X Red = XR \n X Green = XGn \n X Colorless = XCl \n Snow mana = S \n Energy = E \n Loyalty = Ly \n Tap = Tap \n Untap = Untap \n example : [2Gy][2R] give 2 grey manas and 2 red manas for your mana cost \n [1Tap] = [Tap] = 1 tap symbol in your text \n [0Gy] gives the 0 grey mana symbol you can find on the black lotus"

# error window
errorWindowTitle = "Error"
wrongFileTypeErrorMessage = "File type not supported, please select .png or .gif file"
unvalidSymbolMessage = "Symbol not recognized, please check help button to see symbols values"
