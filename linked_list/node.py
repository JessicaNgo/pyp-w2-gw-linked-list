class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    # def __init__(self, elem):
    #     self.elem = elem
    #     self.next = None
    #     pass
    
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        # return self.elem
        pass
    def __eq__(self, other):
        # If both are None, return True; if one of two are None, return False
        if not self and not other:
            return True
        elif not self:
            return False
        elif not other:
            return False
        
        # If both have values, compare
        if self.elem == other.elem:
            return True
        else:
            return False
    
    def __repr__(self):
        pass

