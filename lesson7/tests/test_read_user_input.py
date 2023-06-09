import builtins

from unittest.mock import Mock
from unittest import TestCase

from lesson7.helpers import UserInputError, read_user_input_inner, read_user_input


class Test_ReadUserInputInner(TestCase):
    def setUp(self):
        builtins.input = Mock(return_value='1 2 3')

    def test__parsed_input(self):
        result = read_user_input_inner(
            prompt='enter user input',
            elements_type=int,
            elements_delimeter=' ',
            elements_required_count=3,
        )
        self.assertListEqual(result, [1, 2, 3])

    def test__prompt(self):
        catched_prompt = ''

        def mocked_input(prompt):
            nonlocal catched_prompt
            catched_prompt = prompt
            return '1 2 3'

        builtins.input = Mock(side_effect=mocked_input)

        read_user_input_inner(
            prompt='enter user input',
            elements_type=int,
            elements_delimeter=' ',
            elements_required_count=3,
        )

        self.assertEqual(catched_prompt, 'enter user input')

    def test__elements_types(self):
        result = read_user_input_inner(
            prompt='enter user input',
            elements_type=str,
            elements_delimeter=' ',
            elements_required_count=3,
        )
        self.assertListEqual(result, ['1', '2', '3'])

    def test__too_few_elements(self):
        with self.assertRaisesRegex(UserInputError, 'Too few elements, try again'):
            read_user_input_inner(
                prompt='enter user input',
                elements_type=str,
                elements_delimeter=' ',
                elements_required_count=4,
            )

    def test__custom_elements_checker_fail(self):
        def hate_1_number(user_input):
            if 1 in user_input:
                raise UserInputError('I hate 1!')

        with self.assertRaisesRegex(UserInputError, "I hate 1!"):
            read_user_input_inner(
                prompt='enter user input',
                elements_type=int,
                elements_delimeter=' ',
                elements_required_count=3,
                custom_elements_checkers=[hate_1_number],
            )

    def test__custom_elements_checker_success(self):
        def hate_4_number(user_input):
            if 4 in user_input:
                raise UserInputError('I hate 4!')

        read_user_input_inner(
            prompt='enter user input',
            elements_type=int,
            elements_delimeter=' ',
            elements_required_count=3,
            custom_elements_checkers=[hate_4_number],
        )


class Test_ReadUserInput(TestCase):
    def setUp(self):
        builtins.input = Mock(return_value='123')

    def test__read_user_input(self):
        result = read_user_input(
            prompt='enter user input',
            elements_type=int,
            elements_delimeter='',
            elements_required_count=3,
        )
        self.assertListEqual(result, [1, 2, 3])


class Test_ReadUserInputWithoutRetries(TestCase):
    def setUp(self):
        builtins.input = Mock(return_value='x')

    def test__read_wrong_user_input(self):
        with self.assertRaisesRegex(UserInputError, "'x' is not of type int, try again"):
            read_user_input(
                prompt='enter user input',
                elements_type=int,
                elements_delimeter='',
                elements_required_count=1,
                retry_on_errors=False,
            )


class Test_ReadUserInputWithoutSplit(TestCase):
    def setUp(self):
        builtins.input = Mock(return_value='123')

    def test__read_user_input__with_split(self):
        result = read_user_input(
            prompt='enter user input',
            elements_type=int,
            elements_delimeter='',
            elements_required_count=3,
            split_elements=True,
            retry_on_errors=False,
        )
        self.assertListEqual(result, [1, 2, 3])

    def test__read_user_inputt__without_split(self):
        result = read_user_input(
            prompt='enter user input',
            elements_type=int,
            elements_delimeter='',
            elements_required_count=1,
            split_elements=False,
            retry_on_errors=False,
        )
        self.assertListEqual(result, [123])
