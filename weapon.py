
# Armas

from item import Item

# Weapon herda de Item
class Weapon(Item):
    def __init__(self, name, typei, power):
        super().__init__(name, typei)
        self.power = power
    
    def setName(self, name):
        super().setName(name)
    
    def getName(self):
        return super().getName()

    def setType(self, typei):
        super().setType(typei)

    def getType(self):
        return super().getType()
    
    def setPower(self, power):
        self.power = power
    
    def getPower(self):
        return self.power

    def status(self):
        print("====== Weapon Stats ======")
        print("Weapon = " + self.getName())
        print("Type = " + str(self.getType()))
        print("Power = " + str(self.getPower()))