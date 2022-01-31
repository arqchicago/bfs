
# this class implements breadth first search algorithm
class Graph:

    # constructor
    def __init__(self):
    
        # default dict to store nodes in the graph
        self.graph = {}
        
    # function to connect nodes by edges
    def connect_node(self, u, v):
        try:
            u_len = len(self.graph[u])
            self.graph[u].append(v)
            
        except KeyError:
            self.graph[u] = [v]
                
    def print_graph(self):
        for node, conn_nodes in self.graph.items():
            for sec_node in conn_nodes:
                print(node,"---->",sec_node)

         

if __name__ == "__main__":
    graph1 = Graph()    
    graph1.connect_node(0, 1)
    graph1.connect_node(0, 2)
    graph1.connect_node(1, 2)
    graph1.connect_node(2, 0)
    graph1.connect_node(2, 3)
    graph1.connect_node(2, 4)
    graph1.connect_node(3, 4)
    graph1.connect_node(4, 4)
    graph1.print_graph()

