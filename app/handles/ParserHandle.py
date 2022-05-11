from turtle import st
from typing import List, TypedDict

from .AddressFileHandler import AddressFileHandler


class AddressContract(TypedDict):
    computer_name: str
    mac_address: str
    ip_address: str


class ParserAddress(AddressFileHandler):
    def parser(self) -> List[AddressContract]:
        content = self.get_content()

        computers = []

        for computer in content:
            computer_name, mac_address, ip_address = computer.split(',')

            computers.append(
                {
                    'computer_name': computer_name,
                    'mac_address': mac_address,
                    'ip_address': ip_address,
                }
            )

        return computers
