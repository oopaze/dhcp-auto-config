from app import OUTPUT_SUCCESS_TEMPLATE, RESERVAS_FILEPATH
from app.handles.CSVHandle import CSVHandle
from app.handles.DHCPHandler import DHCPHandler
from app.handles.FileHandler import FileHandler
from app.utils.get_moment import get_moment


def cron_execution():
    print("Executando via cron")

    print("Fazendo backup das reservas")
    moment = get_moment()
    backup_file_name = f"fixtures/backups/reservas/RESERVA-{moment}.txt"
    FileHandler.copy_file(RESERVAS_FILEPATH, backup_file_name)

    print("Atualizando Reservas")
    dhcp_handler = DHCPHandler()

    reservas = dhcp_handler.get_reservas_from_dhcp_conf()

    reservas_as_csv = CSVHandle.list_to_csv(reservas)

    FileHandler.create_file(RESERVAS_FILEPATH, reservas_as_csv)
    print(OUTPUT_SUCCESS_TEMPLATE.format(content="Reservas atualizadas com sucesso"))
