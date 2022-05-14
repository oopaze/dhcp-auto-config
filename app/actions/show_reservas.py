from app.handles.ReservaHandler import ReservaHandler
from app.shared.defaults import (
    OUTPUT_ERROR_TEMPLATE,
    OUTPUT_SUCCESS_TEMPLATE,
    RESERVA_TEMPLATE,
)


def show_reservas():
    try:
        reserva_handler = ReservaHandler()
        reservas = reserva_handler.get_reservas()
    except FileNotFoundError:
        return OUTPUT_ERROR_TEMPLATE.format(
            content="Arquivo de reservas não encontrado"
        )

    for reserva in reservas:
        print(RESERVA_TEMPLATE.format(**reserva))

    return OUTPUT_SUCCESS_TEMPLATE.format(content="Reservas listadas com sucesso.")
