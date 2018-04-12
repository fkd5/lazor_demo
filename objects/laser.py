
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
        starting_position = position
        direction = direction

    # MORE
    # Difficulty 4

    def update(self, board, points)
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
        #         A list of laser objects.
        # '''

        # new position = old position + direction

        # if new position is at a point, tell point it has been hit

        # if new position is on edge of board, return []

        # check to see if the new position is hitting a block
        # either write if statements to check if block is located at closest (even, even) point in
        # direction of laser or pass to block object to check if block is hit and what side it hits

        # if laser hits opaque block, return []

        # if laser hits reflect block, new direction is dependent on what side of block is hit
        # if side parallel to y axis, new direction is (-x, y)
        # if side parallel to x axis, new direction is (x, -y)
        # return [laser(new position, new direction)]

        # if laser hits refract block, there are two new directions
        # one is the same direction as the reflect block
        # one is the same as the old direction
        # return [laser(new position, new direction), laser(new position, old direction)]
