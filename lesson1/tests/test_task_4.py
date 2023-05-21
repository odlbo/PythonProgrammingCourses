import builtins

from unittest import TestCase
from unittest.mock import Mock

from lesson1 import helpers, tasks


class Test_Task4(TestCase):
    def test_calculation(self):
        for inpt, expected in \
                (('6', '6 -> 1 4 1'), ('24', '24 -> 4 16 4'), ('60', '60 -> 10 40 10')):

            builtins.input = Mock(return_value=inpt)

            result = None
            def mocked_print(res):
                nonlocal result
                result = res
            builtins.print = Mock(side_effect=mocked_print)

            tasks.task_4()

            self.assertEqual(result, expected)

    def test_input_params(self):
        builtins.input = Mock(return_value='6')

        origin_read_user_input = helpers.read_user_input

        params = None
        def mocked_read_user_input(**kwargs):
            nonlocal params
            params = kwargs
            return origin_read_user_input(**kwargs)
        helpers.read_user_input = Mock(side_effect=mocked_read_user_input)

        tasks.task_4()

        self.assertDictEqual(
            params,
            {
                'prompt': 'Input number: ',
                'elements_type': int,
                'elements_delimeter': None,
                'elements_required_count': 1,
                'custom_elements_checkers': [tasks.positive_number_devided_on_6_checker]
            })


class Test_PositiveNumberDevidedOn6Checker(TestCase):
    def test__bad_user_input__equal_zero(self):
        with self.assertRaisesRegex(helpers.UserInputError, "'0' is invalid number for this task, try again"):
            tasks.positive_number_devided_on_6_checker([0])

    def test__bad_user_input__less_zero(self):
        with self.assertRaisesRegex(helpers.UserInputError, "'-1' is invalid number for this task, try again"):
            tasks.positive_number_devided_on_6_checker([-1])

    def test__bad_user_input__not_devided_on_six(self):
        with self.assertRaisesRegex(helpers.UserInputError, "'7' is invalid number for this task, try again"):
            tasks.positive_number_devided_on_6_checker([7])

    def test__good_user_input(self):
        tasks.positive_number_devided_on_6_checker([6])
