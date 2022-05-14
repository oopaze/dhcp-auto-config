from os import environ as env

DHCP_BASE_CONFIG_FILE = env.get("DHCP_BASE_CONFIG_FILE", "fixtures/defaults/dhcp.conf")
DHCP_FILEPATH = env.get("DHCP_FILEPATH", "fixtures/dhcpd.conf")

RESERVAS_FILEPATH = env.get("RESERVAS_FILEPATH", "RESERVAS.txt")

BACKUP_FOLDER_PATH = env.get("BACKUPS_FOLDER_PATH", "backups")
RESERVA_BACKUP_FOLDER = f"{BACKUP_FOLDER_PATH}/reservas"
DHCPD_BACKUP_FOLDER = f"{BACKUP_FOLDER_PATH}/dhcpd.conf"

OUTPUT_SUCCESS_TEMPLATE = "\033[92m{content}\033[0m"
OUTPUT_ERROR_TEMPLATE = "\033[91m{content}\033[0m"

RESERVA_TEMPLATE = "Nome={name} | MAC={MAC} | IP={IP}"
