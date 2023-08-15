import random
import string


def generate_random_string():
    length = random.randint(5, 10)
    characters = string.ascii_letters + string.digits
    return "www.xxx.com/" + "".join(random.choice(characters) for _ in range(length))
