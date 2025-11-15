"""Purpose: Convert 54 facelets into a cubie representation"""

from cube_model import Cube

# FACELET POSITIONS (using the standard Singmaster orientation)
#
# Each face has indicies 1..8:
# 0 1 2
# 3 4 5
# 6 7 8
#
# Face names:
# U, R, F, D, L, B

# For each corner: (facelet positions), (ordered color scheme)
corner_facelets = [
    (("U", 8), ("R", 0), ("F", 2)),  # URF
    (("U", 6), ("F", 0), ("L", 2)),  # UFL
    (("U", 0), ("L", 0), ("B", 2)),  # ULB
    (("U", 2), ("B", 0), ("R", 2)),  # UBR
    (("D", 2), ("F", 8), ("R", 6)),  # DFR
    (("D", 0), ("L", 8), ("F", 6)),  # DLF
    (("D", 6), ("B", 8), ("L", 6)),  # DBL
    (("D", 8), ("R", 8), ("B", 6)),  # DRB
]

corner_color_order = [
    ("U", "R", "F"),  # URF
    ("U", "F", "L"),  # UFL
    ("U", "L", "B"),  # ULB
    ("U", "B", "R"),  # UBR
    ("D", "F", "R"),  # DFR
    ("D", "L", "F"),  # DLF
    ("D", "B", "L"),  # DBL
    ("D", "R", "B"),  # DRB
]

# Edge data: (facelet locations), (color order)
edge_facelets = [
    (("U", 5), ("R", 1)),  # UR
    (("U", 7), ("F", 1)),  # UF
    (("U", 3), ("L", 1)),  # UL
    (("U", 1), ("B", 1)),  # UB
    (("F", 5), ("R", 3)),  # FR
    (("F", 3), ("L", 5)),  # FL
    (("B", 3), ("L", 3)),  # BL
    (("B", 5), ("R", 5)),  # BR
    (("D", 5), ("R", 7)),  # DR
    (("D", 7), ("F", 7)),  # DF
    (("D", 3), ("L", 7)),  # DL
    (("D", 1), ("B", 7)),  # DB
]

edge_color_order = [
    ("U", "R"),
    ("U", "F"),
    ("U", "L"),
    ("U", "B"),
    ("F", "R"),
    ("F", "L"),
    ("B", "L"),
    ("B", "R"),
    ("D", "R"),
    ("D", "F"),
    ("D", "L"),
    ("D", "B"),
]

# Helper Functions

def get_colour(facelets, face, index):
    return facelets[face][index]

#Conversion Logic

def facelets_to_cubie(facelets):
    """
    Convert a standard facelet structure gathered from input into a Cube object
    """

    cp = [-1]*8
    co = [0]*8
    ep = [-1]*12
    eo = [0]*12

    # Corners

    for pos in range(8):
        # read the three colours on the corner
        f1, i1 = corner_facelets[pos][0]
        f2, i2 = corner_facelets[pos][1]
        f3, i3 = corner_facelets[pos][2]
        colours = [
            get_colour(facelets, f1, i1),
            get_colour(facelets, f2, i2),
            get_colour(facelets, f3, i3),
        ]

        # Find the cubie that has these colours
        found = False
        for c_idx in range(8):
            scheme = corner_color_order[c_idx]
            cubie_colours = [facelets[f][4] for f in scheme]
            if set(colours) == set(cubie_colours):
                cp[pos] = c_idx
                
                # Determine Orientation:
                # Tells how many rotations are needed so that the sticker belonging to a position is there
                if colours[0] == cubie_colours[0]:
                    co[pos] = 0
                elif colours[1] == cubie_colours[0]:
                    co[pos] = 1
                else:
                    co[pos] = 2
                
                found = True
                break
        if not found:
            raise ValueError(f"Invalid corner at position {pos}, colours = {colours}")
    
    # Edges
    for pos in range(12):
        (f1, i1), (f2, i2) = edge_facelets[pos]
        colours = [
            get_colour(facelets, f1, i1),
            get_colour(facelets, f2, i2),
        ]

        # match to cubie index
        found = False
        for e_idx in range(12):
            fA, fB = edge_color_order[e_idx]
            cA = facelets[fA][4]
            cB = facelets[fB][4]

            if set(colours) == set([cA, cB]):
                ep[pos] = e_idx
                eo[pos] = 0 if colours[0] == cA else 1
                found = True
                break

        if not found:
            raise ValueError(f"Invalid edge at position {pos}, colours={colours}")

    # Final Cube
    return Cube(cp, co, ep, eo)
