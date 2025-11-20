import pytest
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
