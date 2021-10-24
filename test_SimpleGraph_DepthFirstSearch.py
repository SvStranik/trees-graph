from SimpleGraph_DepthFirstSearch import SimpleGraph
from SimpleGraph_DepthFirstSearch import Vertex
#from SimpleGraph_DepthFirstSearch import Stack

S = SimpleGraph(15)
for i in range(1,13):
    S.AddVertex(str(i))

listVertex = S.vertex
arr_Vertex = []
for i in listVertex:
    if i: 
        arr_Vertex.append(i.Value)
        arr_Vertex.append(i.Hit)
    else: arr_Vertex.append(None)
print(arr_Vertex)

S.AddEdge(0,1)
S.AddEdge(1,2)
S.AddEdge(1,5)
S.AddEdge(2,3)
S.AddEdge(3,4)
S.AddEdge(4,8)
S.AddEdge(4,7)
S.AddEdge(5,6)
S.AddEdge(5,10)
S.AddEdge(6,7)
S.AddEdge(7,11)
S.AddEdge(8,9)
S.AddEdge(9,10)
S.AddEdge(9,11)
S.AddEdge(10,11)

x = S.DepthFirstSearch(5,7)
print(x.stack)


"""arr_Vertex = []
for i in listVertex:
    if i: 
        arr_Vertex.append(i.Value)
        arr_Vertex.append(i.Hit)
    else: arr_Vertex.append(None)
print(arr_Vertex)"""