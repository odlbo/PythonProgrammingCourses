import builtins

from unittest.mock import Mock
from unittest import TestCase

from lesson3 import helpers


class Test_ReadUserInputInner(TestCase):
    def setUp(self):
        origin_user_iput = helpers.read_user_input
        helpers.read_user_input = Mock(
            side_effect=partial(origin_user_iput, retry_on_errors=False))