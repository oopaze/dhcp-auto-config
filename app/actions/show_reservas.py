from app import RESERVAS_FILEPATH
from app.handles.ParserHandle import ParserAddress

RESERVA_TEMPLATE = '{idx} - Nome={nome} | MAC={mac} | IP={ip}'


def show_reservas():
    print('Reservas: ')
    parser = ParserAddress(RESERVAS_FILEPATH)
    reservas = parser.parser()

    for idx, reserva in enumerate(reservas):
        reserva_str = RESERVA_TEMPLATE.format(
            idx=idx + 1,
            nome=reserva['computer_name'],
            mac=reserva['mac_address'],
            ip=reserva['ip_address'],
        )

        print(reserva_str, end='\n')

    return ""
