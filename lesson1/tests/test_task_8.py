import builtins

from unittest import TestCase
from unittest.mock import Mock

from lesson1 import helpers, tasks


class Test_Task8(TestCase):
    def test_calculation(self):
        for inpt, expected in \
                (('3 2 4', '3 2 4 -> yes'), ('3 2 1', '3 2 1 -> no'), ('3 2 10', '3 2 10 -> no')):

            builtins.input = Mock(return_value=inpt)

            result = None
            def mocked_print(res):
                nonlocal result
                result = res
            builtins.print = Mock(side_effect=mocked_print)

            tasks.task_8()

            self.assertEqual(result, expected)

    def test_input_params(self):
        builtins.input = Mock(return_value='3 8 5')

        origin_read_user_input = helpers.read_user_input

        params = None
        def mocked_read_user_input(**kwargs):
            nonlocal params
            params = kwargs
            return origin_read_user_input(**kwargs)
        helpers.read_user_input = Mock(side_effect=mocked_read_user_input)

        tasks.task_8()

        self.assertDictEqual(
            params,
            {
                'prompt': 'Input 3 digits splited with white space: ',
                'elements_type': int,
                'elements_delimeter': ' ',
                'elements_required_count': 3,
                'custom_elements_checkers': [tasks.zero_is_restricted_symbols],
            })


class Test_ZeroIsRestrictedSymbols(TestCase):
    def test__restricted_symbols_found(self):
        with self.assertRaisesRegex(helpers.UserInputError, "'0' is not allwoed, try again"):
            tasks.zero_is_restricted_symbols([1, 0, 2])

    def test__restricted_symbols_not_found(self):
        tasks.zero_is_restricted_symbols([1, 2, 3])
