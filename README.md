# Directed_Graph_PY
### Ex3_Graph_Algorithms
## Sivan Cohen & Hodaya Turgeman

in this assigment we were required to implement and to design data structures and algorithms on graphs on python. <br>
We were required to implement the following interfaces: <br>
1. GraphInterface - DiGraph: <br>
2. GraphAlgoInterface - GraphAlgo <br>

**Node** <br>
for the implemention we implement an inner calss: "Node". This class represents a vertex in a directional weighted graph. <br>
for each node we save this information: its unique id, its position(x,y), and we make another field "tag" for computing needs. <br>

**GraphInterface  - DiGraph:** <br>
this interface represents a Directional Weighted Graph: <br>
each graph has set of nodes, set of edges, count which count the edges and mc which is count the changes in the graph. <br>
The data structures which we used are "dict" since it is very effective: <br>
- for the nodes we used dict when the id is the key and the value is the node itself. <br>
- for the edges we used two dict for getting better running time in some operations, so to represent an edge (x,y): <br>
in first dict: it keys are the src node, and the value is a dict which it keys are the dest node and the value is the weighted of the edge. <br>
in other words, key is the node src and its value is all the edge which go out of this node. <br>
in second dict: it keys are the dest node, and the value is a dict which it keys are the src node and the value is the weighted of the edge. <br>
in other words, key is the node dest and its value is all the edge which go into of this node. <br>
 
**GraphAlgoInterface - GraphAlgo** <br>
This interface represents a Directed (positive) Weighted Graph Theory Algorithms including: <br>
1. shortestPath: <br>
 we implement this method by using Dijkstra algorithm for finding the shortest path between two nodes so the sum of edge weight is minimal. <br>
2. center <br> 
this method finds the Node which minimizes the max distance to all the other nodes  <br> 
3. tsp <br>
  we used a greedy algorithem which compute the shortest path by Dijkstra algorithm. <br>
