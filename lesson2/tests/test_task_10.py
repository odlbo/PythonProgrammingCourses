import builtins

from unittest import TestCase
from unittest.mock import Mock

from lesson2 import tasks, helpers


class Test_Task10(TestCase):
    def test_calculation(self):
        for count, eagls_tails, expected in \
                (('1', ['1'], '0\n'), ('3', ['1', '1', '0'], '1\n')):

            inputs = (i for i in [count] + eagls_tails)
            def mocked_input(*args, **kwargs):
                return next(inputs)

            builtins.input = Mock(side_effect=mocked_input)

            result = ''
            def mocked_print(res):
                nonlocal result
                result += f"{res}\n"
            builtins.print = Mock(side_effect=mocked_print)

            tasks.task_10()

            self.assertEqual(result, expected)


class Test_EveryElementGreaterThan1Checker(TestCase):
    def test__restricted_symbols_found(self):
        with self.assertRaisesRegex(helpers.UserInputError, "'-1' is less than 1, try again"):
            tasks.every_element_greater_than_1_checker([-1, 1])

    def test__restricted_symbols_not_found(self):
        tasks.every_element_greater_than_1_checker([1, 2])