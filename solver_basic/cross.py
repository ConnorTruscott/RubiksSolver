"""
Beginner-method white cross solver (D = white).
Orientation:
    U = yellow
    D = white
    F = green
    B = blue
    R = orange
    L = red
"""

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cube_model import Cube
from cube_moves import apply_move, apply_algorithm
from cube_to_facelet import cube_to_facelets
from facelet_to_cubie import edge_facelets


# ------------------------------------------------------------
# Colour constants (your orientation)
# ------------------------------------------------------------
WHITE = "D"      # white face = Down
GREEN = "F"
BLUE  = "B"
ORANGE = "R"
RED = "L"
YELLOW = "U"

# ------------------------------------------------------------
# White edge cubie indexes in your cubie model
# ------------------------------------------------------------
# edges: UR=0, UF=1, UL=2, UB=3, FR=4, FL=5, BL=6, BR=7, DR=8, DF=9, DL=10, DB=11
WHITE_EDGES = {
    (WHITE, GREEN): 9,    # DF
    (WHITE, ORANGE): 8,   # DR
    (WHITE, RED): 10,     # DL
    (WHITE, BLUE): 11,    # DB
}

# A normalised version so (white,side) OR (side,white) both work
WHITE_EDGE_LOOKUP = {}
for key, v in WHITE_EDGES.items():
    WHITE_EDGE_LOOKUP[key] = v
    WHITE_EDGE_LOOKUP[(key[1], key[0])] = v

# ------------------------------------------------------------
# Edge colour order from your facelet system
# ------------------------------------------------------------
edge_colour_order = [
    ("U", "R"),  # 0
    ("U", "F"),  # 1
    ("U", "L"),  # 2
    ("U", "B"),  # 3
    ("F", "R"),  # 4
    ("F", "L"),  # 5
    ("B", "L"),  # 6
    ("B", "R"),  # 7
    ("D", "R"),  # 8
    ("D", "F"),  # 9
    ("D", "L"),  # 10
    ("D", "B"),  # 11
]

# ------------------------------------------------------------
# Helper: find where an edge cubie with colours (c1,c2) is located
# ------------------------------------------------------------
def find_edge_position(cube: Cube, c1: str, c2: str) -> int:
    """
    Returns the POSITION (0..11) of the edge cubie with colours c1,c2.
    Uses correct unordered pair matching.
    """
    for cubie_idx, (fA, fB) in enumerate(edge_colour_order):
        if (fA == c1 and fB == c2) or (fA == c2 and fB == c1):
            return cube.edges_perm.index(cubie_idx)

    raise ValueError(f"Edge with colours {c1},{c2} not found!")

# ------------------------------------------------------------
# Helper: check if a white edge at a D-layer position is oriented
# ------------------------------------------------------------
def edge_is_oriented_white_down(cube: Cube, pos: int) -> bool:
    """
    True if the edge in D-layer position POS has the white sticker
    on the D face.
    """
    faces = cube_to_facelets(cube)
    (f1, i1), (f2, i2) = edge_facelets[pos]

    oriented = False

    if f1 == "D" and faces[f1][i1] == "W":
        oriented = True
    if f2 == "D" and faces[f2][i2] == "W":
        oriented = True

    return oriented


# ------------------------------------------------------------
# Check if a single edge is solved
# ------------------------------------------------------------
def cross_edge_is_solved(cube: Cube, side_face: str) -> bool:
    """
    side_face: F/R/B/L (green/orange/blue/red).

    A cross edge is solved if:
    - the correct cubie for (D, side_face) is in the correct D-layer slot
    - and the sticker on the D face is actually white.
    """
    target_cubie = WHITE_EDGE_LOOKUP[(WHITE, side_face)]
    target_pos = WHITE_EDGES[(WHITE, side_face)]

    if cube.edges_perm[target_pos] != target_cubie:
        return False

    faces = cube_to_facelets(cube)
    (f1, i1), (f2, i2) = edge_facelets[target_pos]

    d_is_white = False
    if f1 == "D" and faces[f1][i1] == "W":
        d_is_white = True
    if f2 == "D" and faces[f2][i2] == "W":
        d_is_white = True

    return d_is_white


# ------------------------------------------------------------
# Check whole cross
# ------------------------------------------------------------
def cross_is_solved(cube: Cube) -> bool:
    return (
        cross_edge_is_solved(cube, GREEN) and
        cross_edge_is_solved(cube, ORANGE) and
        cross_edge_is_solved(cube, BLUE) and
        cross_edge_is_solved(cube, RED)
    )

# ------------------------------------------------------------
# Insert from U layer (beginner drop algorithm)
# ------------------------------------------------------------
DROP = {
    GREEN:  "F2",   # insert UF -> DF
    ORANGE: "R2",   # insert UR -> DR
    BLUE:   "B2",   # insert UB -> DB
    RED:    "L2",   # insert UL -> DL
}

# ------------------------------------------------------------
# Kick middle-layer white edges into U layer
# ------------------------------------------------------------
KICK = {
    4: "F' U' F",  # FR → kick up
    5: "L",  # FL → kick up
    6: "L",  # BL → kick up
    7: "R' U' R",  # BR → kick up
}

# ------------------------------------------------------------
# Main solver
# ------------------------------------------------------------
def solve_cross_beginner(cube: Cube):
    moves = []
    working = cube

    for side in (GREEN, ORANGE, BLUE, RED):
        target_cubie = WHITE_EDGE_LOOKUP[(WHITE, side)]
        target_pos = WHITE_EDGES[(WHITE, side)]

        # If already solved → continue
        if cross_edge_is_solved(working, side):
            continue

        # Find current position of this edge
        pos = working.edges_perm.index(target_cubie)

        # ----------------------------------------------------
        # CASE 1: Edge in U layer (0,1,2,3)
        # ----------------------------------------------------
        if pos in (0,1,2,3):
            # Align U-layer so side colour faces correct centre
            for _ in range(4):
                faces = cube_to_facelets(working)
                # The U-edge facelet index is always 1
                if faces[side][1] == faces[side][4]:
                    break
                working = apply_move(working, "U")
                moves.append("U")

            # Drop it
            alg = DROP[side]
            working = apply_algorithm(working, alg)
            moves.append(alg)

        # ----------------------------------------------------
        # CASE 2: Edge in middle layer (4..7)
        # ----------------------------------------------------
        elif pos in (4,5,6,7):
            alg = KICK[pos]
            working = apply_algorithm(working, alg)
            moves.append(alg)

        # ----------------------------------------------------
        # CASE 3: Edge in D layer (8..11)
        # ----------------------------------------------------
        elif pos in (8,9,10,11):
            # If flipped → use a simple flip algorithm: F R U R' U' F'
            if not edge_is_oriented_white_down(working, pos):
                flip_alg = "F R U R' U' F'"
                working = apply_algorithm(working, flip_alg)
                moves.append(flip_alg)

            # rotate D layer until aligned
            for _ in range(4):
                faces = cube_to_facelets(working)
                # D-layer edge always uses index 7 on the side face
                if faces[side][7] == faces[side][4]:
                    break
                working = apply_move(working, "D")
                moves.append("D")

            # finally drop
            alg = DROP[side]
            working = apply_algorithm(working, alg)
            moves.append(alg)

    # Final assertion (debug)
    #assert cross_is_solved(working), "White cross not solved!"

    return working, moves
