"""Beginner Method: Solve the white cross on D face (white = 'D')"""

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cube_model import Cube
from cube_moves import apply_move, apply_algorithm
from cube_to_facelet import cube_to_facelets
from facelet_to_cubie import edge_facelets, edge_colour_order

WHITE = "D"   # white is on D face
YELLOW = "U"  # yellow on U
GREEN  = "F"
BLUE   = "B"
ORANGE = "R"
RED    = "L"

TARGET_EDGES = {
    (WHITE, GREEN): 9,   # DF
    (WHITE, ORANGE): 8,  # DR
    (WHITE, BLUE): 11,   # DB
    (WHITE, RED): 10,    # DL
}

# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def get_facelets(cube):
    return cube_to_facelets(cube)

def find_edge(cube: Cube, c1, c2):
    """Return edge position index where colours c1 & c2 exist."""
    for e_idx, (fA, fB) in enumerate(edge_colour_order):
        if {fA, fB} == {c1, c2}:
            return cube.edges_perm.index(e_idx)
    raise ValueError("Edge not found")

def white_is_on_face(facelets, pos, white_face="D"):
    """Check if white sticker is visible on a specific face for this edge pos."""
    (f1, i1), (f2, i2) = edge_facelets[pos]
    return facelets[f1][i1] == 'W' or facelets[f2][i2] == 'W'

def is_white_on_U(cube, pos):
    faces = cube_to_facelets(cube)
    (f1, i1), (f2, i2) = edge_facelets[pos]
    return faces[f1][i1] == 'Y' or faces[f2][i2] == 'Y'

# ------------------------------------------------------------
# INSERTION (Beginner)
# ------------------------------------------------------------

def insert_direct(cube, side):
    """Do the F F, R R, B B, L L insertion."""
    move = {
        "F": "F F",
        "R": "R R",
        "B": "B B",
        "L": "L L",
    }[side]
    return apply_algorithm(cube, move), move

def flip_edge(cube):
    """Beginner method flipper."""
    alg = "F R U R' U' F'"
    return apply_algorithm(cube, alg), alg


# ------------------------------------------------------------
# MAIN SOLVER
# ------------------------------------------------------------

def solve_cross_beginner(cube: Cube):
    moves = []

    for (white, side) in [(WHITE, GREEN),
                          (WHITE, ORANGE),
                          (WHITE, BLUE),
                          (WHITE, RED)]:

        target_pos = TARGET_EDGES[(white, side)]

        while True:
            facelets = cube_to_facelets(cube)
            epos = find_edge(cube, white, side)

            # Already solved?
            if epos == target_pos:
                break

            # CASE A — In U layer
            if epos in (0,1,2,3):
                # Step 1: rotate U until side sticker matches side face centre
                for _ in range(4):
                    facelets = cube_to_facelets(cube)
                    side_face_centre = facelets[side][4]
                    (f1, i1), (f2, i2) = edge_facelets[epos]

                    side_colour_here = \
                        facelets[f1][i1] if facelets[f1][i1] != 'W' else facelets[f2][i2]

                    if side_colour_here == side_face_centre:
                        break

                    cube = apply_move(cube, "U")
                    moves.append("U")
                    epos = find_edge(cube, white, side)

                # Step 2: drop it in
                cube, m = insert_direct(cube, side)
                moves.append(m)
                break

            # CASE B — In middle layer
            elif epos in (4,5,6,7):
                # Eject to U layer with a trigger
                eject = {
                    4: "F U F'",
                    5: "L U L'",
                    6: "B U B'",
                    7: "R U R'",
                }[epos]
                cube = apply_algorithm(cube, eject)
                moves.append(eject)

            # CASE C — In D layer but flipped
            elif epos in (8,9,10,11):
                if not white_is_on_face(facelets, epos, WHITE):
                    cube, m = flip_edge(cube)
                    moves.append(m)
                else:
                    # Rotate D until aligned
                    for _ in range(4):
                        facelets = cube_to_facelets(cube)
                        if facelets[side][7] == facelets[side][4]:
                            break
                        cube = apply_move(cube, "D")
                        moves.append("D")
                    # Insert
                    cube, m = insert_direct(cube, side)
                    moves.append(m)
                    break

    return cube, moves
