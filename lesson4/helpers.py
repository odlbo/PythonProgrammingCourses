import builtins


class UserInputError(Exception):
    pass


def read_input(prompt):
    return builtins.input(prompt)


def write_output(output):
    builtins.print(output)


def join_digits(digits, join_symbols=''):
    return join_symbols.join(map(str, digits))


def read_user_input_inner(
        prompt, elements_type, elements_delimeter='',
        elements_required_count=None, custom_elements_checkers=None):

    user_input = []

    raw_user_input = read_input(prompt)

    if elements_delimeter != "":
        parsed_user_input = raw_user_input.split(elements_delimeter)
    else:
        parsed_user_input = [i for i in raw_user_input]

    if elements_required_count:
        if len(parsed_user_input) > elements_required_count:
            raise UserInputError("Too much elements, try again")

        if len(parsed_user_input) < elements_required_count:
            raise UserInputError("Too few elements, try again")

    try:
        for i in parsed_user_input:
            i = elements_type(i)
            user_input.append(i)
    except ValueError:
        raise UserInputError(f"'{i}' is not of type {elements_type.__name__}, try again")

    if custom_elements_checkers:
        for checker in custom_elements_checkers:
            checker(user_input)

    return user_input


def read_user_input(
        prompt, elements_type, elements_delimeter='',
        elements_required_count=None, custom_elements_checkers=None,
        retry_on_errors=True):

    while True:
        try:
            return read_user_input_inner(
                prompt=prompt,
                elements_type=elements_type,
                elements_delimeter=elements_delimeter,
                elements_required_count=elements_required_count,
                custom_elements_checkers=custom_elements_checkers,
            )
        except UserInputError as err:
            write_output(UserInputError)
            if not retry_on_errors:
                raise
            continue
