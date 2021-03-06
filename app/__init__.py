from typing import List

from app.implementations.Menu import Menu
from app.implementations.MenuOption import MenuOption


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
