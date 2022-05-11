class ComputerHandle:
    READ_MODE = "r"
    APPEND_MODE = "a"

    _filename: str = None

    def __init__(self, filename: str):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    def add_line(self, line: str):
        with open(self.filename, self.APPEND_MODE) as file:
            file.write(line)

        return True

    def parser(self):
        content = None
        with open(self.filename, self.READ_MODE) as file:
            content = file.readlines()

        computers = []

        for computer in content:
            computer_name, mac_address, ip_address = computer.split(',')

            computers.append(
                {
                    'computer_name': computer_name,
                    'mac_address': mac_address,
                    'ip_address': ip_address,
                }
            )

        return computers
