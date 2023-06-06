from lesson6 import helpers, tasks
from lesson6.tests.test_task_base import Test_TaskBase


class Test_Task_32(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('100', '1000'), '\n'),
                (('0', '0',), '2\n11\n16\n'),
                (('-3', '-1'), '4\n5\n8\n'),):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_32()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_symbol_input(self):
        for inpt in (
                ('z',),
                ('3', 'z'),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "'z' is not of type int, try again"):
                tasks.task_32()

    def test_first_element_less_than_second(self):
        self.mock_input(('3', '2'))
        with self.assertRaisesRegex(helpers.UserInputError, "First element must be less than second"):
            tasks.task_32()

