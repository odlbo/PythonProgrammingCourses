from lesson6 import helpers, tasks
from lesson6.tests.test_task_base import Test_TaskBase


class Test_Task_30(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('3', '4', '2'), '3\n7\n'),
                (('3', '-4', '2'), '3\n-1\n'),
                (('2', '100', '1'), '2\n'),
                (('2', '100', '0'), '\n'),
                (('2', '0', '3'), '2\n2\n2\n')):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_30()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_symbol_input(self):
        for inpt in (
                ('z',),
                ('3', 'z'),
                ('3', '2', 'z'),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'z' is not of type int, try again"):
                tasks.task_30()

