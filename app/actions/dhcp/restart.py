from app import OUTPUT_SUCCESS_TEMPLATE

from app.actions.dhcp.start import start
from app.actions.dhcp.stop import stop


def restart():
    stop()
    start()

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP reiniciado com sucesso")
