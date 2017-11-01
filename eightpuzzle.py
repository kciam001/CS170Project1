
import math
import random

goalState = [[1,2,3],
			 [4,5,6],
			 [7,8,0]]

class EightPuzzle:

	def __init__(self):
		self.state = [[1,2,3],
					  [4,0,6],
					  [7,5,8]]
		self.hn = 0
		self.depth = 0
		self.parent = None

	def printState(self):

		for i in range(len(self.state)):
			print self.state[i][0], self.state[i][1], self.state[i][2]

		print "\n"

		



	def copy(self):
		cpy = EightPuzzle()
		for i in range(3):
			cpy.state[i]= self.state[i][:]
		return cpy

	def printSolutionTree(self):
		if self.parent == None:
			print "Expanding state"
			self.printState()
		else:
			self.parent.printSolutionTree()
			print "The best state to expand with a g(n) = " + str(self.depth) +  " and h(n) = " + str(self.hn) + " is... "
			self.printState()






	def setPuzzle(self, whichPuzzle):
		if(whichPuzzle == 1):
			self.state = [[1,2,3],
						  [4,0,6],
						  [7,5,8]]
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
			#self.printState()
			#move.printState()
			#print cursor
			#print i 
			move.swap(cursor,i)
			#move.printState()
			move.depth = self.depth + 1
			move.parent = self
			moveList.append(move)

		#print moveList[0].depth
		return moveList



	def swap(self, x, y):
		xrow, xcol = x
		#print xrow
		#print xcol
		#print self.state[1][1]
		xtemp = self.state[xrow][xcol]
		yrow, ycol = y

		self.state[xrow][xcol] = self.state[yrow][ycol]
		self.state[yrow][ycol] = xtemp


		#recursive function to generate the solution path
	def pathToSolution(self, path):


		if self.parent == None:

			return path
		else:
			
			path.append(self)
			return self.parent.pathToSolution(path)

	def solvePuzzle(self, heuristicFunction):

		nodes = [self]
		closed = []
		maxDepth = 0
		maxNodesinQueue = -1
		totalExpanded = 0

		while len(nodes) > 0:

			
			front = nodes.pop(0)

			if maxNodesinQueue < len(nodes):
				maxNodesinQueue = len(nodes)


			#check if solved
			if (front.state == goalState):
				if len(closed) > 0:
					return front.pathToSolution([]), maxDepth, maxNodesinQueue
				else:
					return [front]

			#if it's not solved, see what moves we can make
			maxDepth += 1
			possibleMoves = front.createMoves()

			indexNodes = -1
			indexClosed = -1

			for currMove in possibleMoves:

				#check if we have seen this move
				count = 0

				for i in nodes:
					if currMove == i:
						indexNodes = count
					count += 1

				count = 0
				for i in closed:
					if currMove == i:
						indexClosed = count
					count += 1


				#setting h(n)

				hn = heuristicFunction(currMove)
				#total cost
				cost = hn + currMove.depth

				#if current move hasnt been seen yet
				if indexNodes == -1 and indexClosed == -1:
					currMove.hn = hn
					nodes.append(currMove)

				#else if node is in the queue

				elif indexNodes > -1:
					#make a copy
					copy = nodes[indexNodes]

					#check if this move is better
					if cost < copy.hn + copy.depth:
						#if it's better copy over the cost
						copy.hn =hn
						copy.parent = currMove.parent
						copy.depth = currMove.depth


				#else if node is has already been checked
				elif indexClosed > -1:
					#make a copy
					copy = closed[indexClosed]

					if cost < copy.hn + copy.depth:

						currMove.hn = hn
						closed.remove(copy)
						#put node back on queue
						nodes.append(currMove)

			#close node
			closed.append(currMove)
			#sort queue
			nodes = sorted(nodes, key = lambda p: p.hn + p.depth)

		#if we finish and theres no goal state found, return failure
		return [], 0, 0




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


			











def main():
	
	puzzle = EightPuzzle()
	print "Type \"1\" to use the default puzzle or \"2\" to enter your own: ",
	whichPuzzle = input()


	puzzle.setPuzzle(whichPuzzle)

	print "Original: "
	puzzle.printState()

	print "\n"
	solutionPath, numberOfMoves, maxNodes = puzzle.solvePuzzle(manhattanDistance)

	solutionPath.reverse

	solutionPath[0].printSolutionTree()

	#solutionPath[0].printState()
	#print "\n"
	#solutionPath[0].parent.printState()

	
	print "The maximum number of nodes in the queue at any one time was " + str(maxNodes) +"."
	print "The depth of the goal node was " + str(numberOfMoves) +"."

	#puzzle.printState()
	
	#a = 1, 1
	#b = 0, 1

	#puzzle.swap(a, b)
	#puzzle.createMoves()

	#puzzle.printState()



	#print "test"
	#puzzle.createMoves()





if __name__ == "__main__":
	main()