import random
import math

def manipulate_numbers():
    random_numbers = []
    for _ in range(5):
        random_numbers.append(random.randint(20, 50))
    for i in range(len(random_numbers)):
        if random_numbers[i] % 2 == 0:
            random_numbers[i] = math.pow(random_numbers[i], 2)
    return random_numbers
print(manipulate_numbers())      