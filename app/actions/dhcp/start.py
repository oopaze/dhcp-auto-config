import os
from app import OUTPUT_SUCCESS_TEMPLATE
from app.handles.DHCPHandler import DHCPHandler


def start():
    dhcp_handler = DHCPHandler()

    print("Criando backup do arquivo atual do DHCP")
    dhcp_handler.create_backup_file()

    print("Gerando novo arquivo de configuração DHCP")
    print("Salvando configuração")
    print("Startando DHCP")

    os.system("sudo /etc/init.d/isc-dhcp-server start")

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP iniciado com sucesso")
