from typing import List, TypedDict

from .FileHandler import FileHandler


class AddressContract(TypedDict):
    computer_name: str
    mac_address: str
    ip_address: str


class ParserAddress(FileHandler):
    def parser(self) -> List[AddressContract]:
        content = self.get_content()

        reservas = []

        for reserva in content:
            computer_name, mac_address, ip_address = reserva.split(',')

            reservas.append(
                {
                    'computer_name': computer_name,
                    'mac_address': mac_address,
                    'ip_address': ip_address.replace("\n", ""),
                }
            )

        return reservas
