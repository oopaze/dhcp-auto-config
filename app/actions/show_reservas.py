from app.shared.defaults import OUTPUT_SUCCESS_TEMPLATE


def show_reservas():
    return OUTPUT_SUCCESS_TEMPLATE.format(content="Reservas listadas com sucesso.")
