import logging

class Heap:
    def __init__(self, key=lambda x:x):
        self.data = []
        self.key  = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2
        
    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2
    
    def heapify(self, idx=0):
        p = 0
        l = Heap._left(p)
        r = Heap._right(p)
        while r < len(self):
            # Case for right side is greater than left side
            if self.key(self.data[r]) > self.key(self.data[l]):
                # Check if the parent is the max value
                if self.key(self.data[p]) >= self.key(self.data[r]):
                    return
                else:
                    self.data[p], self.data[r] = self.data[r], self.data[p]
                    p = r
                    l = Heap._left(p)
                    r = Heap._right(p)
            # Case for left side is greater than the right side
            else:
                # Check if the parent is the max value
                if self.key(self.data[p]) >= self.key(self.data[l]):
                    return
                else:
                    self.data[p], self.data[l] = self.data[l], self.data[p]
                    p = l
                    l = Heap._left(p)
                    r = Heap._right(p)
        # Checks if tree has a left node
        if l < len(self):
            # Swaps if the left node is greater than the parent node
            if self.key(self.data[l]) > self.key(self.data[p]):
                self.data[p], self.data[l] = self.data[l], self.data[p]
            
                    
            
    def add(self, x):
        i = len(self.data)
        p = Heap._parent(i)
        self.data.append(x)
        while i != 0 and self.key(self.data[i]) > self.key(self.data[p]):
            self.data[i], self.data[p] = self.data[p], self.data[i]
            i = p
            p = Heap._parent(i)
        
    def peek(self):
        return self.data[0]

    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        self.heapify()
        return ret
    
    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)
    
def running_medians(iterable):
    medians = []
    min_heap = Heap(lambda x: -x)
    max_heap = Heap(lambda x: x)
    for elem, num_elems in enumerate(iterable):
        num_elems += 1
        if medians and elem > medians[-1]:
            min_heap.add(elem)
        else:
            max_heap.add(elem)
        
        if len(max_heap) - len(min_heap) > 1:
            min_heap.add(max_heap.pop())
        elif len(min_heap) - len(max_heap) > 1:
            max_heap.add(min_heap.pop())
        
        # Even number of elements so divide
        if num_elems % 2 == 0:
            high, low = min_heap.pop(), max_heap.pop()
            medians.append((high + low) / 2)
            min_heap.add(high)
            max_heap.add(low)
        # Odd number of elements; median is root of Heap with more values
        else:
            if len(max_heap) > len(min_heap):
                med = max_heap.pop()
                medians.append(med)
                max_heap.add(med)
            else:
                med = min_heap.pop()
                medians.append(med)
                min_heap.add(med)
            
            
    return medians    
