"""Generate lists of strings, to be used with stringparse and others."""
from random import randint


class RandomChar:
    """Iterator. Returns random upper or lower case character."""

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


class RandomNum:
    """Iterator. Returns random single digit positive integer."""

    def __iter__(self):
        return self

    def __next__(self):
        return self._get_random_num()

    @staticmethod
    def _get_random_num():
        return randint(0, 9)


def generate_char_string(length):
    char = RandomChar()
    return ''.join([next(char) for x in range(length)])


def generate_list_of_strings(string_len, list_len):
    the_list = []
    for l in range(list_len):
        the_list.append(generate_char_string(string_len))
    return the_list
