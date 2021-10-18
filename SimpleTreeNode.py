class SimpleTreeNode:
	
  
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent 
        self.Children = []
	
  
class SimpleTree:


    def __init__(self, root):
        self.Root = root
	

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
  

    def DeleteNode(self, NodeToDelete):
        
        def DelElChildren(NodeToDelete,NodeChildren):
            for i in range(len(NodeChildren.Children)):
                if NodeChildren.Children[i] == NodeToDelete:
                    NodeChildren.Children[i] = NodeChildren.Children[-1]
                    return NodeChildren.Children[:-1]

        ParentNode = NodeToDelete.Parent
        NodeToDelete.Parent = None 
        ParentNode.Children = DelElChildren(NodeToDelete,ParentNode)


    def GetAllNodes(self):
        if self.Root == None: return []
        Node = self.Root
        ListAllNodes = []
        ListAllNodes.append(Node)
        count = 0
        while count < len(ListAllNodes):
            Node = ListAllNodes[count]
            for i in Node.Children:
                ListAllNodes.append(i)
            count += 1
        return ListAllNodes


    def FindNodesByValue(self, val):
        ListNodes = self.GetAllNodes()
        ListNodesByValue = []
        for i in range(len(ListNodes)):
            if ListNodes[i].NodeValue == val:
                ListNodesByValue.append(ListNodes[i])
        return ListNodesByValue
   

    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent,OriginalNode)

   
    def Count(self):
        return len(self.GetAllNodes())


    def LeafCount(self):
        counter = 0
        for node in self.GetAllNodes():
            if node.Children == []:
                counter += 1
        return counter
