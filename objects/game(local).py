import sys
import copy
import itertools
# import the Point, Block, and Laser objects

'''

import sys
sys.path.append("C:\\Users\\monikawiktorzak\\Desktop\\mymodules") #what location?? 

import point
import block
import laser

'''

class Game:
    '''
    The game grid.  Here we read in some user input, assign all our blocks,
    lasers, and points, determine all the possible different combinations
    of boards we could make, and then run through them all to try and find
    the winning one.
    '''

    def __init__(self, fptr):
        '''
        Difficulty 1

        Initialize our game.

        **Parameters**

            fptr: *str*
                The file name of the input board to solve.

        **Returns**

            game: *Game*
                This game object.
        '''
        self.fname = fptr

    # DO SOMETHING HERE SO WE CAN PRINT A REPRESENTATION OF GAME!

    ## QUESTION : What does this mean. 

    def read(self, fptr):
        '''
        Difficulty 3

        Some function that reads in a file, and generates the internal board.

        **Parameters**

            fptr: *str*
                The file name of the input board to solve.

        **Returns**

            None
        '''

        file_read=open(fptr,"r") 

        file_read=open(fptr,"r") 

        lines=file_read.readlines()

        print(lines)

        start=lines.index("GRID START\n")+1

        end=lines.index("GRID STOP\n")

        board_int=lines[start:end]
        print(board_int)
        y=len(board_int)
        x=len(board_int[0])
        f=((x)-2)//4+1

        for i in range(0, y):
            for j in range(0,x, 4):
                print(1)
                print(board_int[i][j])

        line_numb=0
        for line in lines:
            if "# Here we specify that we have" in line:
                line_blocks_start=line
                break
            line_numb+=1

        print(line_numb)

        while "#" in lines[line_numb]:
            line_numb+=1

        line_blocks_start=line_numb-1

        line_numb=line_blocks_start

        stop=0

        line_numb_start=line_numb

        while not stop :
            if "#" not in lines[line_numb_start]:
                stop=1
                break
            line_numb_start+=1

        print("start at")
        print(line_numb_start)

        line_numb_stop=line_numb_start+1

        while not stop: 
            if "#" in lines[line_numb_stop]:
                stop=1
                break
            line_numb_stop+=1

        print("stop at")

        print(line_numb_stop)

        file_read.close()

        blocks_values=[]
        for j in range(line_numb_start, line_numb_stop+1):
            blocks_values.append(lines[j][0])
            blocks_values.append(lines[j][2])

        print(blocks_values)


        pass

    def generate_boards(self):
        '''
        Difficulty 3

        A function to generate all possible board combinations with the
        available blocks.

        First get all possible combinations of blocks on the board (we'll call these boards)
          We know we have self.blocks, and N_blocks = len(self.blocks)
          We also know we have self.available_space
          So, essentially we have to find all the possible ways to put N_blocks into
          self.available_space
        This becomes the "stars and bars" problem; however, we have distinguishable "stars",
        and further we restrict our system so that only one thing can be put in each bin.

        **Returns**

            None
        '''

        def get_partitions(n, k):
            '''
            A robust way of getting all permutations.  Note, this is clearly not the fastest
            way about doing this though.

            **Reference**

             - http://stackoverflow.com/a/34690583
            '''
            for c in itertools.combinations(range(n + k - 1), k - 1):
                yield [b - a - 1 for a, b in zip((-1,) + c, c + (n + k - 1,))]

        # Get the different possible block positions.  Note, due to the function we're using, we
        # skip any instance of multiple "stars in bins".
        partitions = [
            p for p in get_partitions(len(self.blocks), self.available_space) if max(p) == 1
        ]

        # Now we have the partitions, we just need to make our boards
        boards = []

        # YOUR CODE HERE
        pass

    def set_board(self, board):
        '''
        Difficulty 2

        A function to assign a potential board so that it can be checked.

        **Parameters**

            board: *list, Block*
                A list of block positions.  Note, this list is filled with
                None, unless a block is at said position, then it is a
                Block object.

        **Returns**

            None
        '''
        # YOUR CODE HERE
        pass

    def save_board(self):
        '''
        Difficulty 2

        A function to save potential boards to file.  This is to be used when
        the solution is found, but can also be used for debugging.

        **Returns**

            None
        '''
        # YOUR CODE HERE
        pass

    def run(self):
        '''
        Difficulty 3

        The main code is here.  We call the generate_boards function, then we
        loop through, using set_board to assign a board, "play" the game,
        check if the board is the solution, if so save_board, if not then
        we loop.

        **Returns**

            None
        '''

        # Get all boards
        print("Generating all the boards..."),
        sys.stdout.flush()
        boards = self.generate_boards()
        print("Done")
        sys.stdout.flush()

        print("Playing boards...")
        sys.stdout.flush()
        # Loop through the boards, and "play" them
        for b_index, board in enumerate(boards):
            # Set board
            self.set_board(board)

            # MAYBE MORE CODE HERE?

            # LOOP THROUGH LASERS
            for j, laser in enumerate(current_lasers):
              child_laser = None
              child_laser = laser.update(self.board, self.points)

            # MAYBE MORE CODE HERE?

            # CHECKS HERE
