"""Solve the white cross on the D face using a small BFS over edge state."""

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from collections import deque

from cube_model import Cube
from cube_moves import apply_move

# White is on the D face in your scheme.
# White edges are the cubies: DR=8, DF=9, DL=10, DB=11
WHITE_EDGE_INDICES = [8, 9, 10, 11]
WHITE_EDGE_TARGETS = {
    8: 8,   # DR cubie should go to DR position
    9: 9,   # DF -> DF
    10: 10, # DL -> DL
    11: 11, # DB -> DB
}

# Allowed moves for cross search
MOVES = [
    "U", "U'", "U2",
    "D", "D'", "D2",
    "F", "F'", "F2",
    "B", "B'", "B2",
    "L", "L'", "L2",
    "R", "R'", "R2",
]


def edges_key(cube: Cube) -> tuple:
    """
    Hashable key for BFS.
    We only care about edges for the cross, so we use edge perm + orient.
    """
    return (tuple(cube.edges_perm), tuple(cube.edges_orient))


def is_white_cross_solved(cube: Cube) -> bool:
    """
    Check if the four white edges (DR, DF, DL, DB) are in the correct
    positions on the D face and correctly oriented (eo == 0).
    """
    ep = cube.edges_perm
    eo = cube.edges_orient

    for cubie in WHITE_EDGE_INDICES:
        target_pos = WHITE_EDGE_TARGETS[cubie]
        if ep[target_pos] != cubie:
            return False
        if eo[target_pos] != 0:
            return False

    return True


def solve_cross(start_cube: Cube, max_depth: int = 8) -> tuple[Cube, list[str]]:
    """
    Solve the white cross on the D face by BFS over edge state.
    Returns (solved_cube, move_list).

    max_depth controls how far we search; 8 seems to be sufficient for cross.
    """

    if is_white_cross_solved(start_cube):
        return start_cube.copy(), []

    start_key = edges_key(start_cube)
    visited = {start_key}

    # BFS queue: (cube_state, moves_so_far)
    queue = deque()
    queue.append((start_cube.copy(), []))

    while queue:
        cube, moves = queue.popleft()

        if len(moves) >= max_depth:
            continue

        for mv in MOVES:
            next_cube = apply_move(cube, mv)
            key = edges_key(next_cube)

            if key in visited:
                continue
            visited.add(key)

            new_moves = moves + [mv]

            if is_white_cross_solved(next_cube):
                return next_cube, new_moves

            queue.append((next_cube, new_moves))

    raise RuntimeError("White cross not found within depth limit")
