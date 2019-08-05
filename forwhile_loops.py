import random

def ex1():
    """
    Roll a dice with 6 faces and count number of faces appear in 10000 iterations
    :return: a list contains 6 numbers show how many times a dice's face appear
    """
    total_roll = 10000
    num_faces = [0, 0, 0, 0, 0, 0]

    for _ in range(total_roll):
        n = random.randint(0,5)
        num_faces[n] = num_faces[n] + 1

    return num_faces
