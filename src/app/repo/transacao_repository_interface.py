from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.transacao_tipo_enum import TransacaoTipoEnum

from ..entities.transacao import Transacao


class ITrasacaoRepository(ABC):
    
    
    @abstractmethod
    def get_all_transacao(self) -> List[Transacao]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def get_transacao(self, transacao_id: int) -> Optional[Transacao]:
        '''
        Returns the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_transacao(self, transacao: Transacao, transacao_id: int) -> Transacao:
        '''
        Creates a new item in the database
        '''
        pass
    
    @abstractmethod
    def delete_transacao(self, transacao_id: int) -> Transacao:
        '''
        Deletes the item with the given id.
        If the item does not exist, returns None
        '''
        
    @abstractmethod
    def update_transacao(self, transacao_id:int, valor: float,timestamp: float, transacao_tipo: TransacaoTipoEnum) -> Transacao:
        '''
        Updates the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    