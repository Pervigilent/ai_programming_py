class MemberType:
	'Member object for storing solution board'
	#solution
	#energy
	#boardLength

	def __init__(self, boardLength):
		self.boardLength = boardLength
		self.initializeSolution()

	def initializeSolution(self):
		self.solution = [*range(self.boardLength)]
		#self.solution = [x + 1 for x in self.solution]

	def computeEnergy(self):
		board = []
		for var in list(range(self.boardLength)):
			temporary = ['\0'] * self.boardLength
			temporary[self.solution[var]] = 'Q'
			board.append(temporary)
		conflicts = 0
		tempX = (-1, 1, -1, 1)
		tempY = (-1, 1, 1, -1)
		for var in list(range(self.boardLength)):
			currentX = var
			currentY = self.solution[var]
			for i in list(range(4)):
				xLocation = currentX + tempX[i]
				yLocation = currentY + tempY[i]
				if xLocation >= 0 and yLocation >= 0 and xLocation < self.boardLength and yLocation < self.boardLength:
					if board[xLocation][yLocation] == 'Q':
						conflicts += 1
		self.energy = conflicts
		return conflicts

BOARD_LENGTH = 10
sample = MemberType(BOARD_LENGTH)
energy = sample.computeEnergy()
print(energy)