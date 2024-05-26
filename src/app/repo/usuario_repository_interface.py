from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.usuario import Usuario


class IUsuarioRepository(ABC):
    
    
    @abstractmethod
    def get_all_usuarios(self) -> List[Usuario]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def get_usuario(self, usuario_id: int) -> Optional[Usuario]:
        '''
        Returns the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_usuario(self, item: Usuario, usuario_id: int) -> Usuario:
        '''
        Creates a new item in the database
        '''
        pass
    
    @abstractmethod
    def delete_usuario(self, usuario_id: int) -> Usuario:
        '''
        Deletes the item with the given id.
        If the item does not exist, returns None
        '''
        
    @abstractmethod
    def update_usuario(self, usuario_id:int, name: str = None, agency: str = None, account: str = None, current_balance: float = None) -> Usuario:
        '''
        Updates the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    

    