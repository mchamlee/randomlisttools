import sys
import os
import unittest
from io import StringIO
from contextlib import contextmanager
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from randomlisttools import stringparse, stringgenerate


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestConsecutiveCharsConsole(unittest.TestCase):
    def test_return_correct_transform_obj_positive(self):
        self.assertEqual(stringparse.ConsecutiveChars(['abXyz', 'befgh', 'cFvwX', 'DGjhY']).get_parsed_list(),
                         ['ab', 'yz', 'efgh', 'vw', 'abc', 'FG', 'XY'])

    def test_stdout_correct_transform_print_positive(self):
        with captured_output() as (out, err):
            stringparse.ConsecutiveChars(['abXyz', 'befgh', 'cFvwX', 'DGjhY']).print_parsed_list()

        output = out.getvalue().strip()
        self.assertEqual(output, "['ab', 'yz', 'efgh', 'vw', 'abc', 'FG', 'XY']")

    def test_return_failure_list_config_negative(self):
        with self.assertRaises(ValueError) as context:
            stringparse.ConsecutiveChars(['abXyz', 'bfgh', 'cFvwX', 'DGjhY'])

        self.assertTrue("All members of list must be the same length." in str(context.exception))


class TestConsecutiveCharsTerminal(unittest.TestCase):
    def test_return_correct_transform_direct_positive(self):
        self.assertEqual(stringparse.main(['', 'ConsecutiveChars', 'abXyz,befgh,cFvwX,DGjhY']), 0)

    def test_stdout_correct_transform_direct_positive(self):
        with captured_output() as (out, err):
            stringparse.main(['', 'ConsecutiveChars', 'abXyz,befgh,cFvwX,DGjhY'])

        output = out.getvalue().strip()
        self.assertEqual(output, "['ab', 'yz', 'efgh', 'vw', 'abc', 'FG', 'XY']")

    def test_return_correct_transform_file_positive(self):
        self.assertEqual(stringparse.main(['', 'ConsecutiveChars', 'array_of_strings.txt']), 0)

    def test_stdout_correct_transform_file_positive(self):
        with captured_output() as (out, err):
            stringparse.main(['', 'ConsecutiveChars', 'test_files/array_of_strings.txt'])

        output = out.getvalue().strip()
        self.assertEqual(output, "['ab', 'yz', 'efgh', 'vw', 'abc', 'DE', 'FG', 'XY']")

    def test_return_failure_code_missing_param_negative(self):
        try:
            stringparse.main([''])
        except SystemExit as e:
            self.assertEqual(e.code, 2)

    # def test_return_failure_msg_missing_param_negative(self):
    #     with captured_output() as (out, err):
    #         try:
    #             stringparse.main([''])
    #         except SystemExit:
    #             pass
    #
    #     output = err.getvalue().strip()
    #     self.assertEqual(output, "usage: string_of_arrays_tests.py [-h] string_of_arrays\n"
    #                              "string_of_arrays_tests.py: error: the following arguments "
    #                              "are required: string_of_arrays")


class TestStringGenerateGenerateCharString(unittest.TestCase):
    def test_string_length_positive(self):
        self.assertEqual(len(stringgenerate.generate_char_string(5)), 5)

    def test_string_length_negative(self):
        with self.assertRaises(ValueError):
            stringgenerate.generate_char_string(-1)


class TestStringGenerateGenerateNumString(unittest.TestCase):
    def test_string_length_positive(self):
        self.assertEqual(len(stringgenerate.generate_num_string(5)), 5)

    def test_string_length_negative(self):
        with self.assertRaises(ValueError):
            stringgenerate.generate_num_string(-1)


class TestStringGenerateGenerateListOfStrings(unittest.TestCase):

    def setUp(self):
        self.string_len = 5
        self.list_len = 4
        self.list_of_strings = stringgenerate.generate_list_of_strings(self.string_len, self.list_len)

    def test_string_length_positive(self):
        string_len_test_list = [self.string_len for _ in range(self.list_len)]
        list_of_strings_str_len = list(map(len, self.list_of_strings))

        self.assertEqual(list_of_strings_str_len, string_len_test_list)

    def test_list_length_positive(self):
        list_of_strings_list_len = len(self.list_of_strings)

        self.assertEqual(self.list_len, list_of_strings_list_len)

    def test_string_length_negative(self):
        with self.assertRaises(ValueError):
            stringgenerate.generate_list_of_strings(-1, self.list_len)

    def test_list_length_negative(self):
        with self.assertRaises(ValueError):
            stringgenerate.generate_list_of_strings(self.string_len, -1)


if __name__ == '__main__':
    unittest.main()
