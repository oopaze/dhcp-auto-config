from app.handles.DHCPHandler import DHCPHandler
from app.implementations.Parser import Parser
from app.implementations.SubnetForm import SubnetForm
from app.shared.defaults import OUTPUT_ERROR_TEMPLATE, OUTPUT_SUCCESS_TEMPLATE


def atualizar_faixa_ip():
    subnet_form = SubnetForm()
    parser = Parser()

    subnet = subnet_form.generate_data()
    dhcp_subnet = parser.transform_subnet_in_dhcp(subnet)

    try:
        dhcp_handle = DHCPHandler()
        dhcp_handle.generate_base_config_file()

        hosts = "".join(dhcp_handle.get_hosts())
        dhcp_handle.update_dhcpd_file(hosts, subnet=dhcp_subnet)
    except FileNotFoundError:
        return OUTPUT_ERROR_TEMPLATE.format(content="Arquivo dhcpd.conf não encontrado")

    return OUTPUT_SUCCESS_TEMPLATE.format(content="Faixa de IP atualizada com sucesso")
