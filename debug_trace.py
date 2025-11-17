from cube_model import Cube
from cube_moves import apply_move

cube = Cube()
cube_r = apply_move(cube, "R")
cube_rprime = apply_move(cube_r, "R'")
print(cube_rprime.is_solved())  # Should be True