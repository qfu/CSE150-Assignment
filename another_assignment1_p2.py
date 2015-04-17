#This is the first Program 
#
__author__ = 'z2tan@ucsd.edu,qfu@ucsd.edu'

#import Queue
import sys
import copy

class BFS_node:

	def __init__  (self, board = None, location = None, preaction = None, prestate = None):
		self.board = board
		self.location = location
		self.preaction = preaction
		self.prestate = prestate
		self.nextmove = self.getmoves(board, location, preaction)


	def getmoves (self, board, location, preaction):
		rowMax = len(board)
		colMax = len(board[0])

		row = location [0]
		col = location [1]

		#nextmoves = Queue.Queue()
		nextmoves = []

		if row !=0 and preaction != 'D':
			nextmoves.append('U')

		if row != rowMax - 1 and preaction != 'U':
			nextmoves.append('D')

		if col != 0 and preaction != 'R':
			nextmoves.append('L')

		if col != colMax - 1 and preaction != 'L':
			nextmoves.append('R')

		return nextmoves

def find_zero(board): 
	for y,row in enumerate(board): 
		for x,col in enumerate(row): 
			if board[y][x]==0: 
				return [y,x]
	return [-1,-1]

def get_next_location (location, action):
	if action == 'U':
		return [location[0] - 1, location[1] ]

	if action == 'D':
		return [location[0] + 1, location[1] ]

	if action == 'L':
		return [location[0], location[1] - 1 ]

	if action == 'R':
		return [location[0], location[1] + 1]

def get_next_board (board, old_location, new_location):
	newboard = copy.deepcopy(board)

	newboard [old_location[0]] [old_location[1]] = newboard[new_location[0]] [new_location [1]]
	newboard[new_location[0]] [new_location [1]] = 0

	return newboard

def is_complete(board):
	# your code here
	check = 0
	for row in board:
		for col in row:
			if col != check:
				return False
			else:
				check += 1	
	return True


def BFS_search (nodes, visited):

	while len(nodes) != 0:
		current_node = nodes.pop(0)
		while len(current_node.nextmove) != 0:
			nextmove = current_node.nextmove.pop(0)
			old_location = current_node.location
			new_location = get_next_location(old_location, nextmove)
			newboard = get_next_board(current_node.board, old_location, new_location)

			if newboard not in visited:
				visited.append(newboard)		

			new_node = BFS_node(newboard, new_location, nextmove, current_node)

			# check if it is solution
			if is_complete(newboard):
				return new_node

			nodes.append(new_node)

	return None


def main():
	board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
	location = find_zero(board)
	if location[0] == -1:
		print 'UNSOLVABLE'
		return

	if is_complete(board) == True:
		print 'It is already solved! No moves needed!'
		return

	nodes = []

	node = BFS_node(board, location, 'N', None)

	nodes.append(node)

	visited = [board]

	solution_node = BFS_search(nodes, visited)

	if solution_node is None:
		print 'UNSOLVABLE'
		return

	s = ''

	while solution_node.preaction != 'N':
		s += solution_node.preaction
		solution_node = solution_node.prestate


	print s [::-1]
	return


if __name__ == '__main__':
	main()