from item import Item

# Defense herda de Item
class Defense(Item):
    def __init__(self, name, typei, defense):
        super().__init__(name, typei)
        self.defense = defense
    
    def setName(self, name):
        super().setName(name)
    
    def getName(self):
        return super().getName()

    def setType(self, typei):
        super().setType(typei)

    def getType(self):
        return super().getType()

    def setOwner(self, owner):
        super().setOwner(owner)

    def getOwner(self):
        return super().getOwner()        
    
    def setDefense(self, defense):
        self.defense = defense
    
    def getDefense(self):
        return self.defense

    def status(self):
        print("====== Defense Stats ======")
        print("Name = " + self.getName())
        print("Type = " + str(self.getType()))
        print("Defense = " + str(self.getDefense()))
        print("Owner = " + str(self.getOwner()))