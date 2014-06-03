from dfs import *
from random import randint

import time

import copy

class SafeNode(object):
    def __init__(self, value, exploding, parent=None):
        self.value = value
        self.exploding = exploding
        self.parent = parent


    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    @property
    def children(self):
        nodes = []
        #print "Self.value: ", self.value
        for i, val in enumerate(self.value):
            for j in [1, -1]:
                combo = (self.value[0:i] + ((val + j) % 10,) + self.value[i+1:4])
                n = SafeNode(combo, self.exploding, self)
                if not n.value in self.exploding:
                    nodes.append(n)
        return nodes

    def __repr__(self):
        return "<SafeNode: {0}, {1} {2}>".format(self.value, self.exploding,
                self.parent)




def reverse_nodes(start, end, last=None):
    print "Reverse start: ", start
    print "Reverse end: ", end
    if start.parent == end:
        start.parent = last
        return start
    start_copy = copy.copy(start)
    start.parent = last
    return reverse_nodes(start_copy.next, end, start)

def instructions(node):
    n = node
    l = [n.value]
    while n.parent != None:
        l.insert(0, n.parent.value)
        n = n.parent
    return l



if __name__ == "__main__":
    #node = SafeNode([0, 9, 0, 0])
    #print node.children([1, 9, 0, 0])
    print "Search: "
    start = SafeNode(tuple([randint(0, 9) for i in range(4)]),
            tuple([randint(0, 9) for i in range(4)] for i in
                range(randint(1,5))))
    target = SafeNode(tuple([randint(0, 9) for i in range(4)]), [])

    #start = SafeNode((0, 0, 0, 0), [])
    #target = SafeNode((0, 0, 1, 0), [])

    print "Initial value: ", start
    print "Exploding values: ", start.exploding
    print "Target: ", target

    #print reverse_nodes(target, start)

    #time.sleep(5)
    
    val = bfs_iter(start, target.value)
    print "Return :", val
    #print 
    print "Instructions: ", instructions(val)
