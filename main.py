import chess
import time
import configparser

opt = configparser.ConfigParser()
opt.read('options.ini')

class Node:
    """"Nodes for the tree that represents found checkmates"""
    def __init__(self, parent=None, move='Checkmates:'):
        self.parent = parent
        self.move = move
        self.children = []
        if parent:  parent.children.append(self)
    
    def kill(self):
        """Removes the node from its parent and deletes itself"""
        self.parent.children.remove(self)
        del self

    def print(self,j=-1, first=True):
        """Prints the possible checkmates when called on the head"""
        if first: 
            if len(self.children) > 0:
                print('Checkmates:')
            else:
                print('No checkmates found')
        else:
            k = j*' '
            t = j // 2 + 1
            c = 'w' if color != (j%2 == 1) else 'b' 
            print(f'{k}{t}{c}: {self.move}')
        ch = self.children
        if ch:
            for i in ch:
                i.print(j+1, False)
        

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

def findCheckmatesVerb(depth, node, verb):
    moves = board.legal_moves
    returnVal = False
    if moves:
        if verb:
            t = time.time()
            c = board.legal_moves.count()
            cl = 'w' if color else 'b' 
            k = 1
            o = d-depth+1
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
                if verb:
                    ec = board.legal_moves.count()
                    ecl = 'b' if color else 'w' 
                    ek = 1   
                for enemyMove in board.legal_moves:
                    if verb:
                        et = time.time()                     
                    board.push(enemyMove)
                    y = Node(x, enemyMove.uci())
                    if findCheckmatesVerb(depth - 1, y, int(opt['Verbose']['Depth']) > d-depth+1):
                        board.pop()
                    else:
                        canCheckmate = False
                        x.kill()
                        board.pop()
                        break
                    if verb:
                        print(f'{o*" "}{o}{ecl}: {ek}/{ec} took {round(time.time()-et,3)} seconds')
                        ek += 1
                if canCheckmate:
                    returnVal = True
                board.pop()
            else:
                board.pop()
            if verb:
                print(f'{d-depth+1}{cl}: {k}/{c} took {round(time.time()-t,3)} seconds')
                k += 1
    return returnVal

board = chess.Board(input("Enter FEN code: "))
d = int(input("Enter search depth: "))
color = board.turn #WHITE == True; BLACK = False

head = Node()

if board.legal_moves.count() == 0:
    print("This position has no valid moves")

t = time.time()
if int(opt['Verbose']['Enabled']):
    findCheckmatesVerb(d, head, int(opt['Verbose']['Depth']))
else:
    findCheckmates(d, head)
head.print()
print(f'The program took: {round(time.time()-t,3)} seconds')