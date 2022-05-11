from app.handles.FileHandler import FileHandler
from app.handles.ParserHandle import AddressContract, ParserAddress
from app.utils.get_today_date import get_today_date

HOST_TEMPLATE = """
host {name} {{
    hardware ethernet    {mac};
    fixed-address        {ip};
    max-lease-time       84600;
}}
"""


class DHCPHandler:
    DHCP_FILEPATH = "/etc/dhcp/dhcpd.conf"
    RESERVAS_FILEPATH = "fixtures/RESERVAS.txt"

    def get_dhcp_conf(self):
        file_handler = FileHandler(self.DHCP_FILEPATH)
        dhcp_file_content = file_handler.get_content(as_str=True)
        return dhcp_file_content

    def get_reservas_conf(self):
        file_handler = ParserAddress(self.RESERVAS_FILEPATH)
        reservas = file_handler.parser()
        return reservas

    def get_hosts_from_reservas(self):
        content = ""

        for reserva in self.get_reservas_conf():
            content += self.tranform_reserva_into_host(reserva)

        return content

    def tranform_reserva_into_host(self, reserva: AddressContract):
        return HOST_TEMPLATE.format(
            name=reserva["computer_name"],
            mac=reserva["mac_address"],
            ip=reserva["ip_address"],
        )

    def create_dhcp_conf_file(self, content: str):
        requied_dhcp_handler = FileHandler('fixtures/required_dhcp.conf')
        required_dhcp_conf = requied_dhcp_handler.get_content(as_str=True)

        content = required_dhcp_conf + content

        moment = get_today_date()
        FileHandler.create_file(f"fixtures/dhcp.conf/dhcp-{moment}.conf", content)

    def create_backup_file(self):
        moment = get_today_date()
        content = self.get_dhcp_conf()
        filename = f"backup-{moment}.conf"

        FileHandler.create_file(
            filepath=f"fixtures/backups/{filename}", content=content
        )
