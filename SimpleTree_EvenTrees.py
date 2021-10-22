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

    def EvenTrees(self):
        if self.Root == None or self.Count() % 2 != 0: return []
        
        def MakingTrees(Node,array_even_trees = []):
            
            def SumNodeTrees(Node):
                sum_node_trees = len(Node.Children)
                for i,j in enumerate(Node.Children):
                    sum_node_trees += SumNodeTrees(Node.Children[i])
                return sum_node_trees

            for i,j in enumerate(Node.Children):
                sum_node_trees = SumNodeTrees(Node.Children[i])
                if (sum_node_trees + 1) >= 2 and (sum_node_trees + 1) % 2 == 0:
                    array_even_trees.append(Node.Children[i].Parent.NodeValue)
                    array_even_trees.append(Node.Children[i].NodeValue)
                MakingTrees(Node.Children[i],array_even_trees)    
            return array_even_trees
            
        return MakingTrees(self.Root)
