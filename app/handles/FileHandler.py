from typing import List, Union


class FileHandler:
    READ_MODE = "r"
    APPEND_MODE = "a"
    WRITE_MODE = "w"

    _filename: str = None

    def __init__(self, filename: str):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    def add_line(self, line: str):
        with open(self.filename, self.APPEND_MODE) as file:
            file.write(line)

    def create_file(filepath: str, content):
        with open(filepath, FileHandler.WRITE_MODE) as file:
            file.write(content)
            file.close

    def get_content(self, as_str: bool = False) -> Union[List[str], str]:
        content = None
        with open(self.filename, self.READ_MODE) as file:
            if as_str:
                content = file.read()
            else:
                content = file.readlines()

        return content