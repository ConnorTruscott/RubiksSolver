# ascii_cube.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cube_model import Cube
from facelet_to_cubie import (
    corner_facelets,
    corner_color_order,
    edge_facelets,
    edge_colour_order,
)
from cube_to_facelet import cube_to_facelets

USE_COLOR = True

COLOR_MAP = {
    "W": "\033[97m",
    "Y": "\033[93m",
    "G": "\033[92m",
    "B": "\033[94m",
    "R": "\033[91m",
    "O": "\033[38;5;208m",
    "?": "\033[90m",
}

RESET = "\033[0m"


def col(ch: str) -> str:
    if not USE_COLOR:
        return ch
    return COLOR_MAP.get(ch, "") + ch + RESET


FACE_DISPLAY_MAP = {
    "U": list(range(9)),
    "D": list(range(9)),
    "F": list(range(9)),
    "B": list(range(9)),
    "L": list(range(9)),
    "R": list(range(9)),
}

# FACE_DISPLAY_MAP = {
#     "U": [0,1,2, 3,4,5, 6,7,8],
#     "D": [0,7,2, 3,4,5, 6,1,8],
#     "F": [0,1,2, 3,4,5, 6,7,8],
#     "B": [0,1,2, 5,4,3, 6,7,8],
#     "L": [0,1,2, 3,4,5, 6,7,8],
#     "R": [0,1,2, 3,4,5, 6,7,8],
# }


def _remap_face_for_display(name: str, face: list[str]) -> list[str]:
    idxmap = FACE_DISPLAY_MAP.get(name, list(range(9)))
    return [face[i] for i in idxmap]


def _rows_from_face(face_list: list[str]) -> list[str]:
    return [
        " ".join(col(x) for x in face_list[0:3]),
        " ".join(col(x) for x in face_list[3:6]),
        " ".join(col(x) for x in face_list[6:9]),
    ]


def print_ascii_cube(cube: Cube) -> None:
    faces = cube_to_facelets(cube)
    

    U = _rows_from_face(_remap_face_for_display("U", faces["U"]))
    F = _rows_from_face(_remap_face_for_display("F", faces["F"]))
    R = _rows_from_face(_remap_face_for_display("R", faces["R"]))
    L = _rows_from_face(_remap_face_for_display("L", faces["L"]))
    B = _rows_from_face(_remap_face_for_display("B", faces["B"]))
    D = _rows_from_face(_remap_face_for_display("D", faces["D"]))

    pad = " " * 7

    # Up
    for row in U:
        print(pad + row)
    print()

    # L F R B
    for i in range(3):
        print(f"{L[i]}   {F[i]}   {R[i]}   {B[i]}")
    print()

    # Down
    for row in D:
        print(pad + row)
    print()
