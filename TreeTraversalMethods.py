class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None

    def setRightChild(self,Node):
        self.RightChild = Node

    def setLeftChild(self,Node):
        self.LeftChild = Node

    def setParent(self, Node):
        self.Parent = Node

    def getLeftChild(self):
        return self.LeftChild

    def getRightChild(self):
        return self.RightChild

    def getParentNode(self):
        return self.Parent

    def isLeftChild(self):
        return self.LeftChild

    def isRightChild(self):
        return self.RightChild

    def isParent(self):
        return self.Parent
    
    def isEmptyRoot(self):
        return self.Root == None
    
    def isKeysEqual(self,key):
        return self.NodeKey == key
    
    def isNodeKeyLardge(self,key):
        return self.NodeKey > key


class BSTFind:

    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False
  
    def isBSTToLeft(self):
        return self.ToLeft

    def getBSTNode(self):
        return self.Node

    def isNodeHasKey(self):
        return self.NodeHasKey

    def setLinkNode(self,Node):
        self.Node = Node

    def setNodeHasKey(self,bool = False):
        self.NodeHasKey = bool

    def setToLeft(self,bool = False):
        self.ToLeft = bool


class BST:

    def __init__(self, node):
        self.Root = node

    def getRootNode(self):
        return self.Root

    def FindNodeByKey(self, key):
        BSTFindNode = BSTFind()
        if BSTNode.isEmptyRoot(self): return BSTFindNode
        Node = self.getRootNode()
        while Node:
            BSTFindNode.setLinkNode(Node)
            if Node.isKeysEqual(key): 
                BSTFindNode.setNodeHasKey(True) 
                return BSTFindNode
            if Node.isNodeKeyLardge(key):
                Node = Node.getLeftChild()
                BSTFindNode.setToLeft(True)
            else: 
                Node = Node.getRightChild()
                BSTFindNode.setToLeft()
        return BSTFindNode


    def AddKeyValue(self, key, val):
        resultatFindNode = self.FindNodeByKey(key)
        if resultatFindNode.isNodeHasKey():
            return False
        newNodeInAdd = BSTNode(key,val,resultatFindNode.getBSTNode())
        if resultatFindNode.getBSTNode() == None:
            self.Root = newNodeInAdd
        elif not resultatFindNode.isBSTToLeft():
            resultatFindNode.getBSTNode().setRightChild(newNodeInAdd)
        else:
            resultatFindNode.getBSTNode().setLeftChild(newNodeInAdd)
        return True
  
    def FinMinMax(self, FromNode, FindMax):
        resultatFindNode = FromNode
        if FindMax:
            while resultatFindNode.getRightChild() != None:
                resultatFindNode = resultatFindNode.getRightChild()
        else:
            while resultatFindNode.getLeftChild() != None:
                resultatFindNode = resultatFindNode.getLeftChild()
        if resultatFindNode == FromNode: return None
        return resultatFindNode


    def ParentLeftChild(self,ReceivingNode,NodeToDelete):
            return (True if ReceivingNode.getLeftChild() == NodeToDelete else False)

    def DeleteNodeByKey(self, key):
        NodeToDelete = self.FindNodeByKey(key)
        if not NodeToDelete.isNodeHasKey(): 
            return False   
        NodeToDelete = NodeToDelete.getBSTNode()
        if not NodeToDelete.getLeftChild() and not NodeToDelete.getRightChild():
            if not NodeToDelete.getParentNode(): self.Root = None
            else:
                ParentNode = NodeToDelete.getParentNode()
                if self.ParentLeftChild(ParentNode,NodeToDelete):
                    ParentNode.setLeftChild(None)
                else: ParentNode.setRightChild(None)
        else:
            if NodeToDelete.getLeftChild() and NodeToDelete.getRightChild():
                ReceivingNode = NodeToDelete.RightChild
                if ReceivingNode.getLeftChild():
                    ReceivingNode = self.FinMinMax(ReceivingNode,False)
                    if ReceivingNode.getRightChild():
                        ReceivingNode.getRightChild().setParent(ReceivingNode.getParentNode())
                        ReceivingNode.getParentNode().setLeftChild(ReceivingNode.getRightChild())
                    else: ReceivingNode.getParentNode().setLeftChild(None)
                    ReceivingNode.setRightChild(NodeToDelete.getRightChild())
                    NodeToDelete.getRightChild().setParent(ReceivingNode)
                NodeToDelete.getLeftChild().setParent(ReceivingNode)
                ReceivingNode.setLeftChild(NodeToDelete.getLeftChild())
            elif NodeToDelete.getRightChild():
                ReceivingNode = NodeToDelete.getRightChild()
            else: ReceivingNode = NodeToDelete.getLeftChild()               
            if NodeToDelete.getParentNode():
                ReceivingNode.setParent(NodeToDelete.getParentNode())
                ParentNode = NodeToDelete.getParentNode()
                if self.ParentLeftChild(ParentNode,NodeToDelete): 
                    ParentNode.setLeftChild(ReceivingNode)
                else: ParentNode.setRightChild(ReceivingNode)
            else:
                self.Root = ReceivingNode
                ReceivingNode.setParent(None)
        NodeToDelete.setParent(None)
        NodeToDelete.setLeftChild(None)
        NodeToDelete.setRightChild(None)
        return True

    def Count(self):
        def RecursionNode(Node):
            if Node:
                self.counter += 1
                RecursionNode(Node.LeftChild)
                RecursionNode(Node.RightChild)
        self.counter = 0
        RecursionNode(self.Root)
        return self.counter

    def DeepAllNodes(self, parameter):
        ResultatDeepInNodes = []

        def PreOrder(Node,ResultatDeepInNodes):
            if Node:
                ResultatDeepInNodes.append(Node)
                PreOrder(Node.getLeftChild(),ResultatDeepInNodes)
                PreOrder(Node.getRightChild(),ResultatDeepInNodes)

        def PostOrder(Node,ResultatDeepInNodes):
            if Node:
                PostOrder(Node.getLeftChild(),ResultatDeepInNodes)
                PostOrder(Node.getRightChild(),ResultatDeepInNodes)
                ResultatDeepInNodes.append(Node)

        def InOrder(Node,ResultatDeepInNodes):
            if Node:
                InOrder(Node.getLeftChild(),ResultatDeepInNodes)
                ResultatDeepInNodes.append(Node)
                InOrder(Node.getRightChild(),ResultatDeepInNodes)
            
        if parameter == 0: 
            InOrder(self.Root,ResultatDeepInNodes)
        elif parameter == 1:
            PostOrder(self.Root,ResultatDeepInNodes)
        else:
            PreOrder(self.Root,ResultatDeepInNodes)
        return tuple(ResultatDeepInNodes)

    def WideAllNodes(self):
        Node = self.Root
        if self.Root == None: return None
        ResultatWideInNodes = [Node]
        TempArray = [Node]
        while TempArray:
            NodesLevel = []
            for NodeArray in TempArray:
                if NodeArray.isLeftChild():
                    NodesLevel.append(NodeArray.getLeftChild())
                if NodeArray.isRightChild():
                    NodesLevel.append(NodeArray.getRightChild())
            [ResultatWideInNodes.append(i) for i in NodesLevel]
            TempArray = NodesLevel
        return tuple(ResultatWideInNodes)
