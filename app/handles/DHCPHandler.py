from app.handles.FileHandler import FileHandler
from app.utils.get_today_date import get_today_date


class DHCPHandler:
    DHCP_FILEPATH = "/etc/dhcp/dhcpd.conf"

    def get_dhcp_conf(self):
        try:
            file_handler = FileHandler(self.DHCP_FILEPATH)
            dhcp_file_content = file_handler.get_content(as_str=True)

        except IndexError:
            ...

        return dhcp_file_content

    def create_backup_file(self):
        moment = get_today_date()
        content = self.get_dhcp_conf()
        filename = f"backup-{moment}.conf"

        FileHandler.create_file(
            filepath=f"fixtures/backups/{filename}", content=content
        )
