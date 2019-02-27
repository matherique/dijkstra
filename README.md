Dijkstra 
------------

Generate a random graph with python and expose the nodes and arcs with flask app to a javascrip application using [p5.js](https://p5js.org) library


Libraries Used
----------------
- **flask** for server json object with graph information
- **flask_cors** for enable cors 
- **random** for randomize some stuff 
- **os** fot get env variables 


Usage
-------------
```bash
# generate graph and start flask server 
./demo.py

# generate graph with 10 nodes and start flask server
NUM=20 ./demo.py
