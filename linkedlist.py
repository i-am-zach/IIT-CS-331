class LinkedList:
    class Node:
        def __init__(self, val, prior=None, next=None):
            self.val = val
            self.prior = prior
            self.next  = next
            
        def __str__(self):
            return self.val
        def __repr__(self):
            return str(self)
    
    def __init__(self):
        self.head = self.cursor = LinkedList.Node(None) # sentinel node (never to be removed)
        self.head.prior = self.head.next = self.head # set up "circular" topology
        self.length = 0
        
        
    ### prepend and append, below, from class discussion
        
    def prepend(self, value):
        n = LinkedList.Node(value, prior=self.head, next=self.head.next)
        self.head.next.prior = self.head.next = n
        self.length += 1
        
    def append(self, value):
        n = LinkedList.Node(value, prior=self.head.prior, next=self.head)
        n.prior.next = n.next.prior = n
        self.length += 1
            
            
    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self)
            if nidx < 0:
                nidx = 0
        return nidx
    
    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))

        i = 0
        if idx > (self.length - 1):
            raise IndexError()
        n = self.head
        while i < self._normalize_idx(idx):
            n = n.next
            i+=1
        return n.next.val

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
       
        i = 0
        if idx < 0 or idx > (self.length - 1):
            raise IndexError()
       
        n = self.head
        while i < idx:
            n = n.next
            i+=1
        n.next.val = value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        ind = self._normalize_idx(idx)
        if ind > (self.length - 1):
            raise IndexError()
       
        i = ind
        while i< self.length - 1:
            self[i] = self[i + 1]
            i += 1
        self[self.length - 1] = None
        self.length += -1

    ### cursor-based access ###
    
    def cursor_get(self): 
        """retrieves the value at the current cursor position"""
        assert self.cursor is not self.head
        return self.cursor.val
        

    def cursor_set(self, idx): 
        """sets the cursor to the node at the provided index"""
        assert idx>= 0 and idx < len(self)
        n = self.head.next
        for _ in range(idx):
            n = n.next
        # n is positioned on the node at index idx
        self.cursor = n

    def cursor_move(self, offset): 
        """moves the cursor forward or backward by the provided offset 
        (a positive or negative integer); note that it is possible to advance 
        the cursor by further than the length of the list, in which case the 
        cursor will just "wrap around" the list, skipping over the sentinel 
        node as needed"""
        assert len(self) > 0
        if offset == 0:
            return
        n = self.cursor
        if offset < 0:
            # Negative offset case
            offset = abs(offset)
            for i in range(offset):
                n = n.prior
                if n == self.head:
                    n = self.head.prior
            self.cursor = n
        elif offset > 0:
            # Positive offset case
            for i in range(offset):
                n = n.next
                if n == self.head:
                    n = self.head.next
            self.cursor = n
        
                    


    def cursor_insert(self, value): 
        """inserts a new value after the cursor and sets the cursor to the 
        new node"""
        n = LinkedList.Node(value, prior=self.cursor, next=self.cursor.next)
        self.cursor.next.prior = self.cursor.next = n
        self.cursor = n
        self.length += 1

    def cursor_delete(self):
        """deletes the node the cursor refers to and sets the cursor to the 
        following node"""
        assert self.cursor is not self.head and len(self) > 0
        self.cursor.next.prior = self.cursor.prior
        self.cursor.prior.next = self.cursor.next
        self.cursor = self.cursor.next
        self.length -= 1
        
        

    ### stringification ###
    
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        return str([val for val in self])
        
    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
            
        return str(self)

    ### single-element manipulation ###
        
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        
    
    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        
    
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        
    

    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Returns True if this LinkedList contains the same elements (in order) as
        other. If other is not an LinkedList, returns False."""
        

    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        


    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        return self.length
    
    def min(self):
        """Returns the minimum value in this list."""
        
    
    def max(self):
        """Returns the maximum value in this list."""
        
    
    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        
    
    def count(self, value):
        """Returns the number of times value appears in this list."""
        

    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_list`. Returns a new LinkedList
        instance that contains the values in this list followed by those 
        of other."""
        assert(isinstance(other, LinkedList))
        
    
    def clear(self):
        """Removes all elements from this list."""
        
        
    def copy(self):
        """Returns a new LinkedList instance (with separate Nodes), that
        contains the same values as this list."""
        

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        

            
    ### iteration ###

    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        for i in range(len(self)):
            yield self[i]
        