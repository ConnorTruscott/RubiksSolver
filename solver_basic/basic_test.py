import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cross import solve_cross_beginner as solve_cross
from cross_BFS import solve_cross as solve_cross_BFS
from cube_model import Cube
from cube_moves import apply_algorithm
from visualisation.ascii_cube import print_ascii_cube

cube = Cube()
scrambled = apply_algorithm(cube, "R2 L2 F2 B2 U2 D2 R' L' U'")

print_ascii_cube(scrambled)

solved, moves = solve_cross(scrambled)

print("Cross solution: ", moves)
print_ascii_cube(solved)