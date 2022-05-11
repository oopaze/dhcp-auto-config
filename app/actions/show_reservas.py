from app.handles.ParserHandle import ParserAddress

FILENAME = 'fixtures/RESERVAS.txt'
RESERVA_TEMPLATE = '{idx} - Nome={nome} | MAC={mac} | IP={ip}'


def show_reservas():
    print('Reservas: ')
    parser = ParserAddress(FILENAME)
    reservas = parser.parser()

    for idx, reserva in enumerate(reservas):
        reserva_str = RESERVA_TEMPLATE.format(
            idx=idx + 1,
            nome=reserva['computer_name'],
            mac=reserva['mac_address'],
            ip=reserva['ip_address'],
        )

        print(reserva_str, end='')

    return ""
