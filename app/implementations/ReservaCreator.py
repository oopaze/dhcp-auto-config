from typing import TypedDict

from app.shared.defaults import RESERVA_TEMPLATE


class ReservaContract(TypedDict):
    name: str
    MAC: str
    IP: str


class ReservaCreator:
    values: ReservaContract = {"name": None, "MAC": None, "IP": None}

    def get_field(self, name: str, key: str):
        value = input(f"Digite o {name}: ")
        self.values[key] = value

    def generate_reserva(self) -> ReservaContract:
        is_validated = False

        while not (is_validated):
            self.get_field("Nome", "name")
            self.get_field("endereço MAC", "MAC")
            self.get_field("endereço de IP", "IP")

            if self.confirm_fields():
                is_validated = True

        return self.values

    def confirm_fields(self) -> bool:
        reserva = RESERVA_TEMPLATE.format(**self.values)
        print(f"\nConfirma Reserva?\n{reserva}")

        is_confirmed = input("S/N: ").lower() == "s"

        return is_confirmed
