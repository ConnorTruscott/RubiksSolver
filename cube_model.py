"""Purpose: Define classes for cube - potentially other shaped puzzles down the line"""

from copy import deepcopy

class Cube:
    def __init__(self, corners_perm=None, corners_orient=None, edges_perm=None, edges_orient=None):
        """
        Corner indices 0..7 = URF, UFL, ULB, UBR, DFR, DLF, DBL, DRB
        Edge indices   0..11 = UR, UF, UL, UB, FR, FL, BL, BR, DR, DF, DL, DB
        """
        # corners_perm: list of 8 integers (0-7)
        # corners_orient: list of 8 integers (0-2)
        # edges_perm: list of 12 integers (0-11)
        # edges_orient: list of 12 integers (0-1)
        self.corners_perm = corners_perm if corners_perm is not None else list(range(8))
        self.corners_orient = corners_orient if corners_orient is not None else [0]*8
        self.edges_perm = edges_perm if edges_perm is not None else list(range(12))
        self.edges_orient = edges_orient if edges_orient is not None else [0]*12

    def copy(self):
        return deepcopy(self)

    def is_solved(self):
        return (self.corners_perm == list(range(8))
        and self.corners_orient == [0]*8
        and self.edges_perm == list(range(12))
        and self.edges_orient == [0]*12)

    def __repr__(self):
        return (f"Cube(cp={self.corners_perm}, co={self.corners_orient},\n"
                f"     ep={self.edges_perm}, eo={self.edges_orient})\n")
        