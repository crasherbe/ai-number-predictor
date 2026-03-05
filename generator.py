import random

def generate_candidates(length, total=10000):

    max_num = 10**length - 1

    numbers = []

    for i in range(total):

        n = str(random.randint(0,max_num)).zfill(length)

        numbers.append(n)

    return numbers
