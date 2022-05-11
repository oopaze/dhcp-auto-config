from typing import List, TypedDict

from .FileHandler import FileHandler


class AddressContract(TypedDict):
    computer_name: str
    mac_address: str
    ip_address: str


class ParserAddress(FileHandler):
    def parser(self) -> List[AddressContract]:
        content = self.get_content()

        computers = []

        for computer in content:
            computer_name, mac_address, ip_address = computer.split(',')

            computers.append(
                {
                    'computer_name': computer_name,
                    'mac_address': mac_address,
                    'ip_address': ip_address.replace("\n", ""),
                }
            )

        return computers
