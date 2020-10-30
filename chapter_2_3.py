#!/usr/bin/env python3
NODE_COUNT = 10
QUEUE_MAXIMUM = 10

adjacentNodes = []
visitedNodes = []
queue = []

read = 0
write = 0

def initializeMatrices():
	global adjacentNodes
	global visitedNodes

	adjacentNodes = [[False for x in range(NODE_COUNT)] for x in range(NODE_COUNT)]
	visitedNodes = [False for x in range(NODE_COUNT)]

def makeEdge(startNode, endNode):
	global adjacentNodes

	assert startNode < NODE_COUNT
	assert endNode < NODE_COUNT
	
	adjacentNodes[startNode][endNode] = True

def Wrap(input):
	return 0 if (input == QUEUE_MAXIMUM - 1) else (input + 1)

def initializeQueue():
	global write
	global read

	write = 0
	read = 0

def isEmpty():
	global write
	global read

	if write == read:
		return True
	else:
		return False

def enqueue(element):
	global queue
	global write
	
	assert write < QUEUE_MAXIMUM 

	queue.append(element)
	write = Wrap(write) 

def dequeue():
	global queue
	global read 
	
	assert not isEmpty() 

	element = queue.pop(0)
	read = Wrap(read)
 
	return element 

def breadthFirstSearch(startNode, goalNode):
	global visitedNodes
	global adjacentNodes
	
	enqueue(startNode)
	while not isEmpty():
		node = dequeue()
	
		if node == goalNode:
			print("Goal reached ", node)
			return

		if visitedNodes[node]:
			continue
		else:
			visitedNodes[node] = True
			print(node, "\t")
			for i in range(0, NODE_COUNT):
				if adjacentNodes[node][i]:
					enqueue(i)

	print("Goal not found.")
	return

def mainFunction():
	initializeMatrices()
	initializeQueue()
	
	# Build our graph in the adjacency matrix
	makeEdge(1, 2)
	makeEdge(1, 3)
	makeEdge(1, 4)
	makeEdge(2, 5)
	makeEdge(3, 5)
	makeEdge(3, 6)
	makeEdge(4, 7)
	makeEdge(5, 8)
	makeEdge(5, 9)

	breadthFirstSearch(1, 9)
	return

mainFunction()
