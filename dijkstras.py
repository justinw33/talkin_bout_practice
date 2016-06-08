import math
class Node(object):

	def __init__(self, vertex, weight):

		self.vertex = vertex;
		self.weight = weight

	def __str__(self):
		return "[vertex: {}, weight {}]".format(self.vertex, self.weight)

	def __repr__(self):
		return str(self)

class BinaryMinHeapMap(object):

	def __init__(self):
		self.size = 0
		self.map = {}
		self.heap = Heap()

	def containsVertex(self, vertex):
		if vertex in self.map:
			return True
		return False

	def addToHeap(self, vertex, weight):
		if vertex in self.map:
			return
		else:
			n = Node(vertex, weight)
			self.map[vertex] = n
			self.heap.addToHeap(n)

		self.size += 1

	def setVertex(self, vertex, weight):
		if vertex in self.map:
			n = self.map[vertex]
			n.weight = weight
		else:
			self.addToHeap(vertex, weight)

	def extractMin(self):
		if self.size == 0:
			return

		n = self.heap.getMin()
		del self.map[n.vertex]
		self.size -= 1

		# def decreaseKey(self, vertex, weight):
		# def getKeyWeight(self, vertex):

	def __str__(self):
		return "map: {}, heap {}]".format(self.map, self.heap)

	def __repr__(self):
		return str(self)

# Heap class takes Node object whereever it says node in one of the paramters
class Heap(object):

	def __init__(self):
		self.heap = []
		self.size = 0
		self.DIVISOR = 2.0

	def addToHeap(self, node):
		self.heap.append(node)
		self.percolateUp(self.size)
		self.size += 1

	def getMin(self):

		min_node = self.heap[0]
		self.swap(0, self.size - 1)
		self.size -= 1
		self.percolateDown(0)

		return min_node

	def percolateUp(self, from_position):
		parent = int(math.ceil(from_position/self.DIVISOR)) - 1
		current = from_position

		while parent >= 0 and self.heap[parent].weight > self.heap[current].weight:
			self.swap(parent, current)
			current = parent
			parent = int(math.ceil(current/self.DIVISOR)) - 1

	def swap(self, position1, position2):
		node1 = self.heap[position1]
		node2 = self.heap[position2]

		self.heap[position1] = node2
		self.heap[position2] = node1

	def percolateDown(self, from_position):

		current = from_position
		left_child = (current * 2) + 1
		right_child = (current * 2) + 2

		current_weight = self.heap[current].weight

		while (right_child < self.size) and ((current_weight > self.heap[left_child].weight) or (current_weight > self.heap[right_child].weight)):
			if self.heap[left_child].weight > self.heap[right_child].weight:
				self.swap(right_child, current)
				current = right_child

			else: #self.heap[left_child].weight < self.heap[right_child].weight:
				self.swap(left_child, current)
				current = left_child

			left_child = (current * 2) + 1
			right_child = (current * 2) + 2


		if left_child < self.size and self.heap[left_child].weight < self.heap[current].weight:
			self.swap[left_child, current]
		
		del self.heap[-1]

	def __str__(self):
		return "{}".format(self.heap)







# testing
binaryMinHeapMap = BinaryMinHeapMap()
binaryMinHeapMap.addToHeap(1,10)
binaryMinHeapMap.addToHeap(2, 5)

print binaryMinHeapMap


