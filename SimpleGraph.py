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
        
    def AddVertex(self, v):
        list_vertex = self.getListVertex()
        for (i,j) in enumerate(list_vertex):
            if not j:
                list_vertex[i] = self.getObjectValueVertex(v)
                return list_vertex[i]
    
    def RemoveVertex(self, v):
        adjacency_matrix = self.getAdjacencyMatrix()
        for i in range(self.max_vertex):
            adjacency_matrix[v][i] = 0
            adjacency_matrix[i][v] = 0
    
    def IsEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        return (True if adjacency_matrix[v1][v2] == 
                        adjacency_matrix[v2][v1] == 1 else False)  
    
    def AddEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        adjacency_matrix[v1][v2] = 1
        adjacency_matrix[v2][v1] = 1
    
    def RemoveEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        adjacency_matrix[v1][v2] = 0
        adjacency_matrix[v2][v1] = 0


