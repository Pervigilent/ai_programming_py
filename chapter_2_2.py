#!/usr/bin/env python3
NODE_COUNT = 10
STACK_MAXIMUM = 10

adjacentNodes = []
visitedNodes = []
stack = []

stackIndex = 0

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

def initializeStack():
	global stackIndex
	stackIndex = 0

def push(element):
	global stack
	global stackIndex
	
	assert stackIndex < STACK_MAXIMUM

	stack.append(element)
	stackIndex = stackIndex + 1

def pop():
	global stackIndex
	
	assert stackIndex > 0

	stackIndex = stackIndex - 1
	return stack.pop()

def isEmpty():
	if stackIndex == 0:
		return True
	else:
		return False

def depthFirstSearch(startNode, goalNode):
	global visitedNodes
	global adjacentNodes
	
	push(startNode)
	while not isEmpty():
		node = pop()
	
		if node == goalNode:
			print("Goal reached ", node)
			return

		if visitedNodes[node]:
			continue
		else:
			visitedNodes[node] = True
			print(node, "\t")
			countdown = range(NODE_COUNT, 1, -1)
			for i in countdown:
				if adjacentNodes[node][i-1]:
					push(i)

	print("Goal not found.")
	return

def mainFunction():
	initializeMatrices()
	initializeStack()
	
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

	depthFirstSearch(1, 6)
	return

mainFunction()
