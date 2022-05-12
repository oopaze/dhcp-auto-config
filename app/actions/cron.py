from app.actions.dhcp.start import start


def cron_execution():
    print("Executando via cron")
    start()
