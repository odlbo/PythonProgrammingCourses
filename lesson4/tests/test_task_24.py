from lesson4 import helpers, tasks

from lesson4.tests.test_task_base import Test_TaskBase


class Test_Task_24(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('4', '1 4 2 3'), '9\n'),
                (('5', '1 10 2 4 9'), '20\n'),):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_24()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_symbol_input(self):
        for inpt in (
                ('z',),
                ('3', '1 2 z'),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'z' is not of type int, try again"):
                tasks.task_24()

    def test_wrong_set_size_input(self):
        for inpt in (('0',), ('1',), ('2',)):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "Count must be greater then 2, try again"):
                tasks.task_24()
