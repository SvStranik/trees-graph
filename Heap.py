class Heap:

    def __init__(self):
        self.HeapArray = [] 
		
    def CreateArrayHeap(self,depth):
        self.HeapArray = [None] * (2**(depth+1)-1)
        return self.HeapArray

    def getHeapArray(self):
        return self.HeapArray

    def MakeHeap(self, a, depth):
        array_heap = self.CreateArrayHeap(depth)
        [self.Add(element_heap) for element_heap in a]

    def GetMax(self):
        array_heap = self.getHeapArray()
        try:
            if not array_heap or array_heap[0] == None : return -1
            position_el_add = array_heap.index(None) 
        except:
            position_el_add = len(array_heap)
        root_value = array_heap[0]
        array_heap[0] = array_heap[position_el_add-1]
        array_heap[position_el_add-1] = None
        position_el_add = 0
	
        def DeletElementInHeap(array_heap,position_el_add):
            index_left_node = (len(array_heap) - 1 if 2*position_el_add + 1 >= len(array_heap) else 2*position_el_add + 1)
            index_right_node = (len(array_heap) - 1 if 2*position_el_add + 2 >= len(array_heap) else 2*position_el_add + 2)
            if array_heap[index_left_node] and array_heap[index_right_node]:
                max_index_node = (index_left_node if array_heap[index_left_node] > 
                                  array_heap[index_right_node] else index_right_node)
            elif array_heap[index_left_node]:
                max_index_node = index_left_node
            else: return
            if array_heap[max_index_node] > array_heap[position_el_add]:
                array_heap[max_index_node],array_heap[position_el_add] = array_heap[position_el_add],array_heap[max_index_node]
                position_el_add = max_index_node
            else: return
            DeletElementInHeap(array_heap,position_el_add)
		
        DeletElementInHeap(array_heap,position_el_add)   
        return root_value

    def Add(self, key):
        array_heap = self.getHeapArray()
        try:
            position_el_add = array_heap.index(None)
            array_heap[position_el_add] = key
        except:
            return False
        
        def InsertElementInHeap(array_heap,position_el_add,position_parent = (position_el_add-1)//2):
            if position_el_add == 0 or array_heap[position_el_add] <= array_heap[position_parent]:
                return True
            else:
                array_heap[position_el_add],array_heap[position_parent] = array_heap[position_parent],array_heap[position_el_add]
                position_el_add = position_parent
            return InsertElementInHeap(array_heap,position_el_add,(position_el_add-1) //2)
        array_heap = InsertElementInHeap(array_heap,position_el_add)
        return array_heap
