"""Purpose: Convert 54 facelets into a cubie representation"""

class Cube:
    def __init__(self, corners_perm=None, corners_orient=None, edges_perm=None, edges_orient=None):
        # corners_perm: list of 8 integers (0-7)
        # corners_orient: list of 8 integers (0-2)
        # edges_perm: list of 12 integers (0-11)
        # edges_orient: list of 12 integers (0-1)
        self.corners_perm = corners_perm or list(range(8))
        self.corners_orient = corners_orient or [0]*8
        self.edges_orient = edges_perm or list(range(12))
        self.edges_orient = edges_orient or [0]*12

def facelets_to_cubie(facelets):
    """
    TODO: Implement mapping from 6x9 facelets to Cube internal representation
    """
    cube = Cube()
    #placeholder
    return cube