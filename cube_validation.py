"""Purpose: validating that the inpu is a legal cube"""

from collections import Counter

VALID_COLOURS = {'W', 'Y', 'R', 'O', 'G', 'B'}
FACES = ['U', 'R', 'F', 'D', 'L', 'B']

OPPOSITE_FACES = {
    'U': 'D', 'D': 'U',
    'F': 'B', 'B': 'F',
    'L': 'R', 'R': 'L'
}

ADJACENT_FACES = {
    'U': ['F','B','L','R'],
    'D': ['F','B','L','R'],
    'F': ['U','D','L','R'],
    'B': ['U','D','L','R'],
    'L': ['U','D','F','B'],
    'R': ['U','D','F','B']
}

def validate_colour_count(facelets):
    """
    Ensure each colour appears exactly 9 times
    """
    all_colours=''.join(facelets[f] for f in FACES)
    counts=Counter(all_colours)
    for c in VALID_COLOURS:
        if counts[c] != 9:
            raise ValueError(f"Invalid number of {c} stickers: {counts[c]}")

def validate_centres_unique(facelets):
    """
    Ensure all centres are unique
    """
    centres = [facelets[f][4] for f in FACES]
    if len(set(centres)) != 6:
        raise ValueError(f"Centres are not unique: {centres}")

def validate_centre_adjacency(facelets):
    """
    Ensure no centre is adjacent to its opposite"""
    centres = {f: facelets[f][4] for f in FACES}
    for face, colour in centres.items():
        opposite_colour = centres[OPPOSITE_FACES[face]]
        for adj_face in ADJACENT_FACES[face]:
            adj_colour = centres[adj_face]
            if adj_colour == opposite_colour:
                raise ValueError(f"Imposible cube: {colour} on {face} is adjacent to its opposite {adj_colour} on{adj_face}")

def validate_facelets(facelets):
    """
    Run all validation checks
    """
    validate_colour_count(facelets)
    validate_centres_unique(facelets)
    validate_centre_adjacency(facelets)
    