#Bibliotecas de sistema
import random
import os

#Bibliotecas do jogo
from player import Player
from enemy import Enemy
from weapon import Weapon
from battle import Battle

class Game():
    players = []    #Lista de jogadores
    enemys = []     #Lista de inimigos
    weapons = []    #Lista de armas

    def run(self):
        
        print("Criando armas")
        #Criar armas
        weapon = Weapon("Sword Low", "Sword", 13)
        self.weapons.append(weapon)
        weapon = Weapon("Sword Medium", "Sword", 5)
        self.weapons.append(weapon)
        weapon = Weapon("Low Axe", "Axe", 3)
        self.weapons.append(weapon)
        weapon = Weapon("Medium Axe", "Axe", 5)
        self.weapons.append(weapon)

        #Criar player
        print("Criando char...")
        player = Player("Maurício", 100, 1)
        player.setWeapon(self.weapons[0])
        self.players.append(player)

        #Criar inimigo radômico nível 1
        print("Creating enemys...")
        self.createRandomEnemy(1)
        
        #Criar menu
        self.menu()

    # criar inimigos randômicos
    def createRandomEnemy(self, nivel):
        h = random.randrange(1 + (nivel * 100 - 100), nivel * 100)
        p = random.randrange(1 + (nivel * 100 - 100), nivel * 100)
        xp = random.randrange(1 + (nivel * 100 - 100), nivel * 100)
        name = str(h)
        enemy = Enemy("Enemy " + name, h, p, xp)
        self.enemys.append(enemy)

        #Nível 1: 1 a 100
        #Nível 2: 101 a 200
        #Nível 3: 201 a 300
        #Nível 4: 301 a 400
        
    
    def menu(self):
        while(True):
            self.updateUI()

            #print("[w | a | s | d] Mover")
            print("[b] Batalha")
            print("[i] Inventário")
            print("[1] Player Status")
            print("[2] Player Enemys")
            print("[e] Sair")
            option = input("Informe sua opção: ")
            if option == "e":
                break
            if option == "b":
                countEnemys = len(self.enemys)
                if countEnemys > 0:
                    #Busca um inimigo aleatório na lista de inimigos
                    i = random.randrange(0, countEnemys)
                    battle = Battle(self.players[0], self.enemys[i])
                    while(True):
                        self.updateUI()
                        battle.status()
                        if self.enemys[i].health > 0:                       
                            option = input("Informe sua opção (h = hit, r = retornar): ")
                            if option == "h":
                                battle.hit()
                            elif option == "r":
                                break
                            else:
                                print("Opção inválida. Tente novamente...")
                        if self.enemys[i].health <= 0:
                            print("Inimigo morto - XP: " + str(self.enemys[i].getExperience()))
                            del(self.enemys[i])
                            #Criar inimigo aleatório do mesmo nível do jogador 
                            self.createRandomEnemy(self.players[0].getNivel())
                            break
            if option == "i":
                self.updateUI()
                print("==== ==== ==== ==== ==== ==== ==== ==== ==== ====")
                print(" 01   02   03   04   05   06   07   08   09   10")
                print("==== ==== ==== ==== ==== ==== ==== ==== ==== ====")
                print(" 11   12   13   14   15   16   17   18   19   20")
                print("==== ==== ==== ==== ==== ==== ==== ==== ==== ====")
                input("pressione uma tecla para continuar... ")
            if option == "1":
                self.statusPlayers()
                input("pressione uma tecla para continuar... ")
            if option == "2":
                self.statusEnemys()
                input("pressione uma tecla para continuar... ")

    def updateUI(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("========================================================================\n" + \
        "|Player: " + self.players[0].getName() + "\t\t" \
        "Gold: " + str(self.players[0].getGold()) + "\n" \
        "|Health: " + str(self.players[0].getHealth()) + "\t\t\t" \
        "Power: " + str(self.players[0].getPower()) + "\n" \
        "|Nivel: " + str(self.players[0].getNivel()) + "\t\t\t" \
        "XP: " + str(self.players[0].getExperience()) + "\n" \
        "========================================================================" + \
        "\n")

    #Imprimir os status
    def statusPlayers(self):
        for player in self.players:
            player.status()

    def statusEnemys(self):
        for enemy in self.enemys:
            enemy.status()