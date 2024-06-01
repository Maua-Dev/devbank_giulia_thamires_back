from typing import Dict, Optional, List

from ..enums.usuario_type_enum import UsuarioTypeEnum
from ..entities.usuario import Usuario
from .usuario_repository_interface import IUsuarioRepository


class UsuarioRepositoryMock(IUsuarioRepository):
    usuario: Dict[int, Usuario]
    
    def __init__(self):
        self.usuarios = {
            1: Usuario(name="Soller", account="00000-0", agency="0000",current_balance=1000.0)
        }
        
    def get_all_usuarios(self) -> List[Usuario]: #feito
        return self.usuarios.values()
    
    def get_usuario(self, usuario_id: int) -> Optional[Usuario]: #feito
        return self.usuarios.get(usuario_id, None)
    
    def create_usuario(self, usuario: Usuario, usuario_id: int) -> Usuario: #feito
        
        self.usuarios[usuario_id] = usuario
        return usuario
    
    def delete_usuario(self, usuario_id: int) -> Usuario: #feito
        usuario = self.usuarios.pop(usuario_id, None)
        return usuario
        
        
    def update_usuario(self, usuario_id:int, name: str = None, agency: str = None, account: str = None, current_balance: float = None) -> Usuario: #feito
        usuario = self.usuarios.get(usuario_id, None)
        if usuario is None:
            return None
        
        if name is not None:
            usuario.name = name
        if agency is not None:
            usuario.agency = agency
        if account is not None:
            usuario.account = account
        if current_balance is not None:
            usuario.current_balance = current_balance
        self.usuarios[usuario_id] = usuario
        
        return usuario
        
    
    