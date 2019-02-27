let cidades = {}
let w = 500;
let h = 500;
let c = []
let b = 50

function preload() {
	cidades = loadJSON('http://localhost:5000');
}

function setup() {
	createCanvas(w, h)
	for (let i = 0; i < Object.keys(cidades).length; i++) {
		c.push(new City(cidades[i].x, cidades[i].y, cidades[i].neighbors))
	}
}

function draw() {
	background(51);
	for (let i = 0; i < c.length; i++) {
		cidade = c[i]
		cidade.show();
		cidade.exibirLigacoes()

	}

}

class City {
	constructor(x, y, neigh) {
		this.x = (x == 0) ? b : x * (w - b);
		this.y = (y == 0) ? b : y * (h - b);
		this.neigh = neigh
	}

	show() {
		fill(255);
		ellipse(this.x, this.y, 20, 20);
	}
	exibirLigacoes() {
		this.neigh.forEach(n => {
			let cd = c[n]
			stroke(255)
			line(this.x, this.y, cd.x, cd.y)
		});
	}

}
