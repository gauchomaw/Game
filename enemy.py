
class Enemy():
    def __init__(self, name, health, power, experience):
        self.name = name
        self.health = health
        self.power = power
        self.experience = experience

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

    def status(self):
        print("======== Enemy Stats =======")        
        print("Name = " + self.name)
        print("Health = " + str(self.health))
        print("Power = " + str(self.power))
        print("XP = " + str(self.experience))