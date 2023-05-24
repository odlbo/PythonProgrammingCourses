import builtins

from unittest import TestCase
from unittest.mock import Mock

from lesson2 import helpers, tasks


class Test_Task12(TestCase):
    def test_calculation(self):
        for inpt, expected in \
                (('3 1', ''), ('6 9', '3 3\n')):

            builtins.input = Mock(return_value=inpt)

            result = ''
            def mocked_print(res):
                nonlocal result
                result += res + '\n'
            builtins.print = Mock(side_effect=mocked_print)

            tasks.task_12()

            self.assertEqual(result, expected)

    def test_input_params(self):
        builtins.input = Mock(return_value='3 8')

        origin_read_user_input = helpers.read_user_input

        params = None
        def mocked_read_user_input(**kwargs):
            nonlocal params
            params = kwargs
            return origin_read_user_input(**kwargs)
        helpers.read_user_input = Mock(side_effect=mocked_read_user_input)

        tasks.task_12()

        self.assertDictEqual(
            params,
            {
                'prompt': 'Input 2 numbers splited with white space: ',
                'elements_type': int,
                'elements_delimeter': ' ',
                'elements_required_count': 2,
                'custom_elements_checkers': [
                    tasks.every_element_less_than_1000_checker,
                    tasks.every_element_greater_than_1_checker,
                ],
            })


class Test_EveryElementLessThan1000Checker(TestCase):
    def test__restricted_symbols_found(self):
        with self.assertRaisesRegex(helpers.UserInputError, "'1001' is greater than 1000, try again"):
            tasks.every_element_less_than_1000_checker([1001, 1])

    def test__restricted_symbols_not_found(self):
        tasks.every_element_less_than_1000_checker([1, 2])


class Test_EveryElementGreaterIs0Or1Checker(TestCase):
    def test__restricted_symbols_found(self):
        with self.assertRaisesRegex(helpers.UserInputError, "Enter 1 - eagle or 0 - tail"):
            tasks.every_element_greater_is_0_or_1_checker([-1, 1])

    def test__restricted_symbols_not_found(self):
        tasks.every_element_greater_is_0_or_1_checker([1, 0])
