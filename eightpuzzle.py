import math
import time

goalState = [[1,2,3],
			 [4,5,6],
			 [7,8,0]]

class EightPuzzle:

	def __init__(self):
		#initialization
		self.parent = 0
		self.state = [[1,2,3],
					  [4,0,6],
					  [7,5,8]]
		self.hn = 0
		self.depth = 0


	def printState(self):
		#helper function to print out the state
		for i in range(len(self.state)):
			print self.state[i][0], self.state[i][1], self.state[i][2]

		print "\n"


	def copy(self):
		cpy = EightPuzzle()
		for row in range(3):
			for col in range(3):
				cpy.state[row][col] = self.state[row][col]
		return cpy

	def printSolutionTree(self):
		if self.parent == 0:
			print "Expanding state"
			self.printState()
		else:
			self.parent.printSolutionTree()
			print "The best state to expand with a g(n) = " + str(self.depth) +  " and h(n) = " + str(self.hn) + " is... "
			self.printState()

	def setPuzzle(self):

		print "Type \"1\" to use the default puzzle or \"2\" to enter your own: ",
		while (True):
			whichPuzzle = input()
			if(whichPuzzle == 1):
				self.state = [[1,2,3],
							  [4,0,6],
							  [7,5,8]]
				return
			elif(whichPuzzle == 2):
				print "Enter your puzzle, use a zero to represent the blank"
				print "Enter the 1st row, use space or tabs between numbers: "
				a = raw_input()
				row1 = map(int, a.split())
				print "Enter the 2nd row, use space or tabs between numbers: "
				a = raw_input()
				row2 = map(int, a.split())
				print "Enter the 3rd row, use space or tabs between numbers: "
				a = raw_input()
				row3 = map(int, a.split())	

				self.state = [row1, row2, row3]	
				return
			print "Please input 1 or 2: "
			
		
		

	def findColumn(self, value):
		#returns row and column coords
		if value > 8 or value < 0:
			raise Exception("out of range")

		for row in range(3):
			for column in range(3):
				if self.state[row][column] == value:
					return column

	def findRow(self, value):
		#returns row and column coords
		if value > 8 or value < 0:
			raise Exception("out of range")

		for row in range(3):
			for column in range(3):
				if self.state[row][column] == value:
					return row

	def findLegalMoves(self):
		# get row and column of the 0 cursor
		row = self.findRow(0)
		column = self.findColumn(0)
		free = []

		
		# find legal moves

		if row < 2:
			free.append((row + 1, column))
		if column < 2:
			free.append((row, column + 1))
		if row > 0:
			free.append((row - 1, column))
		if column > 0:
			free.append((row, column - 1))

		return free

	def createMoves(self):
		moveList = []
		legalMoves = self.findLegalMoves()

		cursor = self.findRow(0), self.findColumn(0)


		for i in legalMoves:
			move = self.copy()
			move.swap(cursor,i)
			move.depth = self.depth + 1
			move.parent = self
			moveList.append(move)

		return moveList


		#to move the cursor
	def swap(self, x, y):
		xrow, xcol = x

		xtemp = self.state[xrow][xcol]
		yrow, ycol = y

		self.state[xrow][xcol] = self.state[yrow][ycol]
		self.state[yrow][ycol] = xtemp


		#recursive function to generate the solution path
	def pathToSolution(self, path):


		if self.parent == 0:

			return path
		else:
			
			path.append(self)
			return self.parent.pathToSolution(path)

	def solver(self, heuristicFunction):

		nodes = [self]
		closed = []
		maxNodesinQueue = -1
		totalNodesExpanded = 0


		while True:

			if(len(nodes) < 1):
				return [], 0, 0

			front = nodes.pop(0)

			if maxNodesinQueue < len(nodes):
				maxNodesinQueue = len(nodes)


			#check if solved
			if (front.state == goalState):
				if len(closed) > 0:
					goalDepth = front.depth
					return front.pathToSolution([]), totalNodesExpanded, maxNodesinQueue
				else:
					return [front], totalNodesExpanded, maxNodesinQueue

			#if it's not solved, see what moves we can make
			
			possibleMoves = front.createMoves()

			indexNodes = -1
			indexClosed = -1

			for currMove in possibleMoves:

				#check if we have seen this move
				count = 0
				foundFlag = False

				if len(nodes) != 0:
					for i in nodes:
						#if currMove == i:
						if currMove.state == i.state:
							indexNodes = count
							foundFlag = True
							break
						count += 1

					if not foundFlag:
						indexNodes = -1

				count = 0
				foundFlag = False	

				if len(closed) != 0:

					for i in closed:
						#if currMove == i:
						if currMove.state == i.state:
							indexClosed = count
							foundFlag = True
							break
						count += 1

					if not foundFlag:
						indexClosed = -1



				#setting h(n)

				hn = heuristicFunction(currMove)
				#total cost

				cost = hn + currMove.depth

				#if current move hasnt been seen yet
				if indexNodes == -1 and indexClosed == -1:
					currMove.hn = hn
					nodes.append(currMove)

					totalNodesExpanded += 1

				#else if node is in the queue

				elif indexNodes > -1:
					#make a copy
					copy = nodes[indexNodes]

					#check if this move is better
					if cost < copy.hn + copy.depth:
						#if it's better copy over the cost
						copy.hn = hn
						copy.parent = currMove.parent
						copy.depth = currMove.depth


				#else if node is has already been closed
				elif indexClosed > -1:
					#make a copy
					copy = closed[indexClosed]


					if cost < copy.hn + copy.depth:

						currMove.hn = hn
						closed.remove(copy)
						#put node back on queue
						nodes.append(currMove)

			#close node
			closed.append(front)
			#sort queue

			
			nodes = sorted(nodes, key = lambda cost: cost.depth + cost.hn)







