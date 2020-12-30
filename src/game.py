# Bibliotecas de sistema
import random
import os
import string

# Bibliotecas do jogo
from player import Player
from enemy import Enemy
from weapon import Weapon
from battle import Battle
from bar import Bar

class Game():
    players = []    # Lista de jogadores
    enemys = []     # Lista de inimigos
    weapons = []    # Lista de armas
    defenses = []   # Lista de defesas

    def run(self):
        
        print("Criando arma")
        # Criar arma
        weapon = Weapon("Espada", "Attack", random.randrange(10,20))
        self.weapons.append(weapon)

        # Criar player
        print("Criando char...")
        player = Player("GauchoMaw", 1000, 1)
        player.setWeapon(self.weapons[0])
        self.players.append(player)
        
        # Criar menu
        self.menu()

    # criar inimigos randômicos
    def createRandomEnemy(self, nivel):
        vList = ['a','e','i','o','u']
        fList1 = ['am', 'an', 'em', 'en', 'im', 'in', 'om', 'on', 'um', 'un']
        fList2 = ['p', 'b', 'm', 'f', 'v', 't', 'd', 'n', 'nh', 'l', 'lh', 'r']
        fList3 = ['rr', 'z', 's', 'x', 'ss', 'c', 'sc', 'j', 'g', 'x', 'ch', 'gu', 'c', 'qu']

        h = random.randrange(1 + (nivel * 100 - 100), nivel * 100)
        p = random.randrange(1 + (nivel * 100 - 100), nivel * 100)
        xp = random.randrange(1 + (nivel * 100 - 100), nivel * 100)
        name = (random.choice(fList1) + random.choice(vList) + random.choice(fList2) + random.choice(vList) + random.choice(fList3) + random.choice(vList)).lower().capitalize()
        #name = ''.join(random.choice(sList) for _ in range(4))
        enemy = Enemy(name, h, p, xp)
        self.enemys.append(enemy)

        # Nível 1: 1 a 100
        # Nível 2: 101 a 200
        # Nível 3: 201 a 300
        # Nível 4: 301 a 400
        # ...
        
    # Menu
    def menu(self):
        while(True):
            self.updateUI()

            # print("[w | a | s | d] Mover")
            print("[b] Batalha\t\t [i] Inventário\t\t [e] Sair")
            print("[1] Player Status\t [2] Enemys Status\t [3] Itens Status" )
            option = input("Sua ação? ")
            if option == "e":
                break
            if option == "b":
                # Criar inimigo aleatório do mesmo nível do jogador 
                self.createRandomEnemy(self.players[0].getNivel())
                countEnemys = len(self.enemys)
                if countEnemys > 0:
                    # Busca um inimigo aleatório na lista de inimigos
                    i = random.randrange(0, countEnemys)
                    battle = Battle(self.players[0], self.enemys[i])
                    while(True):
                        self.updateUI()
                        battle.status()
                        if self.players[0].health <= 0:
                            input("Você morreu. Retornando para a cidade...")

                            #define Health inicial para 1000
                            self.players[0].setHealth(1000)
                            break
                        if self.enemys[i].health > 0:                       
                            option = input("Informe sua opção (h = hit, r = retornar): ")
                            if option == "h":
                                battle.hit()
                            elif option == "r":
                                break
                            else:
                                print("Opção inválida. Tente novamente...")
                        if self.enemys[i].health <= 0:
                            # print("Inimigo morto - XP: " + str(self.enemys[i].getExperience()))

                            #dropa itens aleatórios
                            items = self.enemys[i].getDrop()
                            for item in items:
                                if item.getType() == "Attack":
                                    self.weapons.append(item)
                                if item.getType() == "Defense":
                                    self.defenses.append(item)
                                item.status()
                            
                            del(self.enemys[i])
                            input("pressione <enter> para continuar... ")
                            self.updateUI()
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
            if option == "2":
                self.statusEnemys()
            if option == "3":
                self.statusItems()

    # Atualiza Interface
    def updateUI(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        healthBar = Bar(self.players[0].getHealth(), self.players[0].getHealthMax())
        manaBar = Bar(self.players[0].getMana(), self.players[0].getManaMax())
        staminaBar = Bar(self.players[0].getStamina(), self.players[0].getStaminaMax())
        xpBar = Bar(self.players[0].getExperience(), self.players[0].getExperienceNextNivel(), 40)

        print( \
        " ------------------------------------------------------------\n" + \
        "| Player: " + self.players[0].getName() + "\t\t   Gold: " + str(self.players[0].getGold()) + "\n" \
        "| Health: " + healthBar.show() + "\n" \
        "|   Mana: "  + manaBar.show() + "\n" \
        "|Stamina: " + staminaBar.show() + "\n" \
        "|  Power: " + str(self.players[0].getPower()) + "\n" \
        "|  Nivel: " + str(self.players[0].getNivel()) + "\n" \
        "|     XP: " + xpBar.show() + "\n" \
        " ------------------------------------------------------------\n")

    # Imprimir status dos jagadores
    def statusPlayers(self):
        for player in self.players:
            player.status()
            input("pressione uma tecla para continuar... ")

    # Imprimir status dos inimigos
    def statusEnemys(self):
        for enemy in self.enemys:
            enemy.status()
            input("pressione uma tecla para continuar... ")

    def statusItems(self):
        for w in self.weapons:
            w.status()
        
        for d in self.defenses:
            d.status()
        
        input("pressione uma tecla para continuar... ")            