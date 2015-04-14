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
    #print "new position before action", new_board
    x = new_board[new[0]][new[1]]
    new_board[original[0]][original[1]] = x
    new_board[new[0]][new[1]] = 0
    #print "new position after action", new_board
    return new_board
def find_zero(board): 
    for y,row in enumerate(board): 
        for x,col in enumerate(row): 
            if board[y][x]==0: 
                return [y,x]
def compare_state(b1,b2): 
    a = True
    for y,row in enumerate(b1): 
        for x,col in enumerate(row): 
            if b1[y][x] != b2[y][x]: 
                a = False
    a = True
    return a
def board_info(board): 
    for y,row in enumerate(board): 
        for x,col in enumerate(row): 
            x += 1
        y += 1
    return [y-1,x-1]
def action(position, board):
    #print "applying", position, "to", board
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
        #if compare_state(swap_tile(current,x,board),board) == False:
        final.append(x)
    #print final
    return final

'''def BFS(board,visited):
    closed = []
    open = [board]   
    while len(open) > 0:
        x = open.pop(0)
        print "before entering the second loop",x
        if is_complete(x):
            return x 
        if (x in closed) == False:
            print "the state ready for executing",x
            current = find_zero(x)
            moves = next_states(current,x)
            for move in moves:
                print move[2]
                y = action(move,x)
                print "successor state", y
                open.append(y)
                closed.append(x)
        visited += 1
    return None
    '''
def bfs(board):
    i =1
    visited = []
    myQueue = []
    parent = []
    path = []
    #visited.append(board)
    if is_complete(board):
        return True
    myQueue.append(board)
    while myQueue:
        i += 1
        currentState = myQueue.pop(0)
       # print currentState
        visited.append(currentState)
        if is_complete(currentState):
            backtrace(parent,board,currentState)
            return True
        moves = next_states(find_zero(currentState),currentState)
        for nextStates in moves:
            next = action(nextStates,currentState)
            if next not in visited:
                parent.append((currentState,next))
                myQueue.append(next)
       # print "the queue has",myQueue
    return False
def backtrace(parent,board,currentState):
    path = [currentState]
    while currentState != board:
        currentState = search_parent(parent,currentState)
        path.append(currentState)
    path.reverse()
    #print(path)
    moves(path)
def search_parent(parent,currentState):
    return[item for item in parent if item[1] == currentState][0][0]
def moves(path):
    s = ''
    i = 0
    while i + 1 < len(path):
        ancestor = path[i]
        child = path[i+1]
        if find_zero(ancestor)[0] - find_zero(child)[0] == 1:
            s +='U'
        if find_zero(child)[0] - find_zero(ancestor)[0] == 1:
            s +='D'
        if find_zero(ancestor)[1] - find_zero(child)[1] == 1:
            s +='L'
        if find_zero(child)[1] - find_zero(ancestor)[1] == 1:
            s +='R'
        i = i + 1
    print s

def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    visited = 0
    solution = bfs(board)
    if solution:
        print "SOLVABLE"
    else:
        print "UNSOLVABLE"
    #print(board_info(board))
if __name__ == '__main__':
    main()
