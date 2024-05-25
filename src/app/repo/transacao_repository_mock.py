from typing import Dict, Optional, List

from ..enums.transacao_tipo_enum import TransacaoTipoEnum
from ..entities.transacao import Transacao
from .transacao_repository_interface import ITrasacaoRepository


class TransacaoRepositoryMock(ITrasacaoRepository):
    transacao: Dict[int, Transacao]
    
    def __init__(self):
        self.transacao = {
            1: Transacao(name="Barbie", price=48.90, transacao_type=TransacaoTipoEnum.TOY, admin_permission=False),
            2: Transacao(name="Hamburguer", price=38.00, transacao_type=TransacaoTipoEnum.FOOD, admin_permission=False),
            3: Transacao(name="T-shirt", price=22.95, transacao_type=TransacaoTipoEnum.CLOTHES, admin_permission=False),
            4: Transacao(name="Super Mario Bros", price=55.00, transacao_type=TransacaoTipoEnum.GAMES, admin_permission=True)
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
        
        
    def update_item(self, transacao_id:int, valor: float,timestamp: float, transacao_tipo: TransacaoTipoEnum) -> Transacao:
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