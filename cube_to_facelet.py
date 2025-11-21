from cube_model import Cube
from facelet_to_cubie import (
    corner_facelets,
    corner_color_order,
    edge_facelets,
    edge_colour_order,
)



CENTRE_COLOURS = {
    "U": "Y",  # Up is now Yellow
    "D": "W",  # Down is White
    "F": "G",  # Front stays Green
    "B": "B",  # Back stays Blue
    "L": "R",  # Left is Red
    "R": "O",  # Right is Orange
}

def cube_to_facelets(cube: Cube) -> dict[str, list[str]]:
    faces = {f: ["?"] * 9 for f in CENTRE_COLOURS.keys()}

    for f, col_c in CENTRE_COLOURS.items():
        faces[f][4] = col_c

    # Corners
    for pos in range(8):
        cubie = cube.corners_perm[pos]
        ori = cube.corners_orient[pos] % 3

        canon_faces = corner_color_order[cubie]
        (f1, i1), (f2, i2), (f3, i3) = corner_facelets[pos]
        face_triplet = [(f1, i1), (f2, i2), (f3, i3)]

        for k, (face, idx) in enumerate(face_triplet):
            logical_index = (k - ori) % 3
            logical_face = canon_faces[logical_index]
            faces[face][idx] = CENTRE_COLOURS[logical_face]

    # Edges
    for pos in range(12):
        cubie = cube.edges_perm[pos]
        ori = cube.edges_orient[pos] % 2

        fA, fB = edge_colour_order[cubie]
        cA, cB = CENTRE_COLOURS[fA], CENTRE_COLOURS[fB]

        (f1, i1), (f2, i2) = edge_facelets[pos]

        if ori == 0:
            faces[f1][i1] = cA
            faces[f2][i2] = cB
        else:
            faces[f1][i1] = cB
            faces[f2][i2] = cA

    return faces