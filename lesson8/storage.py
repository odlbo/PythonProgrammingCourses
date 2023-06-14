import csv
from lesson8.model import Person


class StorageClientBaseException(Exception):
    pass


class StorageClientNotFound(StorageClientBaseException):
    pass


class Client:
    def __init__(self, path_to_file):
        self._path_to_file = path_to_file
        self._need_to_save_data_flag = False
        self._current_id = 0
        self._readed_data = {}
        self._read_data()

    def add(self, person: Person):
        person.id = self._current_id

        self._hash_data(person)

        self._need_to_save_data_flag = True

    def delete(self, person_id: str):
        person = self._readed_data.pop(person_id, None)
        if not person:
            raise StorageClientNotFound(f"Person with id {person_id} not found")

        self._need_to_save_data_flag = True

    def update(self, person: Person):
        old_person = self._readed_data.get(person.id, None)
        if not old_person:
            raise StorageClientNotFound(f"Person with id {person.id} not found")

        self._hash_data(person)

        self._need_to_save_data_flag = True

    def find(self, first_name=None, last_name=None, surname=None, phone_number=None):
        for person in self._readed_data.values():
            if first_name and person.first_name != first_name:
                continue
            if last_name and person.last_name != last_name:
                continue
            if surname and person.surname != surname:
                continue
            if phone_number and person.phone_number != phone_number:
                continue

            yield person

    def save_changes(self):
        if self._need_to_save_data_flag:
            self._save_data()

    def _read_data(self):
        with open(self._path_to_file, 'r') as f:
            reader = csv.reader(f, delimiter=',', skipinitialspace=True)
            for raw_data in reader:
                if not raw_data:
                    continue

                person = Person(
                    id=int(raw_data[0]),
                    phone_number=raw_data[1],
                    last_name=raw_data[2],
                    first_name=raw_data[3],
                    surname=raw_data[4])

                self._hash_data(person)

    def _save_data(self):
        with open(self._path_to_file, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for person in self._readed_data.values():
                writer.writerow([
                    person.id,
                    person.phone_number,
                    person.last_name,
                    person.first_name,
                    person.surname])

    def _hash_data(self, person):
        self._readed_data[person.id] = person

        if person.id > self._current_id:
            self._current_id = person.id + 1
