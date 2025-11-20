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

    # Corrected:
    "F": [(0,4,5,1)],
    "B": [(2,6,7,3)],
    "R": [(0,3,7,4)],
    "L": [(1,5,6,2)],
}


# Corner orientation change per move (0,1,2) added mod 3
corner_orient = {
    "U": [0,0,0,0,0,0,0,0],
    "D": [0,0,0,0,0,0,0,0],

    "F": [1,2,0,0,2,1,0,0],
    "B": [0,0,1,2,0,0,2,1],

    "R": [2,0,0,1,1,0,0,2],
    "L": [0,1,2,0,0,2,1,0],
}



# Edge cycles for each move
edge_cycles = {
    "U": [(0,3,2,1)],
    "D": [(8,9,10,11)],

    "F": [(1,4,9,5)],     # corrected
    "B": [(3,6,11,7)],    # corrected
    "R": [(0,7,8,4)],     # corrected
    "L": [(2,5,10,6)],    # corrected
}

# Edge orientation change (0=no flip, 1=flip)
edge_orient = {
    "U": [0]*12,
    "D": [0]*12,
    "F": [0,1,0,0,1,1,0,0,0,1,0,0],  # UF, FR, FL, DF positions
    "B": [0,0,0,1,0,0,1,1,0,0,0,1],  # UB, BL, BR, DB positions
    "R": [0]*12,
    "L": [0]*12,
}




def apply_move(cube, move):
    """
    Apply a single move (e.g., 'R', "R'", 'R2') to the cube.
    Returns a NEW cube object.
    """

    # --- Parse move ---
    face = move[0]
    suffix = move[1:] if len(move) > 1 else ""

    if suffix == "":
        times = 1
        reverse = False
    elif suffix == "'":
        times = 1
        reverse = True
    elif suffix == "2":
        times = 2
        reverse = False
    else:
        raise ValueError(f"Invalid move: {move}")

    new_cube = cube.copy()

    for _ in range(times):
        # snapshot current state
        old_cp = new_cube.corners_perm[:]
        old_co = new_cube.corners_orient[:]
        old_ep = new_cube.edges_perm[:]
        old_eo = new_cube.edges_orient[:]

        # start from old; we'll overwrite the moved positions
        new_cp = old_cp[:]
        new_co = old_co[:]
        new_ep = old_ep[:]
        new_eo = old_eo[:]

        # choose cycles
        if reverse:
            corner_cycles_to_use = [list(reversed(c)) for c in corner_cycles[face]]
            edge_cycles_to_use   = [list(reversed(c)) for c in edge_cycles[face]]
        else:
            corner_cycles_to_use = corner_cycles[face]
            edge_cycles_to_use   = edge_cycles[face]

        # --- corners ---
        for cycle in corner_cycles_to_use:
            L = len(cycle)
            for i in range(L):
                dst = cycle[i]
                src = cycle[(i - 1) % L]   # matches your apply_cycle direction

                # permute cubies
                new_cp[dst] = old_cp[src]

                # twist indexed by DESTINATION POSITION
                twist = corner_orient[face][dst]
                new_co[dst] = (old_co[src] + twist) % 3

        # --- edges ---
        for cycle in edge_cycles_to_use:
            L = len(cycle)
            for i in range(L):
                dst = cycle[i]
                src = cycle[(i - 1) % L]

                new_ep[dst] = old_ep[src]

                flip = edge_orient[face][dst]
                new_eo[dst] = (old_eo[src] + flip) % 2

        # commit this quarter turn
        new_cube.corners_perm = new_cp
        new_cube.corners_orient = new_co
        new_cube.edges_perm = new_ep
        new_cube.edges_orient = new_eo

    return new_cube




def apply_algorithm(cube: Cube, alg: str) -> Cube:
    """
    Alg: string in standard notation
    """
    new_cube = deepcopy(cube)
    tokens = alg.strip().split()
    print(tokens)
    for move in tokens:
        new_cube = apply_move(new_cube, move)
    print(new_cube)
    return new_cube