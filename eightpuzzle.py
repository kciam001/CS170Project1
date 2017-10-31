
import random
import math

goalState = [[1,2,3],
			 [4,5,6],
			 [7,8,0]]

class EightPuzzle:

	def __init__(self):
		# heuristic value
		self.hval = 0
		# search depth of current instance
		self.depth = 0
		# parent node in search path
		self.parent = None
		self.state = []

	def __str__(self):
		prnt = ''
		for row in range(3):
			prnt += ' '.join(map(str, self.state[row]))
			prnt += '\r\n'
		return prnt

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
			
		#print self.state
		





def main():

	puzzle = EightPuzzle()
	print "Type \"1\" to use the default puzzle or \"2\" to enter your own: "
	whichPuzzle = input()

	puzzle.setPuzzle(whichPuzzle)

	print puzzle




if __name__ == "__main__":
	main()