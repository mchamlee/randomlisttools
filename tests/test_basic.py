import sys
import os
import unittest
from io import StringIO
from contextlib import contextmanager
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from randomlisttools import stringparse, stringgenerate, listmodify


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


class TestFlatList(unittest.TestCase):
    test_list_numeric = [1, [2, 3, [4, 5], 6, [7, [8, [9, 10]], 11, 12]], 13]

    result_list_numeric = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def test_numeric_list_positive(self):
        new_list = list(listmodify.flatten_list(self.test_list_numeric))
        self.assertEqual(new_list, self.result_list_numeric)


class TestListModifyRemoveListDupesInplace(unittest.TestCase):
    def test_numeric_list_random_dupes_positive(self):
        test_list = [1, 6, 3, 5, 6, 2, 9, 2, 1, 9, 2, 5, 1, 8, 0, 3, 5, 1, 4, 7, 5, 6]
        test_list_result = [2, 8, 0, 3, 1, 4, 7, 5, 6]
        listmodify.remove_list_dupes_inplace(test_list)
        self.assertEqual(test_list, test_list_result)

    def test_numeric_list_sequential_dupes_positive(self):
        test_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        test_list_result = [1, 2, 3, 4]
        listmodify.remove_list_dupes_inplace(test_list)
        self.assertEqual(test_list, test_list_result)

    def test_alpha_list_random_dupes_positive(self):
        test_list = ['a', 't', 'e', 'a', 'h', 'q', 'c', 'h', 'p', 'i', 'p', 'f']
        test_list_result = ['t', 'e', 'a', 'q', 'c', 'h', 'i', 'p', 'f']
        listmodify.remove_list_dupes_inplace(test_list)
        self.assertEqual(test_list, test_list_result)

    def test_alpha_list_sequential_dupes_positive(self):
        test_list = ['f', 'f', 'g', 'g', 'g', 'i', 'i', 'i', 'j', 'j', 'j', 'j']
        test_list_result = ['f', 'g', 'i', 'j']
        listmodify.remove_list_dupes_inplace(test_list)
        self.assertEqual(test_list, test_list_result)


class TestListModifyReplace(unittest.TestCase):
    test_list_alpha = ['ab-cd', 'efgh_ijkl-mnop', 'alpha-element', 'numeric_element']

    test_list_numeric = [1, 6, 100, 5, 3, 10, 34, 9432, 23]

    test_list_alpha_numeric = ['efgh_ijkl-mnop', 356, 34, 'alpha-element', 'numeric_element', 1992, 43, 'ab-cd']

    test_list_alpha_numeric_nested = [
        'efgh_ijkl-mnop', [
            356,
            34
        ], [
            'alpha-element', [
                'numeric_element',
                1992
            ],
            43
        ],
        'ab-cd'
    ]

    result_list_alpha_replace_hyphens_with_underscores = \
        ['ab_cd', 'efgh_ijkl_mnop', 'alpha_element', 'numeric_element']

    result_list_alpha_numeric_replace_underscores_with_hyphens = \
        ['efgh-ijkl-mnop', 356, 34, 'alpha-element', 'numeric-element', 1992, 43, 'ab-cd']

    result_list_alpha_numeric_nested_replace_element_with_attribute = [
        'efgh_ijkl-mnop', [
            356,
            34
        ], [
            'alpha-attribute', [
                'numeric_attribute',
                1992
            ],
            43
        ],
        'ab-cd'
    ]

    def test_alpha_list_positive(self):
        new_list = listmodify.list_replace(self.test_list_alpha, '-', '_')
        self.assertEqual(new_list, self.result_list_alpha_replace_hyphens_with_underscores)

    def test_numeric_list_positive(self):
        new_list = listmodify.list_replace(self.test_list_numeric, '-', '_')
        self.assertEqual(new_list, self.test_list_numeric)

    def test_alpha_numeric_list_positive(self):
        new_list = listmodify.list_replace(self.test_list_alpha_numeric, '_', '-')
        self.assertEqual(new_list, self.result_list_alpha_numeric_replace_underscores_with_hyphens)

    def test_alpha_numeric_nested_list_positive(self):
        new_list = listmodify.list_replace(self.test_list_alpha_numeric_nested, 'element', 'attribute')
        self.assertEqual(new_list, self.result_list_alpha_numeric_nested_replace_element_with_attribute)


if __name__ == '__main__':
    unittest.main()
