

class Battle():
    def __init__(self, player, enemy):
       self.player = player
       self.enemy = enemy
    
    def hit(self):
        #Hit Player
        if self.player.getPower() >= self.enemy.health:
           self.player.addExperience(self.enemy.experience)
           self.enemy.health = 0
        else:
            self.enemy.health -= self.player.getPower()
        self.status()
    
    def status(self):
        print("=== Battle ===")
        print("Player Power = " + str(self.player.getPower()))
        print("Player Health = " + str(self.player.getHealth()))
        print("---")
        print("Enemy Power = " + str(self.enemy.getPower()))
        print("Enemy Health = " + str(self.enemy.getHealth()))
        print("Enemy XP = " + str(self.enemy.getExperience()))
        