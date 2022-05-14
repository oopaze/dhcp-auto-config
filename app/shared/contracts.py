from calendar import c
from typing import TypedDict


class SubnetContract(TypedDict):
    ip: str
    mask: str
    faixa: str
    gateway: str
    dns: str


class ReservaContract(TypedDict):
    name: str
    MAC: str
    IP: str
