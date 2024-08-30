class Graph:
# Constructor
    def __init__(self):
# default dictionary to store graph
      self.graph = defaultdict(list)
# function to add an edge to graph
    def addEdge(self,u,v):
      self.graph[u].append(v)
# Function to print a BFS of graph
    def BFS(self, s):
# Mark all the vertices as not visited
      visited = [False] * (max(self.graph) + 1)
      queue = []
      queue.append(s)
      visited[s] = True
      while queue:
         s = queue.pop(0)
         print (s, end = " ")
         for i in self.graph[s]:
            if visited[i] == False:
               queue.append(i)
               visited[i] = True
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Following is Breadth First Traversal")