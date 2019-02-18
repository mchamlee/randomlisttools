import sys
import argparse

"""Parse strings in list."""


class ConsecutiveChars:
    """Find consecutive chars (based on ascii code sequence) searching through the list
    vertically and horizontally."""
    # Write a method that takes in a string of arrays as a parameter
    # and finds all consecutive characters in each string both vertically
    # and horizontally. An example if the following input:
    #
    #     [
    #         'abXyz',
    #         'befgh',
    #         'cFvwX',
    #         'DGjhY'
    #     ]
    #
    # Should print out the following out the following values:
    #
    #     ab, yz, efgh, vw, abc, FG, XY
    #
    # Test Input Console: ['abXyz', 'befgh', 'cFvwX', 'DGjhY']
    # Test Input Shell: abXyz,befgh,cFvwX,DGjhY

    def __init__(self, the_list):
        self.the_list = the_list
        self.parsed_list = self.parse_list()

    @property
    def the_list(self):
        return self._the_list

    @the_list.setter
    def the_list(self, value):
        self._set_the_list(value)

    def _set_the_list(self, value):
        """Validate list is in the structure we need. Any number of members are accepted,
        but each member should be the same number of chars."""
        member_length = len(value[0])

        for m in value:
            if len(m) != member_length:
                raise ValueError("All members of list must be the same length.")
        self._the_list = value

    def parse_list(self):
        array_of_strings_transposed = list(map(''.join, list(map(list, zip(*self.the_list)))))
        list_to_search = self.the_list + array_of_strings_transposed

        sequence_string = ''
        parsed_list = []

        for i in range(0, len(list_to_search)):
            for j, c in enumerate(list_to_search[i]):

                if j < len(list_to_search[i])-1:
                    if ord(c) == ord(list_to_search[i][j+1]) - 1:
                        if len(sequence_string) == 0:
                            sequence_string = '{}{}'.format(c, list_to_search[i][j + 1])
                        else:
                            sequence_string += list_to_search[i][j + 1]
                    else:
                        if len(sequence_string) > 1:
                            parsed_list.append(sequence_string)

                        sequence_string = ''

            # Append last/final string segment
            if i == len(list_to_search) - 1:
                if len(sequence_string) > 1:
                    parsed_list.append(sequence_string)

        return parsed_list

    def get_parsed_list(self):
        return self.parsed_list

    def print_parsed_list(self):
        print(self.parsed_list)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('class_to_call', help='Class to call in stringparse.')
    parser.add_argument('string_to_parse', help='A comma-separated list of strings, or a file that contains ' 
                                                'a list of strings')
    return parser.parse_args(args)


def main(args):
    array_of_strings = []

    args = parse_args(args[1:])

    # Test to see if file name, a file with a string of arrays, was passed in
    try:
        with open(args.string_to_parse, 'rt') as f:
            array_of_strings = f.read().split(',')
    except FileNotFoundError:
        # Not a file
        pass

    if not array_of_strings:
        array_of_strings = args.string_to_parse.split(',')

    if args.class_to_call == 'ConsecutiveChars':
        ConsecutiveChars(array_of_strings).print_parsed_list()
    else:
        raise ValueError('Not a valid class name: {}'.format(args.class_to_call))

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
