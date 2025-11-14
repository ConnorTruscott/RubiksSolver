VALID_COLOURS = {'W', 'Y', 'R', 'O', 'G', 'B'}

FACE_ORDER = ['U', 'R', 'F', 'D', 'L', 'B']

FACE_ORIENTATION_HELP = {
    'U': "Hold the cube so U is facing you, R is on the right.",
    'R': "Hold the cube so R is facing you, U is on top.",
    'F': "Hold the cube so F is facing you, U is on top, R on the right.",
    'D': "Hold the cube so D is facing you, F is on top, R is on the right.",
    'L': "Hold the cube so L is facing you, U is on top.",
    'B': "Hold the cube so B is facing you, U is on top (you are viewing the back)."
}

def read_face(face_name):
    print(f"\n--- {face_name} face ---")
    print(FACE_ORIENTATION_HELP[face_name])
    print("Enter 9 colors Left to Right, Top to Bottom (e.g., WGRYOB...):")
    
    while True:
        s = input(f"{face_name}: ").strip().upper()

        if len(s) != 9:
            print("Error: must be exactly 9 characters.")
            continue
        if any(c not in VALID_COLOURS for c in s):
            print("Error: invalid colors used. Allowed: W Y R O G B")
            continue
        return s

def read_cube():
    print("Face order will be: U, R, F, D, L, B")
    print("Use letters: W Y R O G B")

    facelets = {}

    for face in FACE_ORDER:
        facelets[face]=read_face(face)
    
    return facelets