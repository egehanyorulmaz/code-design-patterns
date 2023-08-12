from abc import ABC, abstractmethod


class GameCharacter(ABC):
    @abstractmethod
    def display(self):
        pass


class Warrior(GameCharacter):
    def display(self):
        print("Warrior character created with sword and shield!")


class Mage(GameCharacter):
    def display(self):
        print("Mage character created with magical staff!")


class Archer(GameCharacter):
    def display(self):
        print("Archer character created with bow and arrows!")


class CharacterFactory:
    @staticmethod
    def create_character(character_type):
        if character_type == 'warrior':
            return Warrior()
        elif character_type == 'mage':
            return Mage()
        elif character_type == 'archer':
            return Archer()
        else:
            raise ValueError("Invalid character type")


# Client code
character_type = 'warrior'  # You can switch between 'warrior', 'mage', 'archer'
character = CharacterFactory.create_character(character_type)
character.display()
