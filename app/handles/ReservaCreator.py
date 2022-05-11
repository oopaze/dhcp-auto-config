from typing import Any, List


class ReservaCreator:
    _fields = []
    fields_length = len(_fields)
    values = {}

    def __init__(self, fields):
        self._fields = fields

    @property
    def fields(self):
        return self._fields

    def get_fields(self):
        is_validated = False

        while not (is_validated):
            for field in self.fields:
                name = field['name']
                key = field['key']

                self.get_field(name, key)

            print("\nConfirma Reserva?")
            if self.confirm_fields():
                is_validated = True

        return self.values

    def get_field(self, name: str, key: str):
        value = input(f"Digite o {name}: ")
        self.values[key] = value

    def confirm_fields(self):
        reserva_as_str = ""

        for idx, (_, value) in enumerate(self.values.items()):
            field = self.fields[idx]
            reserva_as_str += f"{field['name']}={value}"

            is_last = idx == self.fields_length - 1
            if not is_last:
                reserva_as_str += " | "

        is_confirmed = input(f"{reserva_as_str}\nS/N: ").lower() == "s"

        return is_confirmed

    def values_as_csv(self, values: List[Any]):
        string_values = '\n'
        values_items = values.items()

        for idx, (_, value) in enumerate(values_items):
            string_values += value

            is_last_value = idx == len(values_items) - 1
            if not is_last_value:
                string_values += ','

        return string_values
