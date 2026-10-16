from enum import Enum

class cards:
    def __init__(self,name,limit,):
        self.name = name
        self.limit = limit

    def __str__(self):
        return self.name

class spell(cards):
    spelltype = Enum('SpellType', ['NORMAL', 'CONTINUOUS', 'QUICKPLAY'])
    effects = Enum('Effects', ['DESTROY', 'SEARCH', 'DRAW'])
    
    def __init__(self,name,limit,effect, type):
        cards.__init__(self,name,limit)
        self.effect = effect
        self.type = type

    def spell_description(self):
        if self.type == self.spelltype.NORMAL:
            print(f"{self.name} is a normal spell card.")
        elif self.type == self.spelltype.CONTINUOUS:
            print(f"{self.name} is a continuous spell card.")
        elif self.type == self.spelltype.QUICKPLAY:
            print(f"{self.name} is a quick-play spell card.")

        print(f"{self.name} is limited to {self.limit} copy(ies) in the deck.")
        if self.effect == self.effects.DESTROY:
            print(f"{self.name} can destroy a card on the field.")
        elif self.effect == self.effects.SEARCH:
            print(f"{self.name} can search a card from the deck.")
        elif self.effect == self.effects.DRAW:
            print(f"{self.name} can draw a card.")


class trap(cards):
    traptype = Enum('TrapType', ['NORMAL', 'CONTINUOUS', 'COUNTER'])
    effects = Enum('Effects', ['DESTROY', 'NEGATE', 'DRAW'])

    def __init__(self,name,limit,effect, type):
        cards.__init__(self,name,limit)
        self.effect = effect
        self.type = type

    def trap_description(self):
        if self.type == self.traptype.NORMAL:
            print(f"{self.name} is a normal trap card.")
        elif self.type == self.traptype.CONTINUOUS:
            print(f"{self.name} is a continuous trap card.")
        elif self.type == self.traptype.COUNTER:
            print(f"{self.name} is a counter trap card.")

        print(f"{self.name} is limited to {self.limit} copy(ies) in the deck.")
        if self.effect == self.effects.DESTROY:
            print(f"{self.name} can destroy a card on the field.")
        elif self.effect == self.effects.NEGATE:
            print(f"{self.name} can negate the effect of a card on the field.")
        elif self.effect == self.effects.DRAW:
            print(f"{self.name} can draw a card.")


