from objects.point import Point
from objects.block import Block

class Laser:
    '''
    The Laser.  We need to store both the starting position and direction of
    the laser.
    '''

    def __init__(self, position=None, direction=(0,0)):
        '''
        Difficulty 1

        DONT FORGET TO COMMENT!
        '''
        self.starting_position = position
        self.direction = direction

    # MORE
    # Difficulty 4

    def update(self, board, points):
        # '''
        # A function to propagate a laser across a board.  It will interact with the blocks on the
        # board.

        # **Warning:** Function does not protect against infinite loops!

        # **Parameters**

        #     board: *list, Block*
        #         A list of block positions.  Note, this list is filled with
        #         None, unless a block is at said position, then it is a
        #         Block object.
        #     points: *list, Point*
        #         A list of points.

        # **Returns**

        #     lasers: *list, Laser*
        #         A list of laser objects.  May be empty, contain 1 laser, or contain 2 lasers.
        # '''

        new_position = tuple(p + d for p, d in zip(self.starting_position, self.direction))

        # if new position is at a point, tell point it has been hit
        for point in points:
            if new_position == point.pos:
                point.intersected = True


        # if new position is on edge of board, return []
        width = len(empty_board[0])
        height = len(empty_board)
        if new_position[0] == 0 or new_position[0] == (width - 1) or new_position[1] == 0 or new_position[1] == (height - 1):
            return []

        # check to see if the new position is hitting a block
        # either write if statements to check if block is located at closest (odd, odd) point in
        # direction of laser or pass to block object to check if block is hit and what side it hits
        hit_block = None
        shift = (0, 0)

        # if x is odd
        if starting_position[0] % 2 == 1:
            if self.direction == (1, 1) or self.direction == (1, -1):
                shift = (1, 0)
            if self.direction == (-1, 1) or self.direction == (-1, -1):
                shift = (-1, 0)

        # if y is odd
        if starting_position[1] % 2 == 1:
            if self.direction == (1, 1) or self.direction == (-1, 1):
                shift = (0, 1)
            if self.direction == (1, -1) or self.direction == (-1, -1):
                shift = (0, -1)

        if shift == (0, 0):
            print('invalid laser position or direction')

        test_position = tuple(p + d for p, d in zip(new_position, shift))

        hit_block = board[test_position[0]][test_position[1]]

        # if laser does not hit a block, continue on
        if hit_block == 'o' or hit_block == 'x' or hit_block == None:
            return [laser(new_position, direction)]

        # if laser hits opaque block, return []
        if hit_block.type == 'B':
            return []

        # if laser hits reflect block, new direction is dependent on what side of block is hit
        if hit_block.type == 'A':
            # if side parallel to y axis, new direction is (-x, y)
            if starting_position[0] % 2 == 1:
                new_direction = (-direction[0], direction[1])
            # if side parallel to x axis, new direction is (x, -y)
            if starting_position[1] % 2 == 1:
                new_direction = (direction[0], -direction[1])
            return [laser(new_position, new_direction)]


        # if laser hits refract block, there are two new directions
        if hit_block.type == 'C':
            # one is the same direction as the reflect block
            if starting_position[0] % 2 == 1:
                new_direction = (-direction[0], direction[1])
            if starting_position[1] % 2 == 1:
                new_direction = (direction[0], -direction[1])
        # one is the same as the old direction
            return [laser(new_position, new_direction), laser(new_position, direction)]

        print('invalid entry in board')
