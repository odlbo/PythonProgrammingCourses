from lesson1 import helpers


def task_2():
    digits = helpers.read_user_input(
        prompt="Input number which consists of 3 digits: ",
        elements_type=int,
        elements_required_count=3,
    )

    sum_digits = sum(digits)

    helpers.write_output(
        f"{helpers.join_digits(digits)} -> {sum_digits} ({helpers.join_digits(digits, ' + ')})")


def positive_number_devided_on_6_checker(user_input):
    number = user_input[0]
    if number <= 0 or number % 6 != 0:
        raise helpers.UserInputError(f"'{number}' is invalid number for this task, try again")


def task_4():
    digits = helpers.read_user_input(
        prompt="Input number: ",
        elements_type=int,
        elements_delimeter=None,
        elements_required_count=1,
        custom_elements_checkers=[positive_number_devided_on_6_checker]
    )

    number = digits[0]
    result: int = int(number / 6)
    helpers.write_output(f"{number} -> {result} {result * 4} {result}")


def task_6():
    digits = helpers.read_user_input(
        prompt="Input number which consists of 6 digits: ",
        elements_type=int,
        elements_required_count=6,
    )

    result = \
        'yes' if sum(digits[:3]) == sum(digits[3:]) else 'no'

    helpers.write_output(
        f"{helpers.join_digits(digits)} -> {result}")


def zero_is_restricted_symbols(user_input):
    if 0 in user_input:
        raise helpers.UserInputError("'0' is not allwoed, try again")


def task_8():
    digits = helpers.read_user_input(
        prompt="Input 3 digits splited with white space: ",
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=3,
        custom_elements_checkers=[zero_is_restricted_symbols],
    )

    a, b, k = digits

    result = \
        'yes' if (k % a == 0 or k % b == 0) and (k <= a * b) else 'no'

    helpers.write_output(f"{a} {b} {k} -> {result}")
