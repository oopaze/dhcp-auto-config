from typing import Callable, List, Union

from app.implementations.MenuOption import MenuOption


class Menu:
    TEMPLATE_MENU: str = "{number} - {menu_text}"

    def __init__(self, menu_options: List[MenuOption], sair_command: Callable):
        sair_command = MenuOption('Sair', sair_command)
        self._menu_options = [sair_command, *menu_options]

    @property
    def menu_options(self):
        return self._menu_options

    def get_action(self, idx: Union[str, int]):
        try:
            idx = int(idx)
            return self.menu_options[idx].action
        except (TypeError, IndexError, ValueError):
            return self.error_action

    def error_action(self):
        return '\033[91mOpção Inválida\033[0m'

    def show(self, brakeline: bool = False):
        if brakeline:
            print()

        for idx, menu in enumerate(self.menu_options):
            menu_option = self.TEMPLATE_MENU.format(
                number=idx, menu_text=menu.menu_text
            )
            print(menu_option)
