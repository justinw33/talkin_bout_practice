from generictree import GenericNode
from collections import deque

n7 = GenericNode(7)
n6 = GenericNode(6)
n5 = GenericNode(5, None, n6)
n4 = GenericNode(4, n7)
n3 = GenericNode(3, None, n4)
n2 = GenericNode(2, n5, n3)
n1 = GenericNode(1, n2)

queue = deque()
queue.append(n1)
total = 0
while len(queue) > 0:
    n = queue.popleft()
    total += n.data

    if n.first_child != None:
        queue.append(n.first_child)

    if n.next_sibling != None:
        queue.append(n.next_sibling)

print total
