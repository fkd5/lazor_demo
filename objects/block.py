
class Block:
    '''
    A generic block for lazor.  We make this extendable so that it can be
    defined as either:

        (a) Reflecting block - Only reflects the laser
        (b) Opaque block - Absorbs the laser
        (c) See-Through block - Both reflects and lets light pass
    '''
    def __init__(self, t='o'):
        '''
        Difficulty 1

        DONT FORGET TO COMMENT!
        '''
        assert t is in ['A', 'B', 'C'], "not an available block type"
        self.type = t
