from typing import Callable, Optional


class MenuOption:
    def __init__(self, menu_text: str, action: Optional[Callable] = None):
        self._menu_text = menu_text
        self._action = self.default_action

        if action:
            self._action = action

    @property
    def menu_text(self):
        return self._menu_text

    @property
    def action(self):
        return self._action

    def default_action(self):
        print(self.menu_text)
