from app.actions.dhcp.start import start
from app.actions.dhcp.stop import stop


def restart():
    stop()
    start()
