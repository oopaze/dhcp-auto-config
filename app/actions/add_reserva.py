from app import DHCP_FILEPATH, OUTPUT_SUCCESS_TEMPLATE, RESERVAS_FILEPATH
from app.handles.DHCPHandler import DHCPHandler

from app.handles.FileHandler import FileHandler
from app.handles.ReservaCreator import ReservaCreator
from app.handles.CSVHandle import listToCSV


def add_reserva():
    reservas_handler = ReservaCreator()
    dhcp_handler = DHCPHandler()

    reserva = reservas_handler.get_fields()

    reservas = dhcp_handler.get_hosts_from_conf()
    reservas.append(reserva)

    reservas_as_str = listToCSV(reservas)

    FileHandler.create_file(RESERVAS_FILEPATH, reservas_as_str)

    hosts = dhcp_handler.get_hosts_from_reservas()
    dhcp_handler.create_dhcp_conf_file(hosts, DHCP_FILEPATH)

    return OUTPUT_SUCCESS_TEMPLATE.format(content="Reserva Adicionada com sucesso")
