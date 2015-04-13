#This is the first Program 
#
__author__ = 'z2tan@ucsd.edu,qfu@ucsd.edu'
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
def main():
	import sys
	board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
	print(is_complete(board))
	print board
if __name__ == '__main__':
	main()
