from app import OUTPUT_SUCCESS_TEMPLATE
from app.handles.AddressFileHandler import AddressFileHandler
from app.handles.ReservaCreator import ReservaCreator

FILENAME = 'fixtures/RESERVAS.txt'
FIELDS = [
    {"name": "Nome", "key": "name"},
    {"name": "endereço MAC", "key": "MAC"},
    {"name": "endereço de IP", "key": "IP"},
]


def add_computer():
    reservas_handler = ReservaCreator(FIELDS)

    reserva = reservas_handler.get_fields()
    reserva_as_str = reservas_handler.values_as_csv(reserva)

    address_file_handler = AddressFileHandler(FILENAME)
    address_file_handler.add_line(reserva_as_str)

    return OUTPUT_SUCCESS_TEMPLATE.format(content="Reserva Adicionada com sucesso")
