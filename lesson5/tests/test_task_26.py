from lesson5 import helpers, tasks
from lesson5.tests.test_task_base import Test_TaskBase


class Test_Task_26(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('3', '5'), 'A = 3; B = 5 -> 243\n'),
                (('2', '3'), 'A = 2; B = 3 -> 8\n'),):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_26()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_symbol_input(self):
        for inpt in (
                ('z',),
                ('3', 'z'),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'z' is not of type int, try again"):
                tasks.task_26()

