
# this class implements breadth first search algorithm
class Graph:

    # constructor
    def __init__(self):
    
        # default dict to store nodes in the graph
        self.graph = {}
        self.path = {}
        self.backward_path = {}
        self.prev = {}
        
    # function to connect nodes by edges
    def connect_node(self, u, v):
        try:
            self.graph[u].append(v)
            
        except KeyError:
            self.graph[u] = [v]
            
        try:
            self.graph[v].append(u)
            
        except KeyError:
            self.graph[v] = [u]

                
    def print_graph(self):
        for node, conn_nodes in self.graph.items():
            for sec_node in conn_nodes:
                print(node,"<---->",sec_node)

    # function to print BFS of a graph
    def BFS(self, start):

        # list to remember the visits
        visited = [False]*(len(self.graph)+1)
        
        # queue for bfs
        queue_list, hist_queue_list = [], []       
        
        queue_list.append(start)
        hist_queue_list.append(start)
        visited[start] = True

        while queue_list:
            # dequeue the first element
            print('-'*15)
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

                    try:
                        self.path[vertex].append(i)
                        
                    except KeyError:
                        self.path[vertex] = [i]

                    try:
                        self.backward_path[i].append(vertex)
                        
                    except KeyError:
                        self.backward_path[i] = [vertex]

                    print(f'queue={queue_list},  history queue={hist_queue_list}, visited={visited},  vertex={vertex},  neighbor={i},  path={self.path},  bw path={self.backward_path}')
            
                    
        return self.path

         

if __name__ == "__main__":
    vertices = 7
    graph1 = Graph()    
    graph1.connect_node(0, 1)
    graph1.connect_node(0, 2)
    graph1.connect_node(1, 2)
    graph1.connect_node(2, 3)
    graph1.connect_node(3, 5)
    graph1.connect_node(3, 6)
    graph1.print_graph()
    paths = graph1.BFS(0)
    print(paths)

