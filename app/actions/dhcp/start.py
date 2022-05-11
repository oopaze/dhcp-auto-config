import os
from app import OUTPUT_SUCCESS_TEMPLATE


def start():
    print("Criando backup do arquivo atual do DHCP")
    print("Gerando novo arquivo de configuração DHCP")
    print("Salvando configuração")
    print("Startando DHCP")

    os.system("sudo /etc/init.d/isc-dhcp-server start")

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP iniciado com sucesso")
