from typing import List, Optional
from app.handles.FileHandler import FileHandler
from app.implementations.Parser import Parser
from app.shared.defaults import DHCP_BASE_CONFIG_FILE, DHCP_FILEPATH
from app.shared.contracts import ReservaContract


class DHCPHandler:
    _filepath = DHCP_FILEPATH
    _parser = Parser()
    base_config = ""

    @property
    def filepath(self):
        return self._filepath

    @property
    def parser(self):
        return self._parser

    @property
    def buffer(self):
        return FileHandler(self.filepath)

    def get_hosts(self, asReserva: bool = False) -> List[ReservaContract]:
        hosts = []

        content = self.buffer.get_content()
        for idx, line in enumerate(content):
            found_host = line.strip().startswith('host')

            if found_host:
                host = "".join(content[idx : idx + 4])

                if asReserva:
                    host = self._parser.transform_host_into_reserva(host)

                hosts.append(host)

        return hosts

    def add_host(self, host: ReservaContract):
        host = self.parser.transform_reserva_into_host(host)
        self.buffer.add_line(host)

    def add_hosts(self, hosts: List[ReservaContract]):
        for host in hosts:
            self.add_host(host)

    def generate_base_config_file(self):
        content = self.buffer.get_content(as_str=True)

        hosts = self.get_hosts()

        for host in hosts:
            content = content.replace(host, "")

        while content.endswith("\n\n"):
            content = content[0:-1]
        
        self.base_config = content

    def update_dhcpd_file(self, hosts: str, asReservas: bool = False, subnet: str = ""):
        self.buffer.create_backup_file("dhcpd.conf", isReserva=False)

        if asReservas:
            hosts = self.parser.transform_reservas_into_host(hosts)

        content = self.base_config + subnet + hosts
        self.buffer.create_file(filepath=DHCP_FILEPATH, content=content)
