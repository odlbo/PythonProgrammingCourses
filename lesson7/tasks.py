# -*- coding: utf-8 -*-
from functools import partial

from lesson7 import helpers

_VOWEL_SYMBOLS = 'аоуыэеёиюя'
_CONSONANT_SYMBOLS = 'бвгджзйклмнпрстфхцчшщ'
_TERMINAL_SYMBOLS = '-'
_ALLOWED_SYMBOLS = _VOWEL_SYMBOLS + _CONSONANT_SYMBOLS + _TERMINAL_SYMBOLS


def task_34():
    phrases = helpers.read_user_input(
        prompt='input your masterpeace: ',
        elements_type=str,
        elements_delimeter=' ',
        custom_elements_checkers=(
            _only_cirrilic_alphabet_checker,
            partial(_more_gte_one_element_checker, message="Input at least one phrase, try again")),
    )

    vowel_counts = \
        [sum(phr.count(sym) for sym in _VOWEL_SYMBOLS)  # sum of vowel symbols for a phrase
         for phr in phrases]  # iterate over phrases

    if max(vowel_counts) == min(vowel_counts):
        result = 'Парам пам-пам'
    else:
        result = 'Пам парам'

    helpers.write_output(result)


def task_36():
    code = helpers.read_one(
        prompt='input your code: ',
        elements_type=str,
        custom_elements_checkers=(
            partial(_more_gte_one_element_checker, message="Input code, try again"),),
    )

    result = eval(code)

    output = '\n'.join(
        ' '.join(str(item) for item in row) for row in result)

    helpers.write_output(output)


def print_operation_table(operation, num_rows=6, num_cols=6):
    result = []
    for row in range(1, num_rows + 1):
        row_item = []
        result.append(row_item)
        for col in range(1, num_cols + 1):
            row_item.append(operation(row, col))
    return result


## Checkers
def _only_cirrilic_alphabet_checker(user_input):
    for phrase in user_input:
        for sym in phrase:
            if sym.lower() not in _ALLOWED_SYMBOLS:
                raise helpers.UserInputError(f"'{sym}' is not allowed symbol, try again")


def _more_gte_one_element_checker(user_input, message):
    for item in user_input:
        item = item.strip()
        if len(item) == 0:
            raise helpers.UserInputError(message)

