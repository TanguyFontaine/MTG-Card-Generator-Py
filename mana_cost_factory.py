import symbols_type as S
import PySimpleGUI as psg
import ressources as rsc

# input : a string contaning mana symbols infos
# output : list< pair<manaSymbol, nb> >

# ***************************************************************************
def extractSymbols(manaSymbolsStr):
    symbols = []
    
    if manaSymbolsStr and manaSymbolsStr.find('[') != 1:
        manaSymbolsSplited = manaSymbolsStr.split('[')
        for symbolCodeStr in manaSymbolsSplited:
            if symbolCodeStr and symbolCodeStr[len(symbolCodeStr) - 1] == ']':
                i = 0
                nbStr = ""
                symbolStr = ""
                while i < len(symbolCodeStr) -1:
                    if symbolCodeStr[i] == '0' or symbolCodeStr[i] == '1' or symbolCodeStr[i] == '2' or symbolCodeStr[i] == '3' or symbolCodeStr[i] == '4' or symbolCodeStr[i] == '5' or symbolCodeStr[i] == '6' or symbolCodeStr[i] == '7' or symbolCodeStr[i] == '8' or symbolCodeStr[i] == '9' or symbolCodeStr[i] == '+' or symbolCodeStr[i] == '-':
                        nbStr += symbolCodeStr[i]
                    else: 
                        symbolStr += symbolCodeStr[i]
                    i += 1

                symbol = S.findSymbolFromCode(symbolStr)
                if symbol:
                    if nbStr:
                        symbols.append( (symbol, int(nbStr)) )
                    else:
                        symbols.append( (symbol, 1) ) #1 is the default value if a symbol is recognized without any number indication
                else:
                    symbols = ["error"]
                    errorWindow = psg.Window(rsc.errorWindowTitle, layout=[[psg.Text(rsc.unvalidSymbolMessage)]], margins=(200, 50)).read()

    return symbols



# ***************************************************************************
def getNeededSpace(symbol, nuberOfSymbols):
    spaces = ""
    
    if symbol == S.SymbolsType.Grey or symbol == S.SymbolsType.LoyaltyDown or symbol == S.SymbolsType.LoyaltyUp:
        spaces += "  "
    else:
        for i in range(nuberOfSymbols):
            spaces += "  "

    return spaces