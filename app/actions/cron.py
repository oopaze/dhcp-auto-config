from app import RESERVAS_FILEPATH
from app.handles.CSVHandle import listToCSV
from app.handles.DHCPHandler import DHCPHandler
from app.handles.FileHandler import FileHandler


def cron_execution():
    print("Executando via cron")

    dhcp_handler = DHCPHandler()
    reservas = dhcp_handler.get_hosts_from_conf()

    reservas_as_csv = listToCSV(reservas)

    FileHandler.create_file(RESERVAS_FILEPATH, reservas_as_csv)
