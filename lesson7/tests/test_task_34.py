# -*- coding: utf-8 -*-

from lesson7 import helpers, tasks
from lesson7.tests.test_task_base import Test_TaskBase


class Test_Task_34(Test_TaskBase):
    def test_calculation(self):
        for inpt, expected_res in (
                (('пара-ра-рам рам-пам-папам па-ра-па-да',), 'Парам пам-пам\n'),
                (('пара-ра-рам рам-пам-папам па-ра-па',), 'Пам парам\n')):
            self.reset_output()
            self.mock_input(inpt)
            tasks.task_34()
            self.assertEqual(self.task_output, expected_res)

    def test_wrong_symbol_input(self):
        for inpt in (
                ('z',),
                ('3',),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, f"'{inpt[0]}' is not allowed symbol, try again"):
                tasks.task_34()

    def test_empty_input(self):
        for inpt in (
                ('',),
                (' ',),
                ('  ',),):
            self.mock_input(inpt)
            with self.assertRaisesRegex(helpers.UserInputError, "Input at least one phrase, try again"):
                tasks.task_34()

