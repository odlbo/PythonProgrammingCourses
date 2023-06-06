from lesson6 import helpers

LST = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]


def task_30():
    first_el = helpers.read_one(
        prompt='input first element: ',
        elements_type=int,
    )

    delta = helpers.read_one(
        prompt='input delta: ',
        elements_type=int,
    )

    count = helpers.read_one(
        prompt='input count: ',
        elements_type=int,
    )

    result = [
        first_el + i * delta for i in range(0, count)]

    helpers.write_output(
        "\n".join(map(str, result)))


def task_32():
    first_el = helpers.read_one(
        prompt='input first element: ',
        elements_type=int,
    )

    second_el = helpers.read_one(
        prompt='input second element: ',
        elements_type=int,
    )

    if first_el > second_el:
        raise helpers.UserInputError("First element must be less than second")

    result = []
    for idx, el in enumerate(LST):
        if first_el <= el <= second_el:
            result.append(idx)

    helpers.write_output(
        "\n".join(map(str, result)))
