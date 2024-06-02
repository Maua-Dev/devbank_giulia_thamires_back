from typing import Dict, Optional, List

from ..enums.transacao_tipo_enum import TransacaoTipoEnum
from ..entities.transacao import Transacao
from .transacao_repository_interface import ITrasacaoRepository


class TransacaoRepositoryMock(ITrasacaoRepository):
    transacao: Dict[int, Transacao]

def __init__(self):
        self.transacao = {
            1: Transacao(valor=1000.0 ,timestamp=1690482853890,transacao_tipo=TransacaoTipoEnum.withdraw),
        }

def get_all_transacao(self) -> List[Transacao]:
    return self.transacao.values()

def get_transacao(self, transacao_id: int) -> Optional[Transacao]:
    return self.transacao.get(transacao_id, None)

def create_transacao(self, transacao: Transacao, transacao_id: int) -> Transacao:
    self.transacao[transacao_id] = transacao
    return transacao

def delete_transacao(self, transacao_id: int) -> Transacao:
    transacao = self.transacao.pop(transacao_id, None)
    return transacao


def update_transacao(self, transacao_id:int, valor: float=None, timestamp: int = None, transacao_tipo: TransacaoTipoEnum= None) -> Transacao:
    transacao = self.transacao.get(transacao_id, None)
    if transacao is None:
        return None

    if valor is not None:
        transacao.valor = valor
    if timestamp is not None:
        transacao.timestamp = timestamp
    if transacao_tipo is not None:
        transacao.transacao_tipo = transacao_tipo
    self.transacao[transacao_id] = transacao

    return transacao