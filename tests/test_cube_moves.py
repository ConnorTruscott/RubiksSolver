import pytest
import random
from cube_model import Cube
from cube_moves import apply_move, apply_algorithm

@pytest.fixture
def solved_cube():
    return Cube()

def test_single_moves(solved_cube):
    cube_U = apply_move(solved_cube, "U")
    assert not cube_U.is_solved()

    #Apply prime to see if it solves
    cube_Uprime = apply_move(cube_U, "U'")
    assert cube_Uprime.is_solved()

def test_single_moves_R(solved_cube):
    cube_R = apply_move(solved_cube, "R")
    assert not cube_R.is_solved()

    #Apply prime to see if it solves
    cube_Rprime = apply_move(cube_R, "R'")
    assert cube_Rprime.is_solved()

def test_double_move(solved_cube):
    cube_U2 = apply_move(solved_cube, "U2")
    assert not cube_U2.is_solved()
    cube_U2U2 = apply_move(cube_U2, "U2")
    assert cube_U2U2.is_solved()

def test_simple_algo(solved_cube):
    alg = "U U U U"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "R R R R"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "L L L L"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "F F F F"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "D D D D"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "B B B B"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "U' U' U' U'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "R' R' R' R'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "L' L' L' L'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "F' F' F' F'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "D' D' D' D'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

    alg = "B' B' B' B'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

def test_move_with_prime(solved_cube):
    alg = "R R' R R'"
    cube_alg = apply_algorithm(solved_cube, alg)
    assert cube_alg.is_solved()

def test_algorithm(solved_cube):
    alg = "R U R' U'"
    cube_alg = apply_algorithm(solved_cube, alg)
    print(f"Cube alg: {cube_alg}")
    assert not cube_alg.is_solved()
    inverse_alg = "U R U' R'"
    cube_alg_inverse = apply_algorithm(cube_alg, inverse_alg)
    print(f"Cube alg: {cube_alg_inverse}")
    assert cube_alg_inverse.is_solved()

def test_algo_not_U_R(solved_cube):
    print(solved_cube)
    alg = "L D L' D'"
    cube_alg = apply_algorithm(solved_cube, alg)
    print(f"Cube alg: {cube_alg}")
    assert not cube_alg.is_solved()
    inverse_alg = "D L D' L'"
    cube_alg_inverse = apply_algorithm(cube_alg, inverse_alg)
    print(f"Cube alg: {cube_alg_inverse}")
    assert cube_alg_inverse.is_solved()

def test_algo_F_R(solved_cube):
    print(solved_cube)
    alg = "F R F' R'"
    cube_alg = apply_algorithm(solved_cube, alg)
    print(f"Cube alg: {cube_alg}")
    assert not cube_alg.is_solved()
    inverse_alg = "R F R' F'"
    cube_alg_inverse = apply_algorithm(cube_alg, inverse_alg)
    print(f"Cube alg: {cube_alg_inverse}")
    assert cube_alg_inverse.is_solved()

@pytest.mark.parametrize("move", ["U", "D", "L", "R", "F", "B"])
def test_move_inverse(solved_cube, move):
    cube = apply_move(solved_cube, move)
    cube = apply_move(cube, move + "'")
    assert cube.is_solved()

@pytest.mark.parametrize("move", ["U", "D", "L", "R", "F", "B"])
def test_move_four_times(solved_cube, move):
    cube = solved_cube
    for _ in range(4):
        cube = apply_move(cube, move)
    assert cube.is_solved()

@pytest.mark.parametrize("move", ["U", "D", "L", "R", "F", "B"])
def test_move_U2_twice(solved_cube, move):
    cube = solved_cube
    cube = apply_move(cube, move + "2")
    cube = apply_move(cube, move + "2")
    assert cube.is_solved()


@pytest.mark.parametrize("alg", [
    "R U R' U'",
    "F R F' R'",
    "L D L' D'",
    "R B R' B'",
])
def test_basic_commutators_scramble(solved_cube, alg):
    cube = apply_algorithm(solved_cube, alg)
    assert not cube.is_solved()


@pytest.mark.parametrize("alg,inverse", [
    ("R U R' U'", "U R U' R'"),
    ("F R F' R'", "R F R' F'"),
    ("L D L' D'", "D L D' L'"),
    ("R B R' B'", "B R B' R'"),
])
def test_commutator_inverse(solved_cube, alg, inverse):
    cube = apply_algorithm(solved_cube, alg)
    cube = apply_algorithm(cube, inverse)
    assert cube.is_solved()


def random_move():
    moves = ["U","D","L","R","F","B"]
    suffix = ["", "'", "2"]
    return random.choice(moves) + random.choice(suffix)

def inverse_move(move):
    if move.endswith("'"): return move[0]
    if move.endswith("2"): return move
    return move + "'"

def test_random_scramble_inverses(solved_cube):
    for _ in range(50):  # run 50 random scrambles
        scramble = [random_move() for _ in range(20)]
        cube = apply_algorithm(solved_cube, " ".join(scramble))
        inverse = " ".join(inverse_move(m) for m in reversed(scramble))
        cube = apply_algorithm(cube, inverse)
        assert cube.is_solved()

   
def test_corner_twist_sum_mod3(solved_cube):
    cube = apply_algorithm(solved_cube, "R U R' U' F R F' R'")
    assert sum(cube.corners_orient) % 3 == 0

def test_edge_flip_parity(solved_cube):
    cube = apply_algorithm(solved_cube, "R U R' U' F R F' R'")
    assert sum(cube.edges_orient) % 2 == 0

