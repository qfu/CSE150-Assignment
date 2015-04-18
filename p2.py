import inspect  
import heapq,random
"""
Data Structures
"""
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0
class Queue:
    def __init__(self):
        self.list = []
    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)
    def pop(self):
        return self.list.pop()
    def isEmpty(self):
        return len(self.list) == 0
class State:
    def __init__(self,board=None):
        self.board = board
        self.size = self.info(board)
    def __eq__(self,other):
        for y,row in enumerate(self.board):
            for x,col in enumerate(row):
                if self.board[y][x] != other[y][x]:
                    return False
        return True
    def __hash__(self):
        return hash(str(self.board))
    def is_goal(self):
        check = 0
        for row in self.board:
            for col in row:
                if col != check:
                    return False
                else:
                    check += 1	
        return True
    def info(self,board):
        for y,row in enumerate(board):
            for x,col in enumerate(row):
                x += 1
            y += 1
        return [y-1,x-1]
    def legalMove(self):
        moves = []
        row,col = self.find_zero(self.board)
        if(row > 0):
            moves.append('U')
        if(row < self.size[0]):
            moves.append('D')
        if(col > 0):
            moves.append('L')
        if(col < self.size[1]):
            moves.append('R')
        return moves
    def find_zero(self,board): 
        for y,row in enumerate(board): 
            for x,col in enumerate(row): 
                if board[y][x]==0: 
                    return [y,x]
    def result(self,move):
        [row, col] = self.find_zero(self.board) 
        if(move == 'U'):
            newrow = row - 1
            newcol = col
        elif(move == 'D'):
            newrow = row + 1
            newcol = col
        elif(move == 'L'):
            newrow = row
            newcol = col - 1
        elif(move == 'R'):
            newrow = row
            newcol = col + 1
        else:
            print "Illegal Move"
        import copy
        newboard = copy.deepcopy(self.board)
        newboard[row][col]= newboard[newrow][newcol]
        newboard[newrow][newcol]= 0 
        return newboard
    def getSuccessors(self):
        succ = []
        for a in self.legalMove():
            succ.append((self.result(a),a))
        return succ
class Node():
    def __init__(self,state=None,direction=None):
        self.state = state 
        self.direction = direction
    def getState(self):
        return self.state
    def getDirection(self):
        return self.direction
    def setState(self,state):
        self.state = state
    def setDirction(self,direction):
        self.direction = direction 

class search():
    @staticmethod
    def breadthFirstSearch(problem):
        toBeExpanded = Queue()
        toBeExpanded.push((problem,[]))
        alreadyExpanded = []
        while not toBeExpanded.isEmpty():
            current = toBeExpanded.pop()
            currentState = current[0]
            currentMoves = current[1]
            if(current in alreadyExpanded):
                continue
            alreadyExpanded.append(current)
            if current.is_goal():
                return currentMoves
            successors = current.getSuccessors()
            for successor, action in successors:
                toBeExpanded.push((successor,currentMoves+[action]))
        return []
def main():
    import sys
    board=[[int(n.strip()) for n in line.split(',')] for line in sys.stdin.readlines()]
    game = State(board)
    solution = search.breadthFirstSearch(game)
    if solution:
        print "SOLVABLE"
        print solution 
    else:
        print "UNSOLVABLE"
if __name__ == '__main__':
    main()
