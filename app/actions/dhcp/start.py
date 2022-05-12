import os

from app import OUTPUT_SUCCESS_TEMPLATE, OUTPUT_ERROR_TEMPLATE
from app.handles.DHCPHandler import DHCPHandler


def start():
    dhcp_handler = DHCPHandler()

    try:
        print("Criando backup do arquivo atual do DHCP")
        dhcp_handler.create_backup_file()

        print("Gerando novo arquivo de configuração DHCP")
        hosts = dhcp_handler.get_hosts_from_reservas()

        print("Salvando configuração")
        dhcp_handler.create_dhcp_conf_file(hosts)

        print("Startando DHCP")
        os.system("/etc/init.d/isc-dhcp-server start")
    except FileNotFoundError:
        return OUTPUT_ERROR_TEMPLATE.format(
            content="Arquivo de configuração não encontrado"
        )

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP iniciado com sucesso")
