from node import Node

def dfs(node, val, stack=[]):
    if not node:
        node = stack.pop()
    print "Node: ", node
    if node.value == val:
        return node
    [stack.append(c) for c in node.children]
    return dfs(None, val, stack)

def bfs(node, val, queue=[]):
    if not node:
        node = queue.pop()
    print "Node: ", node
    if node.value == val:
        print "Returning", node
        return node
    [queue.insert(0, c) for c in node.children]
    return bfs(None, val, queue)

def dfs_iter(node, val):
    print "Node: ", node
    if node.value == val:
        return node
    stack = []
    [stack.append(c) for c in node.children]
    while True:
        if len(stack) == 0:
            return
        n = stack.pop()
        print "Node: ", n
        if n.value == val:
            return n
        [stack.append(c) for c in n.children]


def bfs_iter(node, val):
    #print "Node: ", node
    if node.value == val:
        return node
    vals = 0
    queue = []
    seen = set()
    [queue.insert(0, c) for c in node.children]
    while True:
        if len(queue) == 0:
            return
        n = queue.pop()
        if n in seen:
            continue
        vals += 1
        #if vals % 1000 == 0:
        #    print n
        seen.add(n)
        #print "Node: ", n
        if n.value == val:
            #print "Final node: ", n
            return n
        [queue.insert(0, c) for c in n.children]

if __name__ == "__main__": 
    g = Node('g')
    h = Node('h')
    e = Node('e', h)
    f = Node('f', g)
    d = Node('d')
    c = Node('c')
    b = Node('b', e, f)
    a = Node('a', b, c, d)
    
    node1 = Node('c')
    node2 = Node('b', node1)
    node3 = Node('a', node2)
    #print dfs(node3, 'c').value
    #print dfs_iter(a, 'g').value
    #print bfs_iter(a, 'g').value
