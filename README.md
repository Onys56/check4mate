# Check4mate
Checkmate search for a selected depth. 

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

# Options
Edit options.ini to change
* Verbose

  Progress prints
  * Enable

  Should the program print progress: 1 or 0
  * Depth  

   How many fullmoves down should the program print:  >= 0

   * Time

   Should the program print the time it took to evaluate moves: 1 or 0

