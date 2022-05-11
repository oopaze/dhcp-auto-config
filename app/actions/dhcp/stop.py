import os

from app import OUTPUT_SUCCESS_TEMPLATE


def stop():
    print("Parando servidor DHCP")

    os.system("/etc/init.d/isc-dhcp-server stop")

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP parado com sucesso")
