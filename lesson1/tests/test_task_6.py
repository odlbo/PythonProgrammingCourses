import builtins

from unittest import TestCase
from unittest.mock import Mock

from lesson1 import helpers
from lesson1.tasks import task_6


class Test_Task6(TestCase):
    def test_sum(self):
        for inpt, expected in (('385916', '385916 -> yes'), ('123456', '123456 -> no')):
            builtins.input = Mock(return_value=inpt)

            result = None
            def mocked_print(res):
                nonlocal result
                result = res
            builtins.print = Mock(side_effect=mocked_print)

            task_6()

            self.assertEqual(result, expected)

    def test_input_params(self):
        builtins.input = Mock(return_value='385916')

        origin_read_user_input = helpers.read_user_input

        params = None
        def mocked_read_user_input(**kwargs):
            nonlocal params
            params = kwargs
            return origin_read_user_input(**kwargs)
        helpers.read_user_input = Mock(side_effect=mocked_read_user_input)

        task_6()

        self.assertDictEqual(
            params,
            {
                'prompt': 'Input number which consists of 6 digits: ',
                'elements_type': int,
                'elements_required_count': 6,
            })
