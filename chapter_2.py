NODE_COUNT = 10
STACK_MAXIMUM = 10

adjacentNodes = []
visitedNodes = []

def initializeMatrices():
	adjacentNodes = [[False for x in range(NODE_COUNT)] for x in range(NODE_COUNT)]
	visitedNodes = [False for x in range(NODE_COUNT)]

