from app.file_handles.ComputerHandle import ComputerHandle

FILENAME = 'fixtures/pc-list.csv'
NEW_COMPUTER_TEMPLATE = '\n{name},{mac},{ip}'


def add_computer():
    print('Adicionando máquina')
    computer_handle_bundle = ComputerHandle(FILENAME)

    new_computer = NEW_COMPUTER_TEMPLATE.format(name='foo', mac='01', ip='02')
    computer_handle_bundle.add_line(new_computer)
