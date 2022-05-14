from app.shared.defaults import OUTPUT_ERROR_TEMPLATE, OUTPUT_SUCCESS_TEMPLATE
from app.handles.ReservaHandler import ReservaHandler
from app.implementations.ReservaForm import ReservaForm


def add_reserva():
    try:
        reserva_creator = ReservaForm()
        reserva = reserva_creator.generate_reserva()

        reserva_handler = ReservaHandler()
        reserva_handler.add_reserva(reserva)
    except FileNotFoundError:
        return OUTPUT_ERROR_TEMPLATE.format(
            content="Arquivo de Reservas não encontrado"
        )

    return OUTPUT_SUCCESS_TEMPLATE.format(content="Reserva Adicionada com sucesso")
