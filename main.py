from input import read_cube
from cube_validation import validate_facelets

def main():
    while True:
        cube = read_cube()

        try:
            validate_facelets(cube)
        except ValueError as e:
            print(f"Validation Error: {e}\n")
            print("Please re-enter the cube correctly.\n")
            continue

        break

    print("\nCube input received:")
    for face, colours in cube.items():
        print(f"{face}: {colours}")

if __name__ == "__main__":
    main()