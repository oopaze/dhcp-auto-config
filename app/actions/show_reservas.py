from app.file_handles.ComputerHandle import ComputerHandle

FILENAME = 'fixtures/pc-list.csv'
COMPUTER_TEMPLATE = 'Nome={nome} | MAC={mac} | IP={ip}'


def show_reservas():
    print('Reservas: ')
    computer_handle_bundle = ComputerHandle(FILENAME)
    computers = computer_handle_bundle.parser()

    for computer in computers:
        computer_str = COMPUTER_TEMPLATE.format(
            nome=computer['computer_name'],
            mac=computer['mac_address'],
            ip=computer['ip_address'],
        )

        print(computer_str, end='')
