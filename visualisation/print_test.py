import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cube_model import Cube
from cube_moves import apply_move
from ascii_cube import print_ascii_cube

cube = Cube()

print_ascii_cube(cube)

# cube = apply_move(cube, "R")
# print_ascii_cube(cube)

# cube = apply_move(cube, "U'")
# print_ascii_cube(cube)

print("Applying U move:\n")
cube = apply_move(cube, "U")
print_ascii_cube(cube)
cube = apply_move(cube, "U'")

print("Applying F move:\n")
cube = apply_move(cube, "F")
print_ascii_cube(cube)
cube = apply_move(cube, "F'")


print("Applying L move:\n")
cube = apply_move(cube, "L")
print_ascii_cube(cube)
cube = apply_move(cube, "L'")


print("Applying R move:\n")
cube = apply_move(cube, "R")
print_ascii_cube(cube)
cube = apply_move(cube, "R'")


print("Applying B move:\n")
cube = apply_move(cube, "B")
print_ascii_cube(cube)
cube = apply_move(cube, "B'")


print("Applying D move:\n")
cube = apply_move(cube, "D")
print_ascii_cube(cube)
cube = apply_move(cube, "D'")

