from typing import List

from app.handles.FileHandler import FileHandler
from app.shared.contracts import ReservaContract
from app.shared.defaults import RESERVAS_FILEPATH
from app.utils.csv import dict_to_csv, list_to_csv


class ReservaHandler:
    _filepath = RESERVAS_FILEPATH
    reservas: List[ReservaContract] = []

    @property
    def filepath(self) -> str:
        return self._filepath

    @property
    def buffer(self):
        return FileHandler(self.filepath)

    def get_reservas(self) -> List[ReservaContract]:
        for reserva in self.buffer.get_content():
            name, mac, ip = reserva.split(",")
            ip = ip.replace('\n', '')
            self.reservas.append({'IP': ip, 'MAC': mac, 'name': name})

        return self.reservas

    def add_reserva(self, reserva: ReservaContract):
        reserva = dict_to_csv(reserva)
        self.buffer.add_line(reserva)

    def add_reservas(self, reservas: List[ReservaContract]):
        reservas = list_to_csv(reservas)
        self.buffer.add_line(reservas)

    def update_reservas_file(self, reservas: List[ReservaContract]):
        self.buffer.create_backup_file(backup_filename="backup.txt")

        reservas = list_to_csv(reservas)
        self.buffer.create_file(RESERVAS_FILEPATH, reservas)
