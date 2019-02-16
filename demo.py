#!/usr/bin/env python3
import random
import math

class Cidade:
    def __init__(self):
        self.x = random.uniform(0,1)
        self.y = random.uniform(0,1)
        self.neigh = []
        
    def calcdistance(self, cidade):
        x1, y1 = self.x, self.y
        x2, y2 = cidade.x, cidade.y
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 -y1, 2))  
    
    def __str__(self):
        return 'x: %f y: %f' % (self.x, self.y)
    
    def addneigh(self, neigh):
        self.neigh.append(neigh)

    def showneigh(self):
        for n in self.neigh:
            print(n.__str__())
    


numcidades = 10
cidades = []

for _ in range(numcidades):
    cidades.append(Cidade())

def generateconnections():
    for c in cidades:
        porcent = random.uniform(0,1)
        while porcent > .5:
            c.addneigh(random.choice(cidades))
            porcent = random.uniform(0,1)       


generateconnections()

