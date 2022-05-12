from argparse import ArgumentParser

from app import App
from app.actions.cron import cron_execution

from app.implementations.menu_option import MenuOption

from app.actions.atualizar_faixa_ip import atualizar_faixa_ip
from app.actions.dhcp.restart import restart
from app.actions.dhcp.start import start
from app.actions.dhcp.stop import stop
from app.actions.add_reserva import add_reserva
from app.actions.show_reservas import show_reservas

menu_options = [
    MenuOption('Atualizar faixa de ip do DHCP', atualizar_faixa_ip),
    MenuOption('Acrescentar máquina com reserva de IP', add_reserva),
    MenuOption('Listar as reservas já existentes', show_reservas),
    MenuOption('Start', start),
    MenuOption('Stop', stop),
    MenuOption('Restart', restart),
]

if __name__ == '__main__':
    parser = ArgumentParser(description='DHCP auto config')
    parser.add_argument("--cron", type=bool, default=False)
    args = parser.parse_args()

    if args.cron:
        cron_execution()
    else:
        app = App(menu_options)
        app.run()
