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

    def status(self):
        print("======== Enemy Stats =======")        
        print("Name = " + self.getName())
        print("Health = " + str(self.getHealth()))
        print("Power = " + str(self.getPower()))
        print("XP = " + str(self.getExperience()))
        print("Gold = " + str(self.getGold()))