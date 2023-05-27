from lesson3 import helpers, tasks

from lesson3.tests.test_task_base import Test_TaskBase


class Test_Task_18(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('ноутбук',), '12\n'),
                (('Apple',), '9\n'),):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_20()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_one_symbol_input(self):
        for inpt in (
                ('zzz1zzz',),
                ('жжж1жжж',),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'1' is not allowed, try again"):
                tasks.task_20()

    def test_wrong_many_symbols_input(self):
        for inpt in (
                ('zzz12zzz',),
                ('жжж12жжж',),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'1', '2' is not allowed, try again"):
                tasks.task_20()

    def test_mixed_alphabets(self):
        self.mock_input(('zzzжжж',))
        with self.assertRaisesRegex(helpers.UserInputError, "Latin and cirillic simbols are mixed, try again"):
            tasks.task_20()

    def test_empty_word(self):
        self.mock_input(('',))
        with self.assertRaisesRegex(helpers.UserInputError, "Word is empty, try again"):
            tasks.task_20()
