'''
The main call to the Lazor code.  This will load up the
game object, initialized by a board, and then run the game!
'''

import time
from objects.game import Game


def solve(fptr):
    # Start the game
    g = Game(fptr)
    # Print a representation of the board
    print(g)
    # Solve the board, and time how long it took.
    t0 = time.time()
    g.run()
    t1 = time.time()

    print("\n\n\tTime = %.2f" % (t1 - t0))


if __name__ == "__main__":
    #solve("boards/braid_5.input")
    # SOLUTION FOUND !!!  
    #solve("boards/diagonal_8.input")
    # solved
   # solve("boards/diagonal_9.input")
    # SOLUTION FOUND !!! 
    #solve("boards/mad_1.input")
    # solved
    #solve("boards/mad_7.input")
    # solution found
    solve("boards/showstopper_2.input")      #FIX THIS !!!! 
    # invalid starting file (fix error message)
    #solve("boards/tricky_1.input")
    # solution found
    #solve("boards/vertices_1.input")
    # solution found
    #solve("boards/vertices_2.input") #TRY THIS ONE AGAIN. 
    # FOUND SOLUTION
