import os

from app.handles.DHCPHandler import DHCPHandler
from app.handles.ReservaHandler import ReservaHandler
from app.implementations.Parser import Parser
from app.shared.defaults import OUTPUT_ERROR_TEMPLATE, OUTPUT_SUCCESS_TEMPLATE


def start():
    parser = Parser()

    try:
        dhcp_handler = DHCPHandler()
        dhcp_handler.generate_base_config_file()

        reservas_handler = ReservaHandler()
        reservas = reservas_handler.get_reservas()
        hosts = parser.transform_reservas_into_host(reservas)

        print("Gerando backup do arquivo dhcpd.conf")
        print("Criando novo arquivo dhcp")
        dhcp_handler.update_dhcpd_file(hosts)

        print("Iniciando DHCP server")
        os.system("/etc/init.d/isc-dhcp-server start")
    except FileNotFoundError:
        return OUTPUT_ERROR_TEMPLATE.format("Arquivo dhcpd.conf não encontrado")

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP iniciado com sucesso")
