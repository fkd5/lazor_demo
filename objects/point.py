
class Point:
    '''
    The Point.  This object desribes the points for which we want the laser
    light to intersect.
    '''
    def __init__(self, pos):
        '''
        Difficulty 1

        DONT FORGET TO COMMENT!
        '''


        self.pos=pos


        pass

    # MORE
    # Difficulty 1

    def check.intersection(self, laser_p):

        #needs to be able to check the point position against the laser position. 
        #therefore - the laser needs to have a position
        if self.pos === laser_p:
            return 1
        else:
            return 0





