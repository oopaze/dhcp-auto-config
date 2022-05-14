from abc import abstractclassmethod
from typing import Any, Dict, TypedDict


class Form:
    def __init__(
        self,
        template: str,
        default_value: Dict = {},
        FormContract: TypedDict = Dict[str, Any],
    ):
        self.values: FormContract = default_value
        self.template = template

    def get_field(self, name: str, key: str):
        value = input(f"Digite o {name}: ")
        self.values[key] = value

    @abstractclassmethod
    def generate_data(self):
        raise NotImplementedError("Método não implementado")

    def confirm_fields(self) -> bool:
        instance = self.template.format(**self.values)
        print(f"\nConfirma Reserva?\n{instance}")

        is_confirmed = input("S/N: ").lower() == "s"

        return is_confirmed
