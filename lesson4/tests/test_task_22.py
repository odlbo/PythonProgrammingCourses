from lesson4 import helpers, tasks

from lesson4.tests.test_task_base import Test_TaskBase


class Test_Task_22(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('2', '3', '1 2', '4 2 3'), '1 2 3 4\n'),
                (('3', '3', '1 10 1', '1 1 1'), '1 10\n'),):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_22()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_symbol_input(self):
        for inpt in (
                ('z',),
                ('2', '3', 'z 1', '1 2 3'),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'z' is not of type int, try again"):
                tasks.task_22()

    def test_wrong_set_size_input(self):
        for inpt in (
                ('0',),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "Zero count is not allowed, try again"):
                tasks.task_22()