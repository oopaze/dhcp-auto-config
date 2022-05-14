from app.shared.defaults import OUTPUT_SUCCESS_TEMPLATE


def cron_execution():
    print(OUTPUT_SUCCESS_TEMPLATE.format(content="Reservas atualizadas com sucesso"))
