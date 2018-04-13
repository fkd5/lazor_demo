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
        self.blocks=[]
        self.emptyboard=[]
        self.points=[]
        self.lasers=[]

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

        #open and read lines of file
        file_read=open(fptr,"r") 
        lines=file_read.readlines()

        #find the start and end indeces for the board grid
        start=lines.index("GRID START\n")+1
        end=lines.index("GRID STOP\n")
        board_int=lines[start:end]

        #find the # of blocks in x and y dir
        y=len(board_int)
        x=(len(board_int[0])-2)//4+1
        #scale these #s up to include spaces for the edges of the blocks
        width=x*2+1
        length=y*2+1

        #create the empty board (w/ "None")
        board_int_upd=[ [ None for col in range( width ) ] for row in range( length ) ]

        #add the actual blocks to the new empty board matrix. keep "None" at the block boundaries. 
        for i in range(0, y):
            c=1
            for j in range(0,len(board_int[0])+2, 4):
                c+=2
                board_int_upd[2*i+1][(j+2)//2]=board_int[i][j]

        #parse thorugh the lines to find the beginning of the blocks paragraph, the lasers, and the points. 
        p=0 #initialize p and l to be zero to show that we have not yet found the point and laser lines. 
        l=0
        line_numb=0 #initialize the line number
        for line in lines:
            if "# Here we specify that we have" in line:
                blocks_start=line_numb
            if line[0] is "L" and l is 0:
                laser_start=line_numb
                l=1
            if line[0] is "P" and p is 0:
                point_start=line_numb
                p=1
            line_numb+=1

        #BLOCKS PARAGRAPH
        lin=blocks_start
        stop=0
        while not stop : #find the true start of the blocks
            if "#" not in lines[lin]:
                stop=1
                break
            lin+=1
        blocks_start=lin
        stop=0
        while not stop: #find the end of the blocks
            if "#" not in lines[lin]:
                lin+=1
            else:
                stop=1
                break
        blocks_end=lin-1

        blocks_values=[] #organize the blocks into a list of letters, whose qty = the # of that type of block
        for j in range(blocks_start, blocks_end):
            blocks_values.append(lines[j][0])
            blocks_values.append(lines[j][2])
        blocks_list=[]
        for index in range(1, len(blocks_values), 2):
            f=int(blocks_values[index])
            for index2 in range(1, f+1):
                blocks_list.append(blocks_values[index-1])

        #LASER
        lin=laser_start
        while lines[lin][0] is "L":
            lin+=1
        laser_end=lin

        #organize laser into list of objects
        lsr=[]
        for i in range(laser_start, laser_end):
            line=lines[i].split()
            position=(int(line[1]), int(line[2]))
            direction=(int(line[3]), int(line[4]))
            print(position)
            print(direction)
            #lsr.append(Laser(position, direction))

        #POINTS
        lin=point_start
        while (lines[lin][0] is "P") and lin<len(lines)-1:
            lin+=1
        point_end=lin

        #organize pts into list of objects
        pts=[]
        for i in range(point_start, point_end+1):
            position=(int(lines[i][2]), int(lines[i][4]))
            print(position)
            #pts.append(Point(position, 0))

        #close the file
        file_read.close()

        print(board_int_upd)
        print(blocks_list)

        #assign the important objects/lists to the game object 

        #self.blocks=blocks_list
        #self.emptyboard=board_int_upd
        #self.points=pts
        #self.lasers=lsr

        pass

    def generate_boards(self, empty_board):
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

            *boards* list of boards with all possible combinations of blocks on boards
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

        # Find available_space
        width = len(empty_board[0])
        height = len(empty_board)
        avail_space = 0
        for i in range(1, width):
            for j in range(1, height):
                if empty_board[i][j] == 'o':
                    avail_space = avail_space + 1
        self.available_space = avail_space

        # Get the different possible block positions.  Note, due to the function we're using, we
        # skip any instance of multiple "stars in bins".
        partitions = [
            p for p in get_partitions(len(self.blocks), self.available_space) if max(p) == 1
        ]

        # Now we have the partitions, we just need to make our boards
        boards = []

        # YOUR CODE HERE
        # We need to place different block types in all orders, so we need a list of possibilities
        block_permutations = list(set(list(itertools.permutations(self.blocks))))

        for permutation in block_permutations:
            for p in partitions:
                board = copy.deepcopy(empty_board)
                p_count = 0
                permutation_count = 0
                for i in range(1, width, 2):
                    for j in range(1, height, 2):
                        if empty_board[i][j] == 'o' and p[p_count] == 1:
                            board[i][j] = permutation[permutation_count]
                            permutation_count = permutation_count + 1
                        p_count = p_count + 1
                boards.append(board)

        return boards

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

    def save_board(self, board):
        '''
        Difficulty 2

        A function to save potential boards to file.  This is to be used when
        the solution is found, but can also be used for debugging.

        **Returns**

            None
        '''
        f= open("board_solution","w+")

        for i in range(1, len(self.emptyboard), 2):
            line=[]
            for j in range(1, len(self.emptyboard[0]), 2):
                line.append(self.emptyboard[i][j])
            f.write(line)

        f.close()
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
            #self.set_board(board)

            # MAYBE MORE CODE HERE?
            self.board = board
            current_lasers = copy.deepcopy(self.lasers)

            # LOOP THROUGH LASERS
            counter = 0
            for j, laser in enumerate(current_lasers):
              child_laser = laser.update(self.board, self.points)
              current_lasers = current_lasers + child_laser
              counter = counter + 1
              if counter > 100:
                pass

            # MAYBE MORE CODE HERE?

            # CHECKS HERE
            score = 0
            for point in self.points:
                if point.intersect = True:
                    score = score + 1

            if score == len(self.points):
                save_board(board)
                pass
            else:
                for point in self.points:
                    point.intersect = False

