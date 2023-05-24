from lesson2 import helpers


def every_element_greater_is_0_or_1_checker(user_input):
    for i in user_input:
        if i not in (0, 1):
            raise helpers.UserInputError("Enter 1 - eagle or 0 - tail")


def task_10():
    user_input = helpers.read_user_input(
        prompt="Input number: ",
        elements_type=int,
        elements_required_count=1,
        custom_elements_checkers=[
            every_element_greater_than_1_checker,
        ]
    )

    count = user_input[0]
    eagls, tails = 0, 0
    for i in range(count):
        user_input = helpers.read_user_input(
        prompt="Input 1 - eagl or 0 - tail: ",
        elements_type=int,
        elements_required_count=1,
        custom_elements_checkers=[
            every_element_greater_is_0_or_1_checker,
        ])

        if user_input[0] == 1:
            eagls += 1
        else:
            tails += 1

    helpers.write_output(min(eagls, tails))


def every_element_greater_than_1_checker(user_input):
    for i in user_input:
        if i < 1:
            raise helpers.UserInputError(f"'{i}' is less than 1, try again")


def every_element_less_than_1000_checker(user_input):
    for i in user_input:
        if i > 1000:
            raise helpers.UserInputError(f"'{i}' is greater than 1000, try again")


def task_12():
    digits = helpers.read_user_input(
        prompt="Input 2 numbers splited with white space: ",
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=2,
        custom_elements_checkers=[
            every_element_less_than_1000_checker,
            every_element_greater_than_1_checker,
        ]
    )

    sm, ml = digits

    for i in range(1, 1001):
        for j in range(1, 1001):
            if i + j == sm and i * j == ml:
                helpers.write_output(f"{i} {j}")


def task_14():
    digits = helpers.read_user_input(
        prompt="Input integer number: ",
        elements_type=int,
        elements_required_count=1,
    )

    limit = digits[0]
    current_number = 1
    while True:
        if current_number > limit:
            break
        helpers.write_output(current_number)
        current_number *= 2
