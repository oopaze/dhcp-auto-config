from app.handles.DHCPHandler import DHCPHandler
from app.handles.ReservaHandler import ReservaHandler
from app.shared.defaults import OUTPUT_ERROR_TEMPLATE, OUTPUT_SUCCESS_TEMPLATE


def cron_execution():
    try:
        dhcp_handler = DHCPHandler()
        reservas = dhcp_handler.get_hosts(asReserva=True)
    except FileNotFoundError:
        print(OUTPUT_ERROR_TEMPLATE.format(content="Arquivo dhcpd.conf não encontrado"))
        return

    reservas_handler = ReservaHandler()
    reservas_handler.update_reservas_file(reservas)
    print(OUTPUT_SUCCESS_TEMPLATE.format(content="Reservas atualizadas com sucesso"))
