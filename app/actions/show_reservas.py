from app.handles.ParserHandle import ParserAddress

FILENAME = 'fixtures/RESERVAS.txt'
COMPUTER_TEMPLATE = '{idx} - Nome={nome} | MAC={mac} | IP={ip}'


def show_reservas():
    print('Reservas: ')
    parser = ParserAddress(FILENAME)
    computers = parser.parser()

    for idx, computer in enumerate(computers):
        computer_str = COMPUTER_TEMPLATE.format(
            idx=idx + 1,
            nome=computer['computer_name'],
            mac=computer['mac_address'],
            ip=computer['ip_address'],
        )

        print(computer_str, end='')

    return ""
