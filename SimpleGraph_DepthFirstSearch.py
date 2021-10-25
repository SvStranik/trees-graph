class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() != 0:
            stack = self.stack[0]
            self.stack = self.stack[1:]
            return stack
        return None

    def push(self, value):
        new_stack = []
        new_stack.append(value)
        for i in range(self.size()):
            new_stack.append(self.stack[i])
        self.stack = new_stack[:]

    def peek(self):
        if self.size() != 0:
            return self.stack[0]
        return None 

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

    def DepthFirstSearch(self, VFrom, VTo):
        stack_pop_in_graph = Stack()                      
        list_vertex = self.getListVertex()
        if not self.CheckingVertexes(VFrom) or not self.CheckingVertexes(VTo):
            return stack_pop_in_graph.stack
        number_vertex = self.NumberVertex()
        for i in range(number_vertex):
            list_vertex[i].Hit = False
        while VFrom != None:                      
            list_vertex[VFrom].Hit = True      
            stack_pop_in_graph.push(VFrom)  
            if self.IsEdge(VFrom,VTo):
                stack_pop_in_graph.push(VTo)
                break 
            while len(stack_pop_in_graph.stack) >= 0: 
                for i in range(number_vertex):
                    if i != VFrom and list_vertex[i].Hit == False and self.IsEdge(VFrom,i):
                        VFrom = i
                        break
                else:   
                    stack_pop_in_graph.pop()
                    if len(stack_pop_in_graph.stack) == 0: return stack_pop_in_graph.stack
                    VFrom = stack_pop_in_graph.peek()
                    continue
                break
        return [list_vertex[stack_pop_in_graph.stack[i]] for i in range(len(stack_pop_in_graph.stack)-1,-1,-1)]
