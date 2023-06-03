from lesson5 import helpers


def task_26():
    number = helpers.read_user_input(
        prompt='input number (A): ',
        elements_type=int,
        elements_delimeter=None,
    )
    number = number[0]

    power = helpers.read_user_input(
        prompt='input power (B):',
        elements_type=int,
        elements_delimeter=None,
    )
    power = power[0]

    def calc_power(a, b):
        return \
            a * calc_power(a, b - 1) if b != 1 else a

    result = calc_power(number, power)

    helpers.write_output(
        f'A = {number}; B = {power} -> {result}')


def task_28():
    a = helpers.read_user_input(
        prompt='input first number: ',
        elements_type=int,
        elements_delimeter=None,
    )
    a = a[0]

    b = helpers.read_user_input(
        prompt='input second number:',
        elements_type=int,
        elements_delimeter=None,
    )
    b = b[0]

    def calc_sum(x, y):
        return \
            calc_sum(x + 1, y - 1) if y != 0 else x

    result = calc_sum(a, b)

    helpers.write_output(result)
