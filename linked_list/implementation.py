from .interface import AbstractLinkedList
from linked_list.node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None 
        
        if elements:
            for element in elements:
                self.append(element)

    def __str__(self):
        result = []
        for item in self:
            element = item.elem
            result.append(element)
        print str(result)
        return str(result)

    def __len__(self):
        return self.count()

    def __iter__(self):
        aux_travel = self.start
        while aux_travel: #while aux_travel is not/make!=) None, but at the last node
            yield aux_travel
            aux_travel = aux_travel.next
        raise StopIteration

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        nonmutated = self.__class__() # new object(elements from old list) --> append to new object [1,2,3,4]
        for node in self:
            nonmutated.append(node.elem)
        for node in other:
            element = node.elem
            nonmutated.append(element)
        return nonmutated
        
        
    def __iadd__(self, other):
        for node in other:
            self.append(node.elem)
            
        return self

    def __eq__(self, other):
        
        if len(self) == len(other):
            other_node = other.start
            for item in self:
                #print item, other_node.elem WHY YOU NO PYTHON 3
                if item.elem != other_node.elem:
                    return False
                other_node = other_node.next
            return True
        return False
        
    def __ne__(self, other):
        # if self == other:
        #     return False
        # return True
        return not self == other 

    def append(self, elem):
        
        aux = Node(elem)
        
        if self.start is None:
            self.start = aux
            self.end = aux
        else:
            self.end.next = aux
            self.end = aux
        print self
        return self
        
        # my_list = linkedlist() -> .append(1)
        # 2nd_list = linkedlist([1])
    def count(self):
        count = 0
        for item in self:
            count += 1
        return count


    def pop(self, index=None):
        if len(self) == 0:
            raise IndexError
        if index > (len(self)-1):
            raise IndexError
        if len(self) ==1:
            pop = self.start.elem
            self.start = None
            self.end = None
            return pop
        if index is None or index == (len(self)-1):
            for i, node in enumerate(self): # [1,2,3] --pop--> [1,2] and 3
                if i is (len(self)-2): #go to second last element
                    pop = node.next 
                    node.next = None    #set next  = None
                    self.end = node     #set end pointer to node 
                    return pop.elem
        if index == 0:
            travel_node = self.start
            self.start = travel_node.next
            return travel_node.elem
        for i, node in enumerate(self):
            if i == (index-1): #[1, 2, 3, 4]
                pop = node.next
                node.next = node.next.next                #node.next.next.next.next.next.next.next.next.next.next.next.next
                return pop.elem
        
