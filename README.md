# Check4mate
Checkmate search for selected depth. 

For a given chess position, finds if it's possible to make guaranteed checkmate. The program prints the tree of moves to perform the checkmate based on opponent's moves.

# Requirements
Using libraries: 
*  [python-chess](https://python-chess.readthedocs.io/en/latest/index.html)

# Usage
Start main.py in terminal and follow instructions in terminal.
1. Paste in your FEN

   [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) example: '5bk1/6p1/5PQ1/pp4Pp/2p4P/P2r4/1PK5/8 w - - 1 0'  
   Only the first part (board state) is required.  
   The second part (color to play) defaults to white.  
   If inputted, other parts are accounted for in the algorithm. Defaults to - - 1 0.  

2. Search depth

   Maximum number of fullmoves to reach the checkmate.  
   Recommended maximal depth: 3 generally takes 5s-60s on average PC.  
   (For better performance check out the experimental multi-thread branch TODO)

# Result
The result is printed as a tree of your checkmate moves and opponent's legal moves.

For example this checkmate in 3 position: 'r1b1k1nr/p5bp/p1pBq1p1/3pP1P1/N4Q2/8/PPP1N2P/R4RK1 w'

Prints this result:
```
1w: f4f8
 1b: e8d7
  2w: a4c5
  2w: f1f7
   2b: g8e7
    3w: a4c5
   2b: e6f7
    3w: a4c5
   2b: e6e7
    3w: a4c5
 1b: g7f8
  2w: f1f8
   2b: e8d7
    3w: a4c5
```

If you want to perform the checkmate you have to first play the f4f8 move. Then enemy has 2 legal moves (e8d7 and g7f8). If he then plays e8d7 you have a choice, you can play either a4c5 which is a checkmate or f1f7 which leads into checkmate after another move.

# Test data

You can build any position in [Lichess editor](https://lichess.org/editor). Keep in mind that the search is only guaranteed to work on valid positions.

Great checkmate collections on wtharvey.com:

[Checkmates in 2](http://wtharvey.com/m8n2.txt)

[Checkmates in 3](http://wtharvey.com/m8n3.txt)

[Checkmates in 4](http://wtharvey.com/m8n4.txt)