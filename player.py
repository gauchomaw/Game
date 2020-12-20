
# Jogador

class Player():
    mana = 0
    stamina = 0
    gold = 0
    experience = 0
    weapons = []
    inventario = []

    # forca
    # inteligencia
    # talento
    # agilidade
    # vitalidade

    def __init__(self, name, health, experience):
        self.name = name
        self.health = health
        self.experience = experience

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health

    def getExperience(self):
        return self.experience

    def setWeapon(self, weapon):
        self.weapons.append(weapon)

    def getWeapons(self):
        return self.weapons

    def addExperience(self, experience):
        self.experience += experience

    def getNivel(self):
        if (self.experience < 100):
            return 1
        return (self.experience // 100)
    
    def getPower(self):
        power = 0
        for weapon in self.weapons:
            power += weapon.getPower()
        return power

    def addGold(self, gold):
        self.gold += gold

    def getGold(self):
        return self.gold

    def addWeaponInventario(self, item):
        self.inventario.append(item)
    
    def getInventario(self):
        return self.inventario
    
    def addMana(self, mana):
        self.mana = mana

    def getMana(self):
        return self.mana

    def addStamina(self, stamina):
        self.stamina = stamina
    
    def getStamina(self):
        return self.stamina

    
    #Imprime o status do jogador
    def status(self):
        print("====== Player Stats ======")
        print("Player = " + self.getName())
        print("Health = " + str(self.getHealth()))
        print("Mana = " + str(self.getMana()))
        print("Stamina = " + str(self.getStamina()))
        print("Power = " + str(self.getPower()))
        print("Gold = " + str(self.getGold()))
        print("Nivel = " + str(self.getNivel()))
        print("XP = " + str(self.getExperience()))
        for weapon in self.weapons:
            weapon.status()