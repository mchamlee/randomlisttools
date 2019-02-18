"""Generate lists of strings, to be used with stringparse and others."""
from random import randint


class RandomChar:

    UPPER = [x for x in range(ord('A'), ord('Z'))]
    LOWER = [y for y in range(ord('a'), ord('z'))]

    RAND_MIN = ord('A')
    RAND_MAX = ord('z')

    def __iter__(self):
        return self

    def __next__(self):
        return self._get_random_char()

    @staticmethod
    def _get_random_char():
        char_list = RandomChar.UPPER + RandomChar.LOWER
        while True:
            random_char = randint(RandomChar.RAND_MIN, RandomChar.RAND_MAX)
            if random_char in char_list:
                return chr(random_char)
