
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
		print self.state


	def copy(self):
		cpy = EightPuzzle()
		for i in range(3):
			cpy.state[i]= self.state[i][:]
		return cpy


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








def main():
	
	puzzle = EightPuzzle()
	print "Type \"1\" to use the default puzzle or \"2\" to enter your own: "
	whichPuzzle = input()

	puzzle.setPuzzle(whichPuzzle)

	#puzzle.printState()
	
	#a = 1, 1
	#b = 0, 1

	#puzzle.swap(a, b)
	puzzle.createMoves()

	#puzzle.printState()



	#print "test"
	#puzzle.createMoves()





if __name__ == "__main__":
	main()