from enum import Enum

class SuperTypes(Enum):
    # (key, text)
    Legendary = ("-LEGEND-", "Legendary")
    Snow = ("-SNOW-", "Snow")
    Basic = ("-BASIC-", "Basic")
    Token = ("-TOKEN-", "Token")

    def __init__(self, key, text):
        self.key = key
        self.text = text


