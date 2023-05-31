from lesson4 import helpers


def _set_size_greater_than_0_checker(user_input):
    for i in user_input:
        if i < 1:
            raise helpers.UserInputError("Zero count is not allowed, try again")


def task_22():
    elements_count_a = helpers.read_user_input(
        prompt='input elements count for set A',
        elements_type=int,
        elements_delimeter=None,
        custom_elements_checkers=(_set_size_greater_than_0_checker,),
    )
    elements_count_a = elements_count_a[0]

    elements_count_b = helpers.read_user_input(
        prompt='input elements count for set B',
        elements_type=int,
        elements_delimeter=None,
        custom_elements_checkers=(_set_size_greater_than_0_checker,),
    )
    elements_count_b = elements_count_b[0]

    elements_a = helpers.read_user_input(
        prompt=f'input {elements_count_a} numbers splited with white space for set A',
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=elements_count_a,
    )

    elements_b = helpers.read_user_input(
        prompt=f'input {elements_count_b} numbers splited with white space for set B',
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=elements_count_b,
    )

    result = elements_a + elements_b
    result = set(result)
    result = sorted(result)

    helpers.write_output(
        ' '.join(map(str, result)))


def _set_size_greater_than_2_checker(user_input):
    for i in user_input:
        if i < 3:
            raise helpers.UserInputError("Count must be greater then 2, try again")


def task_24():
    elements_count = helpers.read_user_input(
        prompt='input elements count',
        elements_type=int,
        elements_delimeter=None,
        custom_elements_checkers=(_set_size_greater_than_2_checker,),
    )
    elements_count = elements_count[0]

    elements = helpers.read_user_input(
        prompt=f'input {elements_count} numbers splited with white space for set A',
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=elements_count,
    )

    extended_elements = elements + elements[:2]

    result = -1
    for i in range(0, len(elements)):
        cnt = sum(extended_elements[i:i+3])
        if cnt > result:
            result = cnt

    helpers.write_output(result)
