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

    def NumberVertex(self):
        number = 0
        for i in self.vertex:
            if i != None:
                number += 1
        return number       
        
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
                adjacency_matrix[v][i] = adjacency_matrix[i][v] = 0
    
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

    def WeakVertices(self):
        list_vertex = self.getListVertex()
        number_vertex = self.NumberVertex()
        list_vertex_triangle = []
        list_edges_triangle = []

        def SearchAdjacentVertex(number_vertex,parent_vertex,result_vertex):
            for i in range(number_vertex):
                if i != parent_vertex and self.IsEdge(i,parent_vertex):
                    result_vertex.append(i)
            return result_vertex

        vertex_not_triangle = []
        for position in range(number_vertex):
            if position not in list_vertex_triangle:
                adjacent_vertex = SearchAdjacentVertex(number_vertex,position,[])
                if len(adjacent_vertex) < 2: vertex_not_triangle.append(list_vertex[position])
                else:    
                    flag = True
                    for i in range(len(adjacent_vertex)):
                        for j in range(i+1,len(adjacent_vertex)):
                            if [adjacent_vertex[i],adjacent_vertex[j]] in list_edges_triangle:
                                flag = False
                                continue
                            if self.IsEdge(adjacent_vertex[i],adjacent_vertex[j]):
                                list_edges_triangle.append([adjacent_vertex[i],adjacent_vertex[j]])
                                list_vertex_triangle.append(adjacent_vertex[i])
                                list_vertex_triangle.append(adjacent_vertex[j])
                                flag = False
                    if flag: vertex_not_triangle.append(list_vertex[position])
        return vertex_not_triangle
    