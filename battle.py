# Bibliotecas do sistema
import random

# Gerenciar Batalhas
class Battle():
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    
    def hit(self):
        # Define quem atinge primeiro
        whoFirst = random.randrange(1,2)
        if (whoFirst == 1):
            self.hitPlayer()
            self.hitEnemy()
        else:
            self.hitEnemy()
            self.hitPlayer()
        self.status()
    
    def hitPlayer(self):
        # Hit Player
        if self.player.health > 0:
            # Se o poder de ataque for maior que a saúde total inimigo, ele morre
            if self.player.getPower() >= self.enemy.health:
                self.player.addExperience(self.enemy.experience)
                self.player.addGold(self.enemy.getGold())
                self.enemy.health = 0
            else:
                # senão, decrementa a saúde com o hit da força utilizada
                self.enemy.health -= self.player.getPower()

    def hitEnemy(self):
        # Hit Enemy
         if self.enemy.health > 0:
            # Se o poder de ataque for maior que a saúde total do player, ele morre
            if self.enemy.getPower() >= self.player.health:
                # To Do: Implementar perda de XP ao morrer
                self.player.health = 0
            else:
                # senão, decrementa a saúde com o hit da força utilizada
                self.player.health -= self.enemy.getPower()

    def status(self):
        print("=== Battle ===")
        print("Player Name = " + str(self.player.getName()))
        print("Player Power = " + str(self.player.getPower()))
        print("Player Health = " + str(self.player.getHealth()))
        print("---")
        print("Enemy Name = " + str(self.enemy.getName()))
        print("Enemy Power = " + str(self.enemy.getPower()))
        print("Enemy Health = " + str(self.enemy.getHealth()))
        print("Enemy XP = " + str(self.enemy.getExperience()))
        print("Gold = " + str(self.enemy.getGold()))
        