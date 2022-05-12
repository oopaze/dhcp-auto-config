class ReservaCreator:
    fields = [
        {"name": "Nome", "key": "name"},
        {"name": "endereço MAC", "key": "MAC"},
        {"name": "endereço de IP", "key": "IP"},
    ]
    fields_length = len(fields)
    values = {"name": None, "MAC": None, "IP": None}

    RESERVA_TEMPLATE = 'Nome={nome} | MAC={mac} | IP={ip}'

    def get_field(self, name: str, key: str):
        value = input(f"Digite o {name}: ")
        self.values[key] = value

    def get_fields(self):
        is_validated = False

        while not (is_validated):
            self.get_field("Nome", "name")
            self.get_field("endereço MAC", "MAC")
            self.get_field("endereço de IP", "IP")

            print("\nConfirma Reserva?")
            if self.confirm_fields():
                is_validated = True

        return self.values

    def confirm_fields(self):
        name = self.values["name"]
        mac = self.values["MAC"]
        ip = self.values["IP"]

        reserva = self.RESERVA_TEMPLATE.format(nome=name, mac=mac, ip=ip)

        is_confirmed = input(f"{reserva}\nS/N: ").lower() == "s"

        return is_confirmed
