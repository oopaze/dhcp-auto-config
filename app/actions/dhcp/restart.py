from app.actions.dhcp.start import start
from app.actions.dhcp.stop import stop
from app.shared.defaults import OUTPUT_SUCCESS_TEMPLATE


def restart():
    stop()
    start()

    return OUTPUT_SUCCESS_TEMPLATE.format(content="DHCP reiniciado com sucesso")
