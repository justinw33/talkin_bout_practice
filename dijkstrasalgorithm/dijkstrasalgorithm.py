from dijkstras import BinaryMinHeapMap
import sys

class Vertex(object):

	def __init__(self, id):
		self.adj_list = {}
		self.id = id

	def addEdge(self, adj_vertex, weight):
		self.adj_list[adj_vertex.id] = weight

	def __str__(self):
		return "id: {}, adj_list: {}".format(self.id, self.adj_list)

	def __repr__(self):
		return str(self)

class Graph(object):

	def __init__(self):
		self.vertex = {}

	def addVertex(self, vertex_id):
		vertex = Vertex(vertex_id)
		self.vertex[vertex_id] = vertex

	def addEdge(self, vertex1_id, vertex2_id, weight):

		if vertex1_id in self.vertex:
			vertex1 = self.vertex[vertex1_id]
		else:
			self.addVertex(vertex1_id)
			vertex1 = self.vertex[vertex1_id]

		if vertex2_id in self.vertex:
			vertex2 = self.vertex[vertex2_id]
		else:
			self.addVertex(vertex2_id)
			vertex2 = self.vertex[vertex2_id]

		vertex1.addEdge(vertex2, weight)
		vertex2.addEdge(vertex1, weight)

	def getVertex(self, vertex_id):
		if vertex_id in self.vertex:
			return self.vertex[vertex_id]

	def __str__(self):
		for x in self.vertex:
			print self.vertex[x] 
		return ""


def shortestPath(graph, start_node):

	heap_map = BinaryMinHeapMap()
	
	# contain shortest path
	vertex_map = {}

	#shortest route
	shortest_route = {}

	# initilizing binaryminheap
	for vertex in graph.vertex:
		heap_map.addToHeap(vertex, sys.maxint)

	heap_map.setVertex(start_node, 0)
	shortest_route[start_node] = None
	print heap_map
	while heap_map.size > 0:
		
		# node contains vertex_id and weight
		current_node = heap_map.extractMin()

		vertex_map[current_node.vertex_id] = current_node.weight 

		# get adjacency list
		current_vertex = graph.getVertex(current_node.vertex_id)

		for neighbor in current_vertex.adj_list:
			if heap_map.vertexExist(neighbor):
				neighbor_distance = heap_map.getVertexWeight(neighbor)

				new_distance = (current_node.weight + current_vertex.adj_list[neighbor])
				# print "new {}, old: {}".format(new_distance, neighbor_distance)

				if new_distance < neighbor_distance:
					heap_map.setVertex(neighbor, new_distance)
					shortest_route[neighbor] = current_vertex.id

	print "shortest route: {}".format(shortest_route)





	return

graph = Graph()
graph.addEdge(1,2,5)
graph.addEdge(2,3,2)
graph.addEdge(3,4,3)
graph.addEdge(1,4,9)
graph.addEdge(1,5,3)
graph.addEdge(5,6,2)
graph.addEdge(6,4,2)

shortestPath(graph, 1)

# print graph

