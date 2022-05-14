from typing import List
from app.implementations.SubnetForm import SubnetForm
from app.shared.contracts import ReservaContract
from app.shared.defaults import HOST_TEMPLATE, SUBNET_TEMPLATE


class Parser:
    def transform_reserva_into_host(self, reserva: ReservaContract) -> str:
        return HOST_TEMPLATE.format(**reserva)

    def transform_host_into_reserva(self, host: str) -> ReservaContract:
        host = host.split("\n")

        name = host[0].strip().split(" ")[1]
        mac = host[1].strip().split(" ")[-1].replace(";", "")
        ip = host[2].strip().split(" ")[-1].replace(";", "")

        return {"IP": ip, "MAC": mac, "name": name}

    def transform_reservas_into_host(self, reservas: List[ReservaContract]):
        hosts = ""

        for reserva in reservas:
            hosts += self.transform_reserva_into_host(reserva)

        return hosts

    def transform_subnet_in_dhcp(self, subnet: SubnetForm):
        return SUBNET_TEMPLATE.format(**subnet)
