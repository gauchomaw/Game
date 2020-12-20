
from enum import Enum

    #Attack
        #1.1 ADAGAS
        #1.2 ARCOS
        #1.3 CAJADOS/VARINHAS
        #1.4 ESPADAS
        #1.5 FANTASMAS
        #1.6 FOICES
        #1.7 GARRAS
        #1.8 LANÇAS
        #1.9 MACHADOS
        #1.10 MARTELOS
        #1.11 PUNHOS
        
    #Defense
        #2.1 ARMADURAS
        #2.2 ROUPÕES
        #2.3 ESCUDOS
        #2.4 ORBITAIS
        #2.5 LUVAS
        #2.6 BRACELETES
        #2.7 BOTAS 
    #Accessory    
        #3.1 AMULETOS
        #3.2 ANÉIS
        #3.3 SHELTOMS
        #3.4 BRINCOS 

#Enum com os tipos dos itens
class Typei(Enum):
    Attack = 1
    Defense = 2
    Accessory = 3

#Representa todos os itens do jogo: weapon, armor, ring, etc...
class Item():
    def __init__(self, name, typei):
        self.name = name
        self.typei = typei
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setType(self, typei):
        self.typei = typei
    
    def getType(self):
        return self.typei