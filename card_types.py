from enum import Enum

class CardTypes(Enum):
    # (key, text)
    Creature = ("-CREATURE-", "Creature")
    Artifact = ("-ARTIFACT-", "Artifact")
    Enchantment = ("-ENCHANTMENT-", "Enchantment")
    Planeswalker = ("-PLANESWALKER-", "Planeswalker")
    Instant = ("-INSTANT-", "Instant")
    Sorcery = ("-SORCERY-", "Sorcery")
    Land = ("-LAND-", "Land")
    Tribal = ("-TRIBAL-", "Tribal")

    def __init__(self, key, text):
        self.key = key
        self.text = text