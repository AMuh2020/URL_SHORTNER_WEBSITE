import random
import string

chars = string.ascii_letters + string.digits


def random_string():
    return ''.join(random.choice(chars) for _ in range(6))
