import math

class Node(object):

	def __init__(self, vertex_id, weight):

		self.vertex_id = vertex_id;
		self.weight = weight

	def __str__(self):
		return "[vertex_id: {}, weight {}]".format(self.vertex_id, self.weight)

	def __repr__(self):
		return str(self)

class BinaryMinHeapMap(object):

	def __init__(self):
		self.size = 0
		self.map = {}
		self.heap = Heap()

	# def containsVertex(self, vertex_id):
	# 	if vertex_id in self.map:
	# 		return True
	# 	return False

	def addToHeap(self, vertex_id, weight):
		if vertex_id in self.map:
			return
		else:
			n = Node(vertex_id, weight)
			self.map[vertex_id] = n
			self.heap.addToHeap(n)

		self.size += 1

	def setVertex(self, vertex_id, weight):
		if vertex_id in self.map:
			n = self.map[vertex_id]
			n.weight = weight
		else:
			self.addToHeap(vertex_id, weight)
		self.heap.rebuildHeap()

	def extractMin(self):
		if self.size == 0:
			return

		n = self.heap.getMin()
		del self.map[n.vertex_id]
		self.size -= 1
		return n

	def getVertexWeight(self, vertex_id):

		if vertex_id in self.map:
			v = self.map[vertex_id]
			return v.weight

		return None

	def vertexExist(self, vertex_id):
		if vertex_id in self.map:
			return True

		return False

	def __str__(self):
		# return "map: {}, heap {}]".format(self.map, self.heap)
		print "map"
		for vertex in self.map:
			print "{}".format(self.map[vertex])

		print "heap"
		print "{}".format(self.heap)

		return ""

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
		del self.heap[-1]

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
		print "current:{}, left_child:{}, right_child:{}, current_weight:{}, size:{}".format(current, left_child, right_child, current_weight, self.size)
		while (right_child < self.size) and ((current_weight > self.heap[left_child].weight) or (current_weight > self.heap[right_child].weight)):
			
			if self.heap[left_child].weight > self.heap[right_child].weight:
				self.swap(right_child, current)
				current = right_child

			else: 
				self.swap(left_child, current)
				current = left_child

			left_child = (current * 2) + 1
			right_child = (current * 2) + 2


		if left_child < self.size and self.heap[left_child].weight < self.heap[current].weight:
			self.swap(left_child, current)
		
	def rebuildHeap(self):
		parent = int(math.ceil(self.size/self.DIVISOR)) - 1
		for x in range(parent, -1, -1):
			self.percolateDown(x)

		return

	def __str__(self):
		return "{}".format(self.heap)

# # testing
# binaryMinHeapMap = BinaryMinHeapMap()
# binaryMinHeapMap.addToHeap(1,10)
# binaryMinHeapMap.addToHeap(2, 5)
# binaryMinHeapMap.extractMin()
# n = binaryMinHeapMap.getVertexWeight(1)

# print binaryMinHeapMap


