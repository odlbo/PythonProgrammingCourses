from lesson3 import helpers, tasks

from lesson3.tests.test_task_base import Test_TaskBase


class Test_Task_18(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('3', '2 1 2', '2'), '2\n'),
                (('3', '1 2 3', '0'), '1\n'),
                (('3', '1 3 4', '2'), '1\n')):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_18()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_input(self):
        for inpt in (
                ('x', '2 1 2', '2'),
                ('3', '1 x 3', '2'),
                ('3', '1 2 3', 'x')):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'x' is not of type int, try again"):
                tasks.task_18()