def manhattanDistance(puzzle):

	targetRow = 0
	targetCol = 0
	hn = 0

	for row in range(3):
		for col in range(3):

			val = puzzle.state[row][col]

	

			if(val == 1):
				targetRow = 0
				targetCol = 0
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 2):
				targetRow = 0
				targetCol = 1
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 3):
				targetRow = 0
				targetCol = 2
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 4):
				targetRow = 1
				targetCol = 0
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 5):
				targetRow = 1
				targetCol = 1
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 6):
				targetRow = 1
				targetCol = 2
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 7):
				targetRow = 2
				targetCol = 0
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))

			if(val == 8):
				targetRow = 2
				targetCol = 1
				if(row != targetRow or col != targetCol):
					hn += (abs(targetRow - row) + abs(targetCol - col))


	return hn


def misplacedTile(puzzle):
	
	hn = 0

	if puzzle.state[0][0] != 1:
		hn += 1
	if puzzle.state[0][1] != 2:
		hn += 1
	if puzzle.state[0][2] != 3:
		hn += 1
	if puzzle.state[1][0] != 4:
		hn += 1
	if puzzle.state[1][1] != 5:
		hn += 1
	if puzzle.state[1][2] != 6:
		hn += 1	
	if puzzle.state[2][0] != 7:
		hn += 1
	if puzzle.state[2][1] != 8:
		hn += 1

	return hn

def uniformCost(puzzle):
	
	hn = 0
	return hn


def solvePuzzle(puzzle, heuristicFunction):

	start = time.time()
	solutionPath, totalNodes, maxNodes = puzzle.solver(heuristicFunction)
	# test = puzzle.createMoves()
	# for i in test:
	# 	i.printState()
	end = time.time()
	solutionPath.reverse

	goalDepth = solutionPath[0].depth
	solutionPath[0].printSolutionTree()
	print "To solve this problem the search algorithm expanded a total of " + str(totalNodes) + " nodes."
	print "The maximum number of nodes in the queue at any one time was " + str(maxNodes) +"."
	print "The depth of the goal node was " + str(goalDepth) +"."

	elapsedTime = end - start
	print "Time took to solve: "+ str(elapsedTime) + " seconds. \n"


def whichAlgorithm(puzzle):
	print "Enter your choice of algorithm"
	print "1. Uniform Cost Search"
	print "2. A* with the Misplaced Tile heuristic."
	print "3. A* with Manhattan distance heuristic."


	while(True):
		choice = input()
		if(choice == 1):
			print "Solving with Uniform Cost Search: "
			solvePuzzle(puzzle, uniformCost)
			return

		if(choice == 2):
			print "Solving with Misplaced Tile Heuristic: "
			solvePuzzle(puzzle, misplacedTile)
			return

		if(choice == 3):
			print "Solving with Manhattan Distance Heuristic: "
			solvePuzzle(puzzle, manhattanDistance)
			return
		print "Please input 1, 2 or 3: "
		


def main():
	
	print "Welcome to the awesome 8-puzzle solver."
	puzzle = EightPuzzle()

	puzzle.setPuzzle()
	print "\n"
	whichAlgorithm(puzzle)




if __name__ == "__main__":
	main()