### Source: https://www.youtube.com/watch?v=tAuRQs_d9F8
class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle


class BurgerBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self

    def build(self):
        return self.burger


burger = BurgerBuilder() \
    .addBuns("sesame") \
    .addPatty("fish-patty") \
    .addCheese("swiss cheese")
