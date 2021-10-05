class aBST:

    def __init__(self, depth):
        tree_size = self.TreeSize(depth)
        self.Tree = [None] * tree_size
        self.Depth = depth

    def IndexLeftChild(self,index):
        return 2 * index + 1
        

    def IndexRightChild(self,index):
        return 2 * index + 2

    def TreeSize(self,depth):
        tree_size = 1
        temp_variable = 1
        while depth != 0:
            temp_variable *= 2
            tree_size += temp_variable
            depth -= 1
        return tree_size

    def FindKeyIndex(self, key):
        NodeIndex = 0
        counter = self.Depth +1
        while counter:
            if self.Tree[NodeIndex] == key:
                return NodeIndex
            if self.Tree[NodeIndex] == None:
                return NodeIndex * -1
            if self.Tree[NodeIndex] < key:
                NodeIndex = self.IndexRightChild(NodeIndex)
            else:
                NodeIndex = self.IndexLeftChild(NodeIndex)
            counter -= 1
        return None
    
    def AddKey(self, key):
        NodeIndex = self.FindKeyIndex(key)
        if NodeIndex == None: return -1
        if NodeIndex == 0:
            if self.Tree[NodeIndex] == None:
                self.Tree[NodeIndex] = key
            return NodeIndex
        elif NodeIndex > 0:
            return NodeIndex
        else:
            NodeIndex *= -1
            self.Tree[NodeIndex] = key
            return NodeIndex
