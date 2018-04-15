
class Point:
    '''
    The Point.  This object desribes the points for which we want the laser
    light to intersect.  Contains information about position and whether the
    point has been hit.
    '''
    def __init__(self, pos, int):
        '''
        Difficulty 1

        '''

        # Takes (x,y) input and saves as (row, column) position
        self.pos=(pos[1], pos[0])

        #intersected can either be true or false 
        #"true" means that the point has been intersected
        #"false" means that the point has not been intersected
        self.intersected=int
        pass






