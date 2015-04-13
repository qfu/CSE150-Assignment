#This is the second  Program 
import copy 
import time
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
def swap_tile(original, new, board):

    new_board = copy.deepcopy(board)
    print "new position before action", new_board
    x = new_board[new[0]][new[1]]
    new_board[original[0]][original[1]] = x
    new_board[new[0]][new[1]] = 0
    print "new position after action", new_board
    return new_board
def find_zero(board): 
    for y,row in enumerate(board): 
        for x,col in enumerate(row): 
            if board[y][x]==0: 
                return [y,x]
def board_info(board): 
    for y,row in enumerate(board): 
        for x,col in enumerate(row): 
            x += 1
        y += 1
    return [y-1,x-1]
def action(position, board):
    print "applying", position, "to", board
    x = position[0]
    y = position[1]
    z = position[2]
    if z == None:
        return board
    elif z == 'up':
        return swap_tile([x + 1, y], [x, y],board)
    elif z == 'down':
        return swap_tile([x - 1, y], [x, y], board)
    elif z == 'left':
        return swap_tile([x, y + 1], [x, y], board)
    elif z == 'right':
        return swap_tile([x, y - 1], [x, y], board)

def next_states(current,board): 
    row = current[0]
    column = current[1]
    l = [((row - 1), column, 'up'), #Move Up
          ((row + 1), column, 'down'), #Move Down
          (row, (column - 1), 'left'), #Move Left
          (row, (column + 1), 'right')] #Move Right

    final = []
    for x in l:
        tempx = x[0]
        tempy = x[1]
        if tempx >board_info(board)[0] or tempy > board_info(board)[1]:
            continue
        if tempx < 0 or tempy < 0:
            continue
        if swap_tile(find_zero(board),x,board) != board:
            final.append(x)
    return final

def BFS(board,visited):
    closed = []
    open = [board]   
    return_list=[]
    direction = []
    return_list2=[]
    counter = 0
    index = 0
    while len(open) > 0:
        x = open.pop(0)
        if len(return_list) >0:
            direction.append(return_list.pop(0))
        print "pop", x
        if is_complete(x):
            for i in range(0,index+1):
                return_list2.append(direction.pop(0))
            return return_list2
        print "not goal"
        if (x in closed) == False:
            print "not visited"
            current = find_zero(x)
            moves = next_states(current,board)
            print "legal moves", moves
            for move in moves:
                print move[2]
                y = action(move,x)
                index += step(y)    
                return_list.append(move[2])
                print "successor state", y
                open.append(y)
                closed.append(x)
        visited += 1
    return None
def step(board):
    if is_complete(board):
        return 1
    else:
        return 0
        
def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    print(is_complete(board))
    print(find_zero(board))
    print board
    visited = 0
    solution = BFS(board,visited)
    if solution:
        print "SOLVABLE"
        print solution
    else:
        print "UNSOLVABLE"
    print(board_info(board))
if __name__ == '__main__':
    main()
