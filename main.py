import chess
import time

# Fullmove depth of progess prints
# Possible values: 
#   integer from 0 to infinity
# Recommended values: 
#   0 or 1 for searches up to depth 3
#   1 or 2 for searchers of depth 4+
progressPrints = 1


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
    """
    Finds all possible checkmates and makes a tree from the results with the 

    Returns True if checkmate is found otherwise returns False
    """
    # This function works recursively every iteration checks all fullmoves (my move + enemy move)
    # and calls itself with lower depth
    moves = board.legal_moves   # generates my legal moves
    returnVal = False           
    if moves:                   
        for myMove in moves:
            board.push(myMove)  # play the move
            if board.is_checkmate():    # if its checkmate
                Node(node, myMove.uci())    # add to results
                board.pop()                 # undo the move
                returnVal = True
            elif depth > 1 and board.legal_moves:   
                # if position after my move isn't checkmate and we want to find checkmates of depth 2+
                # we need to go through ALL enemy's legal moves
                # and have a checkmate for all of them
                # otherwise there is a way for the enemy to dodge the checkmate
                myMoveNode = Node(node, myMove.uci())
                enemyCantDodge = True
                for enemyMove in board.legal_moves:                   
                    board.push(enemyMove)
                    enemyMoveNode = Node(myMoveNode, enemyMove.uci())
                    if findCheckmates(depth - 1, enemyMoveNode): 
                        # recursively calls itself after a fullmove
                        # if it returns true that means we can make a checkmate with this particular enemy move
                        board.pop()
                    else:
                        # else if it returns false then there is a enemy move that avoids checkmate
                        # we can break out of the loop and erase my move from the results
                        enemyCantDodge = False
                        myMoveNode.kill()
                        board.pop()
                        break
                if enemyCantDodge:
                    returnVal = True
                board.pop()
            else:
                board.pop()
    return returnVal

# I decided to make this a separate function because it makes the function less understandable 
def findCheckmatesVerb(depth, node):
    """
    Same function as findCheckmates but with progress prints
    """
    moves = board.legal_moves
    returnVal = False
    if moves:
        c = board.legal_moves.count()
        cl = 'w' if color else 'b' 
        k = 1
        o = d-depth+1
        for myMove in moves:
            t = time.time()
            board.push(myMove)
            if board.is_checkmate():
                Node(node, myMove.uci())
                board.pop()
                returnVal = True
            elif depth > 1 and board.legal_moves:
                x = Node(node, myMove.uci())
                canCheckmate = True
                ec = board.legal_moves.count()
                ecl = 'b' if color else 'w' 
                ek = 1   
                for enemyMove in board.legal_moves:
                    et = time.time()                     
                    board.push(enemyMove)
                    y = Node(x, enemyMove.uci())
                    if progressPrints > d-depth+1:
                        canCheckmateAll = findCheckmatesVerb(depth - 1, y)
                    else:
                        canCheckmateAll = findCheckmates(depth - 1, y)
                    if canCheckmateAll:
                        board.pop()
                    else:
                        canCheckmate = False
                        x.kill()
                        board.pop()
                        break
                    print(f'{o*" "}{o}{ecl}: {ek}/{ec} took {round(time.time()-et,3)} seconds')
                    ek += 1
                if canCheckmate:
                    returnVal = True
                board.pop()
            else:
                board.pop()
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
if progressPrints:
    findCheckmatesVerb(d, head)
else:
    findCheckmates(d, head)
head.print()
print(f'The program took: {round(time.time()-t,3)} seconds')