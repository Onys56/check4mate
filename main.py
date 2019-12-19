import chess

board = chess.Board(input("Enter FEN code: "))
d = int(input("Enter depth: "))
color = board.turn #WHITE == True; BLACK = False

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

#DEBUG 8/5p2/5P1p/5PkN/6P1/4N1Rp/7P/6KQ w - - 0 2
#AND
#board.push(chess.Move.from_uci('a8h1'))
#board.push(chess.Move.from_uci('h4g5'))
#Q7/5p2/5P1p/5PPN/6Pk/4N1Rp/7P/6K1 w - - 0 1

def findCheckmates(depth, node):
    moves = board.legal_moves
    returnVal = False
    if moves:
        for myMove in moves:
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
    return returnVal


if board.is_checkmate():
    print("You are in a checkmate")
findCheckmates(d, head)
head.print()
