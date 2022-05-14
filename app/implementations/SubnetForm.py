from app.implementations.AbstractForm import Form
from app.shared.contracts import SubnetContract
from app.shared.defaults import SUBNET_TEMPLATE


class SubnetForm(Form):
    def __init__(self):
        default_values = {
            "ip": None,
            "mask": None,
            "faixa": None,
            "gateway": None,
            "dns": None,
        }

        super().__init__(SUBNET_TEMPLATE, default_values, SubnetContract)

    def generate_data(self) -> SubnetContract:
        is_validated = False

        while not (is_validated):
            self.get_field("Enderço de IP", "ip")
            self.get_field("Máscara", "mask")
            self.get_field("Faixa de IP", "faixa")
            self.get_field("Gateway", "gateway")
            self.get_field("DNS", "dns")

            if self.confirm_fields():
                is_validated = True

        return self.values
