class Vertex:

    def __init__(self, val):
        self.Value = val

class SimpleGraph:
    
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def getListVertex(self):
        return self.vertex
        
    def getAdjacencyMatrix(self):
        return self.m_adjacency
        
    def getObjectValueVertex(self,val):
        return Vertex(val)
        
    def CheckingVertexes(self,v):
        list_vertex = self.getListVertex()
        try: return isinstance(list_vertex[v],Vertex)
        except: return False
            
    def AddVertex(self, v):
        list_vertex = self.getListVertex()
        for (i,j) in enumerate(list_vertex):
            if not j:
                list_vertex[i] = self.getObjectValueVertex(v)
                return
                
    def RemoveVertex(self, v):
        adjacency_matrix = self.getAdjacencyMatrix()
        if self.CheckingVertexes(v):
            for i in range(self.max_vertex):
                adjacency_matrix[v][i] = 0
                adjacency_matrix[i][v] = 0
    
    def IsEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        if self.CheckingVertexes(v1) and self.CheckingVertexes(v2):
            return (True if adjacency_matrix[v1][v2] == 
                            adjacency_matrix[v2][v1] == 1 else False)
        else: return False
            
    def AddEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        if self.CheckingVertexes(v1) and self.CheckingVertexes(v2):
            adjacency_matrix[v1][v2] = adjacency_matrix[v2][v1] =1
   
    def RemoveEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        if self.CheckingVertexes(v1) and self.CheckingVertexes(v2):
            adjacency_matrix[v1][v2] = adjacency_matrix[v2][v1] = 0
