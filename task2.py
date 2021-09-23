class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        resultatFindNode = BSTFind()
        if self.Root == None: return resultatFindNode
        Node = self.Root
        while Node:
            resultatFindNode.Node = Node
            if Node.NodeKey == key: 
                resultatFindNode.NodeHasKey = True 
                return resultatFindNode
            if Node.NodeKey > key:
                Node = Node.LeftChild
                resultatFindNode.ToLeft = True
            else: 
                Node = Node.RightChild
                resultatFindNode.ToLeft = False
        return resultatFindNode


    def AddKeyValue(self, key, val):
        resultatFindNode = self.FindNodeByKey(key)
        if resultatFindNode.NodeHasKey == True:
            return False
        newNodeInAdd = BSTNode(key,val,resultatFindNode.Node)
        if resultatFindNode.Node == None:
            self.Root = newNodeInAdd
        elif resultatFindNode.ToLeft == False:
            resultatFindNode.Node.RightChild = newNodeInAdd
        else:
            resultatFindNode.Node.LeftChild = newNodeInAdd

  
    def FinMinMax(self, FromNode, FindMax):
        resultatFindNode = FromNode
        if FindMax:
            while resultatFindNode.RightChild != None:
                resultatFindNode = resultatFindNode.RightChild
        else:
            while resultatFindNode.LeftChild != None:
                resultatFindNode = resultatFindNode.LeftChild
        if resultatFindNode == FromNode: return None
        return resultatFindNode


    def ParentLeftChild(self,ReceivingNode,NodeToDelete):
            return (True if ReceivingNode.LeftChild == NodeToDelete else False)

    def DeleteNodeByKey(self, key):
        NodeToDelete = self.FindNodeByKey(key)
        if not NodeToDelete.NodeHasKey: return False   
        NodeToDelete = NodeToDelete.Node   
        if not NodeToDelete.LeftChild and not NodeToDelete.RightChild:
            if not NodeToDelete.Parent: 
                self.Root = None
                return
            ParentNode = NodeToDelete.Parent
            if self.ParentLeftChild(ParentNode,NodeToDelete):
                ParentNode.LeftChild = None
            else: ParentNode.RightChild = None
        else:
            ReceivingNode = NodeToDelete.LeftChild
            if NodeToDelete.RightChild:
                ReceivingNode = NodeToDelete.RightChild  
                if ReceivingNode.LeftChild:
                    ReceivingNode = self.FinMinMax(ReceivingNode,False)
                    NodeToDelete.RightChild.Parent = ReceivingNode
                    ReceivingNode.Parent.LeftChild = ReceivingNode.RightChild
                    ReceivingNode.RightChild = NodeToDelete.RightChild
                    ReceivingNode.LeftChild = NodeToDelete.LeftChild
                else:
                    ReceivingNode.LeftChild = NodeToDelete.LeftChild
            if not NodeToDelete.Parent:
                self.Root = ReceivingNode
            else:
                ReceivingNode.Parent = NodeToDelete.Parent
                if NodeToDelete.Parent.RightChild == NodeToDelete:
                    NodeToDelete.Parent.RightChild = ReceivingNode
                else: NodeToDelete.Parent.LeftChild = ReceivingNode
    def Count(self):
        def RecursionNode(Node):
            if Node:
                self.count += 1
                RecursionNode(Node.LeftChild)
                RecursionNode(Node.RightChild)
        self.count = 0
        RecursionNode(self.Root)
        return self.count
