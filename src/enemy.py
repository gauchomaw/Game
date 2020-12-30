# Bibliotecas do jogo
from weapon import Weapon
from defense import Defense

# Constantes
# Lista de itens de ataque
ATTACK_LIST = ['Adaga', 'Arco', 'Cajado', 'Espada', 'Fantasma', 'Foice', 'Garra', 'Lança', 'Machado', 'Martelo', 'Punho']

# Lista de itens de defesa
DEFENSE_LIST = ['Armadura', 'Roupão', 'Escudo', 'Obital', 'Luva', 'Bracelete', 'Bota']

#Lista de itens acessórios
ACESSORY_LIST = ['Amuleto', 'Anel', 'Sheltom', 'Brinco']

#Outros
OTHER_LIST = ['Pote Resistência, ''Pote Mana', 'Pote Life']

# Bibliotecas do sistema
import random

# Inimigo
class Enemy():
    gold = 0

    def __init__(self, name, health, power, experience):
        self.name = name
        self.health = health
        self.power = power
        self.experience = experience

        # define entre 10% e 20% da Experiência
        self.gold = int(experience * (random.randrange(10, 20)/100))

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health
    
    def setPower(self, power):
        self.power = power
    
    def getPower(self):
        return self.power

    def setExperience(self, experience):
        self.experience = experience

    def getExperience(self):
        return self.experience

    def getGold(self):
        return self.gold

    def getDrop(self):
        items = []

        # Dropar item de ataque
        powerMin = int(self.getPower() * 0.1)       # 10% de mínimo do poder do inimigo
        powerMax = int(powerMin + (powerMin * 0.2)) # 20% do mínimo para o range máximo
        if powerMin == powerMax:
                powerMax += 1
        print("powerMin=%s, powerMax=%s" % (powerMin, powerMax))
        weapon = Weapon(random.choice(ATTACK_LIST), "Attack", random.randrange(powerMin, powerMax))

        # Dropar item de defesa
        defenseMin = int(self.getPower() * 0.1)         # 10% de mínimo do poder do inimigo
        defenseMax = int(powerMin + (powerMin * 0.2))   # 20% do mínimo para o range máximo
        if defenseMin == defenseMax:
                defenseMax += 1
        print("defenseMin=%s, defenseMax=%s" % (defenseMin, defenseMax))
        defense = Defense(random.choice(DEFENSE_LIST), "Defense", random.randrange(defenseMin, defenseMax))

        # Dropar acessório

        # Dropar outros

        # Adicionar drops na lista de itens
        items.append(weapon)
        items.append(defense)

        return items

    def status(self):
        print("======== Enemy Stats =======")        
        print("Name = " + self.getName())
        print("Health = " + str(self.getHealth()))
        print("Power = " + str(self.getPower()))
        print("XP = " + str(self.getExperience()))
        print("Gold = " + str(self.getGold()))