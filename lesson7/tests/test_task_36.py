# -*- coding: utf-8 -*-

from lesson7 import helpers, tasks
from lesson7.tests.test_task_base import Test_TaskBase


class Test_Task_36(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in ((
                ('print_operation_table(lambda x, y: x * y)',),
                '1 2 3 4 5 6\n'
                '2 4 6 8 10 12\n'
                '3 6 9 12 15 18\n'
                '4 8 12 16 20 24\n'
                '5 10 15 20 25 30\n'
                '6 12 18 24 30 36\n'),):

            self.reset_output()
            self.mock_input(inpt)
            tasks.task_36()
            self.assertEqual(self.task_output, expected_res)

    def test_empty_input(self):
        for inpt in (
                ('',),
                (' ',),
                ('  ',),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "Input code, try again"):
                tasks.task_36()
