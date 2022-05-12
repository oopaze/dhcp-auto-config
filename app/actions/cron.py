from app import OUTPUT_SUCCESS_TEMPLATE, RESERVAS_FILEPATH
from app.handles.CSVHandle import listToCSV
from app.handles.DHCPHandler import DHCPHandler
from app.handles.FileHandler import FileHandler
from app.utils.get_today_date import get_today_date


def cron_execution():
    print("Executando via cron")

    print("Fazendo backup das reservas")
    moment = get_today_date()
    FileHandler.copy_file(
        RESERVAS_FILEPATH, f"fixtures/backups/reservas/RESERVA-{moment}.txt"
    )

    print("Atualizando Reservas")
    dhcp_handler = DHCPHandler()

    reservas = dhcp_handler.get_hosts_from_conf()

    reservas_as_csv = listToCSV(reservas)

    FileHandler.create_file(RESERVAS_FILEPATH, reservas_as_csv)
    print(OUTPUT_SUCCESS_TEMPLATE.format(content="Reservas atualizadas com sucesso"))
