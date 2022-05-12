from os import environ as env
from typing import List

from app.implementations.menu import Menu
from app.implementations.menu_option import MenuOption

OUTPUT_SUCCESS_TEMPLATE = "\033[92m{content}\033[0m"
OUTPUT_ERROR_TEMPLATE = "\033[91m{content}\033[0m"

DHCP_FILEPATH = env.get("DHCP_FILEPATH", "fixtures/dhcpd.conf")
DHCP_REQUIRED_CONFIG_FILEPATH = env.get(
    "DHCP_REQUIRED_CONFIG_FILEPATH", "fixtures/defaults/dhcp.conf"
)
RESERVAS_FILEPATH = env.get("RESERVAS_FILEPATH", "fixtures/RESERVAS.txt")


class App:
    ON = 'on'
    OFF = 'off'

    _running = OFF

    def __init__(self, menu_options: List[MenuOption]):
        self.menu = Menu(menu_options=menu_options, sair_command=self.stop)

    @property
    def running(self):
        return self._running

    def stop(self):
        self._running = self.OFF

    def start(self):
        print("Iniciando aplicação")
        self._running = self.ON

    def run(self):
        self.start()
        is_app_on = self.running == self.ON

        while is_app_on:
            self.menu.show(brakeline=True)

            option = input('Option: ')
            action_selected = self.menu.get_action(option)
            print()
            action_message = action_selected()

            if action_message:
                print(f"\n{action_message}")

            is_app_on = self.running == self.ON

        print("Encerrando aplicação...")
