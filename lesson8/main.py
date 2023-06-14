import os

from textwrap import dedent

from lesson8 import helpers
from lesson8.model import Person
from lesson8.storage import Client as StorageClient


PATH_TO_CSV_FILE = os.path.join(
    os.path.dirname(__file__), 'data/phonebook.txt')


COMMAND_SHOW_ALL = 1
COMMAND_SELECT = 2
COMMAND_ADD = 3
COMMAND_UPDATE = 4
COMMAND_DELETE = 5
COMMAND_EXIT = 6


def main():
    storage_client = StorageClient(PATH_TO_CSV_FILE)

    helpers.write_output(dedent(
        '''Hello, meat bag!
           [1] -- press for SHOW ALL 
           [2] -- press for SELECT 
           [3] -- press for ADD DATA
           [4] -- press for UPDATE DATA
           [5] -- press for DELETE DATA
           [6] -- press for EXIT\n'''))

    try:
        while True:
            command_id = helpers.read_one(
                prompt='Input yor choise: ',
                elements_type=int,
                custom_elements_checkers=(_available_command_checker,))

            if command_id == COMMAND_SHOW_ALL:
                _show_all_command(storage_client)
            elif command_id == COMMAND_SELECT:
                _select_command(storage_client)
            elif command_id == COMMAND_ADD:
                _add_command(storage_client)
            elif command_id == COMMAND_UPDATE:
                _update_command(storage_client)
            elif command_id == COMMAND_DELETE:
                _delete_command(storage_client)
            elif command_id == COMMAND_EXIT:
                helpers.write_output('Goodbye!')
                break

    finally:
        storage_client.close()


def _show_all_command(storage_client):
    helpers.write_output('Trying to show all persons...')
    _print_persons(storage_client.find())


def _select_command(storage_client):
    helpers.write_output('Trying to select persons...')
    _print_persons(storage_client.find(
        first_name=helpers.read_one(prompt='Input first name or empty string: '),
        last_name=helpers.read_one(prompt='Input last name or empty string: '),
        surname=helpers.read_one(prompt='Input surname or empty string: '),
        phone_number=helpers.read_one(prompt='Input phone number or empty string: '),
    ))


def _add_command(storage_client):
    helpers.write_output('Trying to add person...')
    storage_client.add(person=_read_person_info())
    helpers.write_output('Person has been added\n')


def _delete_command(storage_client):
    helpers.write_output('Trying to delete person...')
    storage_client.delete(
        helpers.read_one(prompt='Input ID: ', elements_type=int),
    )
    helpers.write_output('Person has been deleted\n')


def _update_command(storage_client):
    helpers.write_output('Trying to update person...')

    person_id = helpers.read_one(prompt='Input ID: ', elements_type=int)
    person = _read_person_info()

    person.id = person_id

    storage_client.update(person=person)
    helpers.write_output('Person has been updated\n')


def _read_person_info():
    return Person(
        first_name=_read_one_non_empty(prompt='Input first name: '),
        last_name=_read_one_non_empty(prompt='Input last name: '),
        surname=_read_one_non_empty(prompt='Input surname: '),
        phone_number=_read_one_non_empty(prompt='Input phone number: '))


def _read_one_non_empty(prompt):
    return helpers.read_one(prompt=prompt, custom_elements_checkers=(_empty_string_not_allowed_checker,))


def _print_persons(persons):
    helpers.write_output('Persons:')
    find_any = False
    for person in persons:
        find_any = True
        helpers.write_output(
            f'{person.id} - {person.phone_number}: {person.first_name} {person.last_name} {person.surname}')

    if find_any:
        helpers.write_output('')
    else:
        helpers.write_output('No one person has been found\n')


def _available_command_checker(user_input):
    if user_input[0] not in (
            COMMAND_SHOW_ALL,
            COMMAND_SELECT,
            COMMAND_ADD,
            COMMAND_UPDATE,
            COMMAND_DELETE,
            COMMAND_EXIT,
    ):
        raise helpers.UserInputError('Invalid command ID, try again')


def _empty_string_not_allowed_checker(user_input):
    if not user_input:
        raise helpers.UserInputError('Empty string is not allowed, try again')


if __name__ == '__main__':
    main()
