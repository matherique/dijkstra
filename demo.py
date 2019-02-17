#!/usr/bin/env python3
import random as r
import math
import os


class City:
	def __init__(self, start=False, end=False):		
		if start:
			self.x, self.y = 0, 0 
		elif end:	
			self.x , self.y = 1, 1
		else:
			self.x, self.y = r.random(), r.random()

		self.neigh = []	

	def calcdistance(self, cidade):
		x1, y1 = self.x, self.y
		x2, y2 = cidade.x, cidade.y
		return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 -y1, 2))  

	def __str__(self):
		return { 'x': self.x, 'y': self.y }
		# return 'x: %f y: %f' % (self.x, self.y)

	def addneigh(self, neigh):
		self.neigh.append(neigh)

	def showneigh(self):
		print(self.__str__())
		for n in self.neigh:
			print("\t" + n.__str__())
		
def generate():	
	numcities = int(os.environ.get('NUM')) if 'NUM' in os.environ else 4
	cities = [City(start=True), City(end=True)] + [City() for _ in range(numcities)]	

	lenc = len(cities) // 2
	for city in cities:
		nn = r.randint(1, lenc)
		othercities = list(filter(lambda c: c != city, cities))	
	
		while len(city.neigh) - 1 < nn:
			# escolhendo uma cidade aleatoria
			rn = r.choice(othercities)

			# se a cidade nao estiver na lista de vizinhos, adiciona
			if rn not in city.neigh:
				city.addneigh(rn)
				othercities = list(filter(lambda c: c != rn, othercities))

	return cities

def export(cities):
	lc = {}
	for i,c in enumerate(cities):
		lc[i] = c.__str__()
		lc[i]['neighbors'] = [cities.index(n) for n in c.neigh]
		
	return lc
		


from flask import Flask, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloworld():
	cities = generate()
	ej = export(cities)	
	return json.dumps(ej)


@app.route("/generate")
def newgraph():
	generate()
	return json.dumps({"generate" : True })


if __name__ == '__main__':
	app.run(debug=True)

