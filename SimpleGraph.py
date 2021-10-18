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
        
    def AddVertex(self, v):
        new_vertex = Vertex(v)
        list_vertex = self.getListVertex()
        for (i,j) in enumerate(list_vertex):
            if not j:
                list_vertex[i] = v
                return
    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        pass
    
    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        return False
    
    def AddEdge(self, v1, v2):
        adjacency_matrix = self.getAdjacencyMatrix()
        adjacency_matrix[v1][v2] = 1
        adjacency_matrix[v2][v1] = 1
        # добавление ребра между вершинами v1 и v2

    
    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        pass