class monster(cards):
    attribute = Enum('Attribute', ['DARK', 'LIGHT', 'EARTH', 'WATER', 'FIRE', 'WIND', 'DIVINE'])
    cardtype = Enum('CardType', ['NORMAL', 'EFFECT', 'FUSION', 'SYNCHRO', 'XYZ', 'LINK'])
    type = Enum('Type', ['FIEND', 'DIVINEBEAST', 'WARRIOR', 'SPELLCASTER', 'BEAST', 'DRAGON', 'AQUA', 'PYRO', 'INSECT', 'MACHINE', 'FAIRY', 'ZOMBIE', 'PSYCHIC', 'REPTILE', 'ROCK', 'SEASERPENT', 'DINOSAUR', 'WINGEDBEAST', "ILLUSION"])
    def __init__(self,name,limit,level,attack,defense,cardtype,attribute,type):
        cards.__init__(self,name,limit)
        self.level = level
        self.attack = attack
        self.defense = defense
        self.cardtype = cardtype
        self.attribute = attribute
        self.type = type

    def monster_description(self):
        if self.cardtype == self.cardtype.NORMAL:
            print(f"{self.name} is a normal monster card.")
        elif self.cardtype == self.cardtype.EFFECT:
            print(f"{self.name} is an effect monster card.")
        elif self.cardtype == self.cardtype.FUSION: 
            print(f"{self.name} is a fusion monster card.")
        elif self.cardtype == self.cardtype.SYNCHRO:
            print(f"{self.name} is a synchro monster card.")
        elif self.cardtype == self.cardtype.XYZ:
            print(f"{self.name} is an xyz monster card.")
        elif self.cardtype == self.cardtype.LINK:
            print(f"{self.name} is a link monster card.")


        if self.attribute == self.attribute.DARK:
            print(f"{self.name} is a dark attribute monster.")
        elif self.attribute == self.attribute.LIGHT:
            print(f"{self.name} is a light attribute monster.")
        elif self.attribute == self.attribute.EARTH:
            print(f"{self.name} is an earth attribute monster.")
        elif self.attribute == self.attribute.WATER:
            print(f"{self.name} is a water attribute monster.")
        elif self.attribute == self.attribute.FIRE:
            print(f"{self.name} is a fire attribute monster.")
        elif self.attribute == self.attribute.WIND:
            print(f"{self.name} is a wind attribute monster.")
        elif self.attribute == self.attribute.DIVINE:
            print(f"{self.name} is a divine attribute monster.")


        if self.type == self.type.FIEND:
            print(f"{self.name} is a fiend type monster.")
        elif self.type == self.type.DIVINEBEAST:
            print(f"{self.name} is a divine beast type monster.")
        elif self.type == self.type.WARRIOR:
            print(f"{self.name} is a warrior type monster.")
        elif self.type == self.type.SPELLCASTER:
            print(f"{self.name} is a spellcaster type monster.")
        elif self.type == self.type.BEAST:
            print(f"{self.name} is a beast type monster.")
        elif self.type == self.type.DRAGON:
            print(f"{self.name} is a dragon type monster.")
        elif self.type == self.type.AQUA:
            print(f"{self.name} is an aqua type monster.")
        elif self.type == self.type.PYRO:
            print(f"{self.name} is a pyro type monster.")
        elif self.type == self.type.INSECT:
            print(f"{self.name} is an insect type monster.")
        elif self.type == self.type.MACHINE:
            print(f"{self.name} is a machine type monster.")
        elif self.type == self.type.FAIRY:
            print(f"{self.name} is a fairy type monster.")
        elif self.type == self.type.ZOMBIE:
            print(f"{self.name} is a zombie type monster.")
        elif self.type == self.type.PSYCHIC:
            print(f"{self.name} is a psychic type monster.")
        elif self.type == self.type.REPTILE:
            print(f"{self.name} is a reptile type monster.")
        elif self.type == self.type.ROCK:
            print(f"{self.name} is a rock type monster.")
        elif self.type == self.type.SEASERPENT:
            print(f"{self.name} is a sea serpent type monster.")
        elif self.type == self.type.DINOSAUR:
            print(f"{self.name} is a dinosaur type monster.")
        elif self.type == self.type.WINGEDBEAST:
            print(f"{self.name} is a winged beast type monster.")
        elif self.type == self.type.ILLUSION:
            print(f"{self.name} is an illusion type monster.") 

        print(f"{self.name} is level {self.level} monster with {self.attack} attack and {self.defense} defense.")
        print(f"{self.name} is limited to {self.limit} copy(ies) in the deck.")

    

MysticalSpaceTyphoon = spell("Mystical Space Typhoon", 3, spell.effects.DESTROY ,spell.spelltype.QUICKPLAY) 
potofGreed = spell("Pot of Greed", 0, spell.effects.DRAW, spell.spelltype.NORMAL)
solemnJudgment = trap("Solemn Judgment", 1, trap.effects.NEGATE, trap.traptype.COUNTER)
blueEyes = monster("Blue-Eyes White Dragon", 3, 8, 3000, 2500, monster.cardtype.NORMAL, monster.attribute.LIGHT, monster.type.DRAGON)

deck = [MysticalSpaceTyphoon, potofGreed, solemnJudgment, blueEyes, blueEyes, potofGreed, MysticalSpaceTyphoon]

def draw_card(deck):
    import random
    if len(deck) == 0:
        print("The deck is empty. No more cards to draw.")
        return None
    card = random.choice(deck)
    deck.remove(card)
    return card

while True:
    drawn_card = draw_card(deck)
    if drawn_card is None:
        break
    else:
        print(f"You drew {drawn_card.name}. It's effect is {drawn_card.effect.name if hasattr(drawn_card, 'effect') else 'N/A'} It's attack is {drawn_card.attack if hasattr(drawn_card, 'attack') else 'N/A'}.")
