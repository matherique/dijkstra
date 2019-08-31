Dijkstra 
------------

Generate a random graph with python and expose the nodes and arcs with flask app in api form to a javascript application using [p5.js](https://p5js.org) library


Libraries Used
----------------
- **flask**: server json object with graph information
- **flask_cors**: enable cors 
- **random**:randomize some stuff 
- **os**: get env variables 


Usage
-------------
```bash
# generate graph and start flask server 
./demo.py

# generate graph with 10 nodes and start flask server
NUM=20 ./demo.py
```

TODO
-------------
- Find best path with Dijkstra
- Add genetic algorithm to compete with Dijkstra
