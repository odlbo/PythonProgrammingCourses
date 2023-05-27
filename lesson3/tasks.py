from lesson3 import helpers


_LATIN_ALPHABET = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1,'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10,
}
_LATIN_ALPHABET.update({
    k.lower(): v for k, v in _LATIN_ALPHABET.items()})

_CIRILLIC_ALPHABET = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10,
}
_CIRILLIC_ALPHABET.update({
    k.lower(): v for k, v in _CIRILLIC_ALPHABET.items()})


def task_16():
    elements_count = helpers.read_user_input(
        prompt='input elements count',
        elements_type=int,
        elements_delimeter=None,
    )
    elements_count = elements_count[0]

    elements = helpers.read_user_input(
        prompt=f'input {elements_count} numbers splited with white space',
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=elements_count,
    )

    look_for_element = helpers.read_user_input(
        prompt=f'input number to look for',
        elements_type=int,
        elements_delimeter=None,
    )
    look_for_element = look_for_element[0]

    result = elements.count(look_for_element)

    helpers.write_output(result)


def task_18():
    elements_count = helpers.read_user_input(
        prompt='input elements count',
        elements_type=int,
        elements_delimeter=None,
    )
    elements_count = elements_count[0]

    elements = helpers.read_user_input(
        prompt=f'input {elements_count} numbers splited with white space',
        elements_type=int,
        elements_delimeter=' ',
        elements_required_count=elements_count,
    )

    element_to_find_nearest = helpers.read_user_input(
        prompt=f'input number to find the nearest element',
        elements_type=int,
        elements_delimeter=None,
    )
    element_to_find_nearest = element_to_find_nearest[0]

    result = min([
        (abs(p - element_to_find_nearest), p)
        for p in elements])

    helpers.write_output(result[1])


def _empty_word_checker(user_input):
    if not user_input:
        raise helpers.UserInputError("Word is empty, try again")


def _restricted_symbols_checker(user_input):
    allowed_symbols = set(_LATIN_ALPHABET.keys()).union(
        set(_CIRILLIC_ALPHABET.keys()))

    for p in user_input:
        restricted_symbols = set(p).difference(allowed_symbols)
        if restricted_symbols:
            restricted_symbols_str = "'" + "', '".join(sorted(restricted_symbols)) + "'"
            raise helpers.UserInputError(
                f"{restricted_symbols_str} is not allowed, try again")


def _mixed_symbols_checker(user_input):
    cirilic_set = set(_CIRILLIC_ALPHABET.keys())
    latin_set = set(_LATIN_ALPHABET.keys())

    for p in user_input:
        if set(p).intersection(cirilic_set) and set(p).intersection(latin_set):
            raise helpers.UserInputError("Latin and cirillic simbols are mixed, try again")


def task_20():
    word = helpers.read_user_input(
        prompt='input word',
        elements_type=str,
        elements_delimeter=None,
        custom_elements_checkers=[
            _empty_word_checker,
            _restricted_symbols_checker,
            _mixed_symbols_checker,
        ]
    )
    word = word[0]

    alphabet = _LATIN_ALPHABET \
        if word[0] in _LATIN_ALPHABET else _CIRILLIC_ALPHABET

    result = sum([alphabet[i] for i in word])

    helpers.write_output(result)
