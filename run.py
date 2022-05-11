from app import App

from app.implementations.menu_option import MenuOption

from app.actions.atualizar_faixa_ip import atualizar_faixa_ip
from app.actions.dhcp.restart import restart
from app.actions.dhcp.start import start
from app.actions.dhcp.stop import stop
from app.actions.add_computer import add_computer
from app.actions.show_reservas import show_reservas

menu_options = [
    MenuOption('Atualizar faixa de ip do DHCP', atualizar_faixa_ip),
    MenuOption('Acrescentar máquina com reserva de IP', add_computer),
    MenuOption('Listar as reservas já existentes', show_reservas),
    MenuOption('Start', start),
    MenuOption('Stop', stop),
    MenuOption('Restart', restart),
]

if __name__ == '__main__':
    app = App(menu_options)

    app.run()
