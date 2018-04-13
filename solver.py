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
    solve("boards/mad_1.input")
