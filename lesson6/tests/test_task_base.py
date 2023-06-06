from functools import partial
from unittest.mock import Mock
from unittest import TestCase

from lesson6 import helpers


class Test_TaskBase(TestCase):
    def setUp(self):
        origin_user_iput = helpers.read_user_input
        helpers.read_user_input = Mock(
            side_effect=partial(origin_user_iput, retry_on_errors=False))

        origin_read_one = helpers.read_one
        helpers.read_one = Mock(
            side_effect=partial(origin_read_one, retry_on_errors=False))

        self._task_output = ''
        def mocked_write_output(res):
            self._task_output += str(res) + '\n'
        helpers.write_output = Mock(side_effect=mocked_write_output)

    @property
    def task_output(self):
        return self._task_output

    def reset_output(self):
        self._task_output = ''

    def mock_input(self, return_values):
        return_values = iter(return_values)
        helpers.read_input = Mock(
            side_effect=lambda *args, **kwargs: str(next(return_values)))

