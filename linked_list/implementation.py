from .interface import AbstractLinkedList
from .node import Node


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """


    def __init__(self, elements=None):
        self.start = None
        self.end = None
        # self.next = None
        # if elements:
        #     for elem in elements:
        if elements:
            for elem in elements:
                self.append(elem)
                    
    def __str__(self):
        pass

    def __len__(self):
        aux = self.start
        count = 0
        while aux.next != None:
            count += 1
            
        return count

    def __iter__(self):
        # return iter(self.list)
        pass

    def __getitem__(self, index):
        # return self.list[index]
        pass

    def __add__(self, other):
        # would it be while other.list.next != none:
            #self.list.
            #append()
        # while self.list.next != None:
        #     self.list.next()
        # self.list.next = other.start
        #not sure what to put here]
        #we're supposed to use nodes?
        pass

    def __iadd__(self, other):
        pass

    def __eq__(self, other):
        # Assign dummies for both start nodes
        aux_s = self.start
        aux_o = other.start
        
        # To be equal, they must have same count and same elem
        # in each place
        # Assume True and test both criteria
        equal = True
        
        if self.count() != other.count():
            equal = False
            
        while aux_s != None and aux_o != None:
            if aux_s != aux_o:
                equal = False
                
        return equal

    def append(self, elem):
        if self.start == None:
            self.start = Node(elem)
            self.end = self.start
        else:
            aux = Node(elem)
            self.end.next = aux
            self.end = aux

    def count(self):
        # Start at 
        count = 0
        if self.start:
            count = 1
            aux = self.start
            while aux.next != None:
                count += 1
                aux = aux.next
        return count
        

    def pop(self, index=None):
        #pop remo
        return self.list.pop(index)
