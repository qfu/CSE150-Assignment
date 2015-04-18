#This is the first Program 
#
__author__ = 'z2tan@ucsd.edu,qfu@ucsd.edu,xul008@ucsd.edu'

#import Queue
import sys
import copy
import heapq

class A_node:

	def __init__  (self, board = None, location = None, preaction = None, level = 0 ,prestate = None):
		self.board = board
		self.location = location
		self.preaction = preaction
		self.prestate = prestate
		self.level = level
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

def find_num(board, num): 
	for y,row in enumerate(board): 
		for x,col in enumerate(row): 
			if board[y][x]==num: 
				return [y,x]
	return None

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


def getpriority(node):
	board = node.board
	num = 0
	priority = node.level
	for y,row in enumerate(board): 
		for x,col in enumerate(row): 
			if num == 0:
				continue

			location = find_num(board, num)
			if location is None:
				return None

			priority += max(y, location[0]) - min(y,location[0])
			priority += max(x, location[1]) - min(x,location[1])

			num += 1

	return priority

def A_search (nodes):
	visited =[nodes[0][2].board]
	count = 1
	while len(nodes) != 0:
		current_node = heapq.heappop(nodes)[2]

		if is_complete(current_node.board):
			return current_node

		while len(current_node.nextmove) != 0:
			action = current_node.nextmove.pop(0)
			old_location = current_node.location
			new_location = get_next_location(old_location, action)
			newboard = get_next_board(current_node.board, old_location, new_location)

			if newboard not in visited:
				visited.append(newboard)
				new_node = A_node(newboard, new_location, action, current_node.level+1, current_node)
				priority = getpriority(new_node)
				if priority is None:
					return None
				heapq.heappush(nodes, (priority, count, new_node))


	return None


def main():
	board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
	location = find_num(board, 0)
	if location is None:
		print 'UNSOLVABLE'
		return

	node = A_node(board, location, 'N', 0, None)

	priority = getpriority(node)

	counter = 0

	nodes = []

	heapq.heappush(nodes,(priority,counter,node))

	solution_node = None

	solution_node = A_search(nodes)


	if solution_node is None:
		print 'UNSOLVABLE'
		return

	if solution_node.prestate is None:
		print 'It is already solved. No moves needed'
		return

	s = ''

	while solution_node.preaction != 'N':
		s += solution_node.preaction
		solution_node = solution_node.prestate


	print s [::-1]
	return


if __name__ == '__main__':
	main()