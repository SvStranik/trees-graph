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
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        stack_pop_in_graph = Stack()                        # 0: Делаем стэк пустым
        list_vertex = self.getListVertex()
        #top_vfrom = list_vertex[VFrom]                       # 1: Выбираем текущую вершину

        def looking_for_a_way(list_vertex,top_vfrom,top_vto,stack_pop_in_graph):
            list_vertex[top_vfrom].Hit = True
            stack_pop_in_graph.push(top_vfrom)

            while True:
                if self.IsEdge(top_vfrom,top_vto):              # 4: пУНКТ 
                    stack_pop_in_graph.push(top_vto)
                    return stack_pop_in_graph
                else:
                    for i in range(len(list_vertex)):
                        if i != top_vfrom and self.IsEdge(top_vfrom,i) and list_vertex[i].Hit == False:
                            looking_for_a_way(list_vertex,i,top_vto,stack_pop_in_graph)
                    stack_pop_in_graph.pop()
                    if len(stack_pop_in_graph.stack) == 0: return "Путь не найден"
                    top_vfrom = stack_pop_in_graph.peek()
                    looking_for_a_way(list_vertex,top_vfrom,top_vto,stack_pop_in_graph)
                    
        
        return looking_for_a_way(list_vertex,VFrom,VTo,stack_pop_in_graph)