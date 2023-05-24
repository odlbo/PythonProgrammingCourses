import builtins

from unittest import TestCase
from unittest.mock import Mock

from lesson2 import helpers, tasks


class Test_Task14(TestCase):
    def test_calculation(self):
        for inpt, expected in \
                (('0', ''), ('1', '1\n'), ('5', '1\n2\n4\n')):

            builtins.input = Mock(return_value=inpt)

            result = ''

            def mocked_print(res):
                nonlocal result
                result += str(res) + '\n'

            builtins.print = Mock(side_effect=mocked_print)

            tasks.task_14()

            self.assertEqual(result, expected)

    def test_input_params(self):
        builtins.input = Mock(return_value='5')

        origin_read_user_input_inner = helpers.read_user_input_inner

        params = None

        def mocked_read_user_input_inner(**kwargs):
            nonlocal params
            params = kwargs
            return origin_read_user_input_inner(**kwargs)

        helpers.read_user_input = Mock(side_effect=mocked_read_user_input_inner)

        tasks.task_14()

        self.assertDictEqual(
            params,
            {
                'prompt': 'Input integer number: ',
                'elements_type': int,
                'elements_required_count': 1,
            })
