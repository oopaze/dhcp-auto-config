from app import OUTPUT_SUCCESS_TEMPLATE

from app.handles.FileHandler import FileHandler
from app.handles.ReservaCreator import ReservaCreator
from app.handles.CSVHandle import dictToCSV

FILENAME = 'fixtures/RESERVAS.txt'


def add_reserva():
    reservas_handler = ReservaCreator()

    reserva = reservas_handler.get_fields()
    reserva_as_str = dictToCSV(reserva)

    address_file_handler = FileHandler(FILENAME)
    address_file_handler.add_line(reserva_as_str)

    return OUTPUT_SUCCESS_TEMPLATE.format(content="Reserva Adicionada com sucesso")
