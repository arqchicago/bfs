
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

    # function to print BFS of a graph
    def BFS(self, start):
        print(self.graph)
        # list to remember the visits
        visited = [False]*(len(self.graph))
        prev =[-1]*(len(self.graph))
        
        # queue for bfs
        queue_list, hist_queue_list = [], []       
        
        queue_list.append(start)
        hist_queue_list.append(start)
        visited[start] = True

        while queue_list:
            # dequeue the first element
            vertex = queue_list.pop(0)
            for i in self.graph[vertex]:
                print(f'vertex={vertex} -- neighbor={i}')
            
            # get all neighbor vertices of the element
            # if the neighbor has not been visited, then mark it visited and enqueue it
            for i in self.graph[vertex]:
                if visited[i]==False:
                    queue_list.append(i)
                    hist_queue_list.append(i)
                    visited[i] = True
                    prev[i] = vertex
                    print(f'queue={queue_list},  history queue={hist_queue_list}, visited={visited},  vertex={vertex},  neighbor={i},  prev={prev}')
            
                    
        return prev

    def get_path(self, p1, p2, prev):
        path = []
        i = p2
        
        while(i!=-1): 
            path.append(i)
            i = prev[i]

        path.reverse()
        if path[0] == p1:
            return path
        else:
            return []

         

if __name__ == "__main__":
    graph1 = Graph()    
    graph1.connect_node(0, 1)
    graph1.connect_node(0, 2)
    graph1.connect_node(1, 2)
    graph1.connect_node(2, 0)
    graph1.connect_node(2, 3)
    graph1.connect_node(3, 3)
    graph1.print_graph()
    prev = graph1.BFS(0)

