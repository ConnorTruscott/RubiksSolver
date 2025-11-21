from cube_model import Cube
from cube_to_facelet import cube_to_facelets

c = Cube()
faces = cube_to_facelets(c)

print("CENTRES:")
for f in ["U","F","R","B","L","D"]:
    print(f, faces[f][4])
