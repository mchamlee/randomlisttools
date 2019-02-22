"""Generate lists of strings, to be used with stringparse and others."""
from random import randint


class RandomChar:
    """Iterator. Returns random upper or lower case character.

    Returns:
        A single, random character.
    """

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


def generate_num_string(length):
    if length <= 0:
        raise ValueError("String length should be a positive integer greater than zero")
    return ''.join([str(randint(0, 9)) for _ in range(length)])


def generate_char_string(length):
    if length <= 0:
        raise ValueError("String length should be a positive integer greater than zero")
    char = RandomChar()
    return ''.join([next(char) for _ in range(length)])


def generate_list_of_strings(string_len, list_len):
    """Generates a list of uniform alpha-based strings.

    Args:
        string_len: Length of the strings in the list.
        list_len: Length of the list, or number of members in the list.

    Returns:
        A list.

    Raises:
        ValueError: If list length is less then or equal to 0.
    """
    if list_len <= 0:
        raise ValueError("List length should be a positive integer greater than zero")
    the_list = []
    for l in range(list_len):
        the_list.append(generate_char_string(string_len))
    return the_list


def get_fibonacci_recur(num):
    if num <= 1:
        return num
    else:
        return get_fibonacci_recur(num - 1) + get_fibonacci_recur(num - 2)


def generate_fibonacci_to_nth(nums_to_generate):
    """Generates Fibonacci sequence to a specified length.

    Args:
        nums_to_generate: Generate this many numbers in the Fibonacci sequence.

    Returns:
        A list.

    Raises:
        ValueError: If nums_to_generate is less than or equal to 0.
    """
    if nums_to_generate <= 0:
        raise ValueError("Please provide a positive integer greater than 0.")
    fib_seq = []
    for i in range(nums_to_generate):
        fib_seq.append(get_fibonacci_recur(i))
    return fib_seq
