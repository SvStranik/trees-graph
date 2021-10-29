class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.queue: return []
        first_element = self.queue[0]
        self.queue = self.queue[1:]
        return first_element

    def size(self):
        return len(self.queue)

class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def NumberVertex(self):
        number = 0
        for i in self.vertex:
            if i != None:
                number += 1
        return number

    def getAdjacencyMatrix(self):
        return self.m_adjacency

    def getListVertex(self):
        return self.vertex
        
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

    def BreadthFirstSearch(self, VFrom, VTo):
        
        def LookingForVertex(current_vertex):
            for i in range(number_vertex):
                if i != current_vertex and list_vertex[i].Hit == False and self.IsEdge(current_vertex,i):
                    return i
            return -1

        def RezultataOutput(vertex_array,temp_per,list_vertex):
            short_way = [temp_per]
            for i in range(len(vertex_array)-1,-1,-1):
                if temp_per in vertex_array[i]:
                    temp_per = vertex_array[i][0]
                    short_way.append(temp_per)
            return [list_vertex[short_way[j]] for j in range(len(short_way)-1,-1,-1)]

        list_vertex = self.getListVertex()
        queue_pop_in_graph = Queue()
        if not self.CheckingVertexes(VFrom) or not self.CheckingVertexes(VTo): return []
        number_vertex = self.NumberVertex() 

        for i in range(number_vertex):
            list_vertex[i].Hit = False 
            
        current_vertex = VFrom                                       
        list_vertex[current_vertex].Hit = True
        queue_pop_in_graph.enqueue(current_vertex)
        vertex_array = []  
        temp_vertex_array = [current_vertex]   

        while True:
            next_vertex = LookingForVertex(current_vertex)
            if next_vertex == VTo:
                queue_pop_in_graph.enqueue(next_vertex)
                temp_vertex_array.append(next_vertex)
                vertex_array.append(temp_vertex_array)
                return RezultataOutput(vertex_array,next_vertex,list_vertex)
            elif next_vertex == -1:
                if queue_pop_in_graph.size() == 0: return []
                else:
                    current_vertex = queue_pop_in_graph.dequeue()
                    vertex_array.append(temp_vertex_array)
                    temp_vertex_array = [current_vertex]
            else:
                temp_vertex_array.append(next_vertex)
                list_vertex[next_vertex].Hit = True
                queue_pop_in_graph.enqueue(next_vertex)
