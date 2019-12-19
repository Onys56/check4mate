import chess
import time

board = chess.Board(input("Enter FEN code: "))
d = int(input("Enter depth: "))
color = board.turn #WHITE == True; BLACK = False
verbDepth = 1

class Node:
    def __init__(self, parent=None, move=None):
        self.parent = parent
        self.move = move
        self.children = []
        if parent:  parent.children.append(self)
    
    def kill(self):
        """Deletes the node"""
        self.parent.children.remove(self)
        del self

    def print(self,j=0):
        k = j*' '
        print(k,j,': ',self.move,sep='')
        ch = self.children
        if ch:
            for i in ch:
                #print(k, end='',sep='')
                i.print(j+1)
        

head = Node()

def findCheckmates(depth, node):
    moves = board.legal_moves
    returnVal = False
    if moves:
        verb = verbDepth > (d-depth)
        if verb:
            t = time.time()
            c = board.legal_moves.count()
            k = 1
        for myMove in moves:
            if verb:
                t = time.time()
            board.push(myMove)
            if board.is_checkmate():
                Node(node, myMove.uci())
                board.pop()
                returnVal = True
            elif depth > 1 and board.legal_moves:
                x = Node(node, myMove.uci())
                canCheckmate = True
                for enemyMove in board.legal_moves:                        
                    board.push(enemyMove)
                    y = Node(x, enemyMove.uci())
                    if findCheckmates(depth - 1, y):
                        board.pop()
                    else:
                        canCheckmate = False
                        x.kill()
                        board.pop()
                        break
                if canCheckmate:
                    returnVal = True
                board.pop()
            else:
                board.pop()
            if verb:
                print(f'{d-depth+1}: {k}/{c} took {time.time()-t} seconds')
                k += 1
    return returnVal


if board.is_checkmate():
    print("You are in a checkmate")
t = time.time()
findCheckmates(d, head)
head.print()
print(time.time()-t, 'seconds')