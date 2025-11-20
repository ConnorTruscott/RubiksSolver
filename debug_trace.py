from cube_model import Cube
from cube_moves import apply_algorithm, apply_move

cube = Cube()
x = apply_algorithm(cube, "R U R' U'")
print("After sexy move:")
print("Corners perm:", x.corners_perm)
print("Corners orient:", x.corners_orient)
print("Edges perm:", x.edges_perm)
print("Edges orient:", x.edges_orient)

y = apply_algorithm(x, "U R U' R'")
print("\nAfter applying your inverse:")
print("Corners perm:", y.corners_perm)
print("Corners orient:", y.corners_orient)
print("Edges perm:", y.edges_perm)
print("Edges orient:", y.edges_orient)

print("\nIs solved?", y.is_solved())