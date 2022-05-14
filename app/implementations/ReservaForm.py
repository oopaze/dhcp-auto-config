from app.implementations.AbstractForm import Form
from app.shared.contracts import ReservaContract
from app.shared.defaults import RESERVA_TEMPLATE


class ReservaForm(Form):
    def __init__(self):
        default_values = {"name": None, "MAC": None, "IP": None}
        super().__init__(RESERVA_TEMPLATE, default_values, ReservaContract)

    def generate_data(self) -> ReservaContract:
        is_validated = False

        while not (is_validated):
            self.get_field("Nome", "name")
            self.get_field("endereço MAC", "MAC")
            self.get_field("endereço de IP", "IP")

            if self.confirm_fields():
                is_validated = True

        return self.values
