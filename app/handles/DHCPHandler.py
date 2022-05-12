from typing import List

from app import DHCP_FILEPATH, DHCP_REQUIRED_CONFIG_FILEPATH, RESERVAS_FILEPATH
from app.handles.FileHandler import FileHandler
from app.handles.ParserHandle import AddressContract, ParserAddress
from app.utils.get_moment import get_moment

HOST_TEMPLATE = """
host {name} {{
    hardware ethernet    {mac};
    fixed-address        {ip};
}}
"""


class DHCPHandler:
    def get_dhcp_conf(self, as_str: bool = True):
        file_handler = FileHandler(DHCP_FILEPATH)
        return file_handler.get_content(as_str=as_str)

    def get_reservas(self):
        file_handler = ParserAddress(RESERVAS_FILEPATH)
        reservas = file_handler.parser()
        return reservas

    def generate_hosts_from_reservas(self):
        content = ""

        for reserva in self.get_reservas():
            content += self.tranform_reserva_into_host(reserva)

        return content

    def tranform_reserva_into_host(self, reserva: AddressContract):
        return HOST_TEMPLATE.format(
            name=reserva["computer_name"],
            mac=reserva["mac_address"],
            ip=reserva["ip_address"],
        )

    def get_reservas_from_dhcp_conf(self) -> List[AddressContract]:
        content = self.get_dhcp_conf(as_str=False)
        reservas = []

        for idx, line in enumerate(content):
            if line.strip().startswith("host"):
                host = content[idx : idx + 3]
                reservas.append(self.format_host(host))

        return reservas

    def format_host(self, host: List[str]) -> AddressContract:
        computer_name = host[0].split(" ")[1]
        mac_address = host[1].split("    ")[2].replace(";\n", "")
        ip_address = host[2].split("        ")[1].replace(";\n", "")

        return {
            "computer_name": computer_name,
            "mac_address": mac_address,
            "ip_address": ip_address,
        }

    def create_dhcp_conf_file(self, content: str):
        requied_dhcp_handler = FileHandler(DHCP_REQUIRED_CONFIG_FILEPATH)
        required_dhcp_conf = requied_dhcp_handler.get_content(as_str=True)

        content = required_dhcp_conf + content

        FileHandler.create_file(DHCP_FILEPATH, content)

    def create_backup_file(self):
        moment = get_moment()
        content = self.get_dhcp_conf()
        filename = f"backup-{moment}.conf"

        FileHandler.create_file(
            filepath=f"fixtures/backups/dhcpd.conf/{filename}", content=content
        )
