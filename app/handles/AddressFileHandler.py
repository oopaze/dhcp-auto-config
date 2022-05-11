from typing import List


class AddressFileHandler:
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

    def get_content(self) -> List[str]:
        content = None
        with open(self.filename, self.READ_MODE) as file:
            content = file.readlines()

        return content
