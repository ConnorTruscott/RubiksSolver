"""Purpose: Define move tables and functions to apply moves"""

from cube_model import Cube
from copy import deepcopy

# Move definitions (cycle-based)

# Each move: corners and edges cycle (0-based indicies)
# Orientation change: +1 = clockwise, -1 = counterclockwise, 0 = no change
# Standard cubie numbering:
# Corners: URF=0, UFL=1, ULB=2, UBR=3, DFR=4, DLF=5, DBL=6, DRB=7
# Edges: UR=0, UF=1, UL=2, UB=3, FR=4, FL=5, BL=6, BR=7, DR=8, DF=9, DL=10, DB=11

# Corner cycles for each move (list of tuples)
corner_cycles = {
    "U": [(0,3,2,1)],
    "D": [(4,5,6,7)],
    "F": [(0,1,5,4)],
    "B": [(2,3,7,6)],
    "R": [(0,4,7,3)],
    "L": [(1,2,6,5)],
}

# Corner orientation change per move (0,1,2) added mod 3
corner_orient = {
    "U": [0]*8,
    "D": [0]*8,
    "F": [1,2,0,0,2,1,0,0],  # only corners in F face change orientation
    "B": [2,1,0,0,0,0,1,2],
    "R": [1,0,0,2,2,0,0,1],
    "L": [0,1,2,0,0,2,1,0],
}

# Edge cycles for each move
edge_cycles = {
    "U": [(0,3,2,1)],
    "D": [(8,9,10,11)],
    "F": [(1,5,9,4)],
    "B": [(3,6,11,7)],
    "R": [(0,4,8,7)],
    "L": [(2,5,10,6)],
}

# Edge orientation change (0=no flip, 1=flip)
edge_orient = {
    "U": [0]*12,
    "D": [0]*12,
    "F": [1 if i in [1,5,9,4] else 0 for i in range(12)],
    "B": [1 if i in [3,6,11,7] else 0 for i in range(12)],
    "R": [0]*12,
    "L": [0]*12,
}

# Helper Function: apply cycles
def apply_cycle(array, cycle):
    temp = array[cycle[-1]]
    for i in reversed(range(1, len(cycle))):
        array[cycle[i]] = array[cycle[i-1]]
    array[cycle[0]] = temp

def apply_move(cube: Cube, move: str) -> Cube:
    """
    Returns a new Cube obj after applying the given move.
    """
    new_cube = deepcopy(cube)

    base_move = move[0]
    times = 1
    if len(move) > 1:
        if move[1] == "'":
            times = 3 # counterclockwise
        elif move[1] == "2":
            times = 2 # 180 degrees
    
    for _ in range(times):
        # Corners
        for cycle in corner_cycles[base_move]:
            apply_cycle(new_cube.corners_perm, cycle)
        for i in range(8):
            new_cube.corners_orient[i] = (new_cube.corners_orient[i] + corner_orient[base_move][i]) % 3
        
        # Edges
        for cycle in edge_cycles[base_move]:
            apply_cycle(new_cube.edges_perm, cycle)
        for i in range(12):
            new_cube.edges_orient[i] = (new_cube.edges_orient[i] + edge_orient[base_move][i]) % 2
    return new_cube

def apply_algorithm(cube: Cube, alg: str) -> Cube:
    """
    Alg: string in standard notation
    """
    new_cube = deepcopy(cube)
    tokens = alg.strip().split()
    for move in tokens:
        new_cube = apply_move(new_cube, move)
    return new_cube