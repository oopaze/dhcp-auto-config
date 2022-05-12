from os import environ as env

from app.handles.CSVHandle import listToCSV
from app.handles.DHCPHandler import DHCPHandler
from app.handles.FileHandler import FileHandler

RESERVAS_FILEPATH = env.get("RESERVAS_FILEPATH", "fixtures/RESERVAS.txt")


def cron_execution():
    print("Executando via cron")

    dhcp_handler = DHCPHandler()
    reservas = dhcp_handler.get_hosts_from_conf()

    reservas_as_csv = listToCSV(reservas)

    FileHandler.create_file(RESERVAS_FILEPATH, reservas_as_csv)
