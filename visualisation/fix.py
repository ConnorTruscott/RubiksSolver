import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cube_model import Cube
from cube_moves import apply_move
from ascii_cube import print_ascii_cube, cube_to_facelets

def show_edges(cube):
    faces = cube_to_facelets(cube)
    print("D face:", faces["D"])
    print("B face:", faces["B"])
    print()

cube = Cube()
print("After F:")
show_edges(apply_move(cube,"F"))

print("After D:")
show_edges(apply_move(cube,"D"))

print("After B:")
show_edges(apply_move(cube,"B"))
