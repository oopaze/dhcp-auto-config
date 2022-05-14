import os
from typing import List, Union

from app.utils.get_moment import get_moment
from app.shared.defaults import (
    DHCPD_BACKUP_FOLDER,
    RESERVA_BACKUP_FOLDER,
)


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

    @classmethod
    def create_file(cls, filepath: str, content):
        with open(filepath, FileHandler.WRITE_MODE) as file:
            file.write(content)

    @classmethod
    def copy_file(cls, filepath: str, new_filepath: str):
        os.system(f"cat {filepath} > {new_filepath}")

    def create_backup_file(self, backup_filename: str, isReserva: bool = True):
        moment = get_moment()
        backup_filepath = (
            f"{DHCPD_BACKUP_FOLDER}/{moment}-{backup_filename}"
            if isReserva
            else f"{RESERVA_BACKUP_FOLDER}/{moment}-{backup_filename}"
        )

        self.copy_file(self.filename, backup_filepath)

    def get_content(self, as_str: bool = False) -> Union[List[str], str]:
        content = None
        with open(self.filename, self.READ_MODE) as file:
            if as_str:
                content = file.read()
            else:
                content = file.readlines()

        return content
