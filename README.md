# Breath First Search algorithm
Breadth First Search algorithm for graphs is an algorithm to traverse nodes in the graph. The main purpose of this algorithm
is to visit each vertex through their connections while avoiding cycles or visiting a vertex twice. The algorithm starts at
a starting node and explores all nodes at the present depth, meaning that it explores other nodes that are neighbor of the
starting node, prior to moving on to the nodes at the next depth level. As the nodes are traversed, they are saved in a queue
so that the algorithm has a memory of the nodes that have already been traversed. During this process, the algorithm can keep
track of the connected paths between nodes. 

## Pseudocode
The following describes the pseudocode for breadth first search algorithm. The function takes as input a starting vertex and
returns a dictionary in which the key represents a vertex and values are lists containing vertices connected to the key vertex. 
The function also returns a list of all vertices that have been traversed by the algorithm.
![alt text](https://github.com/arqchicago/bfs/blob/main/data/bfs_pseudocode.png)

## More Info 2


