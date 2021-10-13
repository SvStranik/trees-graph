class BSTNode:
    

    def __init__(self, key, parent):
        self.NodeKey = key 
        self.Parent = parent
        self.LeftChild = None 
        self.RightChild = None
        self.Level = 0 


class BalancedBST:
        

    def __init__(self):
        self.Root = None


    def GenerateTree(self, a):
        array_sorted = sorted(a)
        root_node = self.Root

        def RecursivGenerateTree(root_node,array_sorted,Level = 0):
            central_element = len(array_sorted) // 2
            if not array_sorted == []:
                NewNode = BSTNode(array_sorted[central_element],root_node)
                NewNode.Level = Level 
                NewNode.LeftChild = RecursivGenerateTree(NewNode,array_sorted[:central_element],Level + 1)    
                NewNode.RightChild = RecursivGenerateTree(NewNode,array_sorted[central_element+1:],Level + 1)
                return NewNode
                
        return RecursivGenerateTree(root_node,array_sorted)


    def IsBalanced(self, root_node):

        def IsCorrectTree(root_node):
            if root_node:
                if root_node.LeftChild:
                    if root_node.NodeKey < root_node.LeftChild.NodeKey: return False
                if root_node.RightChild:
                    if root_node.NodeKey > root_node.RightChild.NodeKey: return False
                IsCorrectTree(root_node.LeftChild)
                IsCorrectTree(root_node.RightChild)
            return True

        if not IsCorrectTree(root_node): return False

        left_subtree = root_node.LeftChild
        right_subtree = root_node.RightChild

        def RecursivTreeDepths(root_node):
            if not root_node: return 0
            LeftNode = RecursivTreeDepths(root_node.LeftChild)
            RigftNode = RecursivTreeDepths(root_node.RightChild)
            return max(LeftNode,RigftNode) + 1

        quantity_left_subtree = RecursivTreeDepths(left_subtree)
        quantity_right_subtree = RecursivTreeDepths(right_subtree)
        max_quantity_subtree = max(quantity_left_subtree,quantity_right_subtree) 
        min_quantity_subtree = min(quantity_left_subtree,quantity_right_subtree)

        return (quantity_left_subtree == quantity_right_subtree or 
                max_quantity_subtree == min_quantity_subtree + 1)
