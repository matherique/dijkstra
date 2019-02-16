#!/usr/bin/env python3
import random
import math

class City:
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
		print(self.__str__())
		for n in self.neigh:
			print("\t" + n.__str__())


numcities = 10
cities = [City() for _ in range(numcities)]
		

for city in cities:
	# numero randomico de vizinhos, de 1 a 10
	nn = random.randint(1, len(cities) - 2)

	# lista com todas as cidades - que esta no city do for
	othercities = list(filter(lambda c: c != city, cities))
	
	# se o numero de vizinho for menor que a quantidade escolhida em nn
	while len(city.neigh) - 1 < nn:
		# escolhendo uma cidade aleatoria
		rn = random.choice(othercities)

		# se a cidade nao estiver na lista de vizinhos, adiciona
		if rn not in city.neigh:
			city.addneigh(rn)
			othercities = list(filter(lambda c: c != rn, othercities))
		
	city.showneigh()








