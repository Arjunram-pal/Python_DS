from collections import defaultdict

class Graph:
    
    def __init__(self):
        
        self.graph=defaultdict(list)
        
        
    def addEdge(self,u,v):
        
         self.graph[u].append(v)
         self.visited=[]
         
         
    def BFS(self,s):
        
        queue=[]
        
        queue.append(s)
        self.visited.append(s)
        
        
        while queue:
            
            s=queue.pop(0)
            print(s,end=" ")
            
            for i in self.graph[s]:
                if i not in self.visited:
                    queue.append(i)
                    self.visited.append(s)
                    
                
g=Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 2)

print("------")

g.BFS(1)
                
