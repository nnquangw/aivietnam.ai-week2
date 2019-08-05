import random

def ex1():
    """
    Roll a dice with 6 faces and count number of faces appear in 10000 iterations
    :return: a list contains 6 numbers show how many times a dice's face appear
    """
    total_roll = 10000
    num_faces = [0, 0, 0, 0, 0, 0]

    for _ in range(total_roll):
        n = random.randint(0, 5)
        num_faces[n] = num_faces[n] + 1

    return num_faces

def ex2():
    """
    Flip a coin with 70% rate that will be head side and 30% that will be tail side
    :return: a list contains 2 numbers show how many times the coin's side appear
    """
    total_flip = 1000
    num_sides = [0, 0]

    for _ in range(total_flip):
        n = random.random()
        num_sides[round(n)] = num_sides[round(n)] + 1

    return num_sides