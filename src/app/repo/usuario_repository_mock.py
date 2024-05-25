from typing import Dict, Optional, List

from ..enums.usuario_type_enum import UsuarioTypeEnum
from ..entities.usuario import Usuario
from .usuario_repository_interface import IUsuarioRepository


class UsuarioRepositoryMock(IUsuarioRepository):
    usuario: Dict[int, Usuario]
    
    def __init__(self):
        self.usuarios = {
            1: Usuario(name="Barbie", price=48.90, usuario_type=UsuarioTypeEnum.TOY, admin_permission=False),
            2: Usuario(name="Hamburguer", price=38.00, usuario_type=UsuarioTypeEnum.FOOD, admin_permission=False),
            3: Usuario(name="T-shirt", price=22.95, usuario_type=UsuarioTypeEnum.CLOTHES, admin_permission=False),
            4: Usuario(name="Super Mario Bros", price=55.00, usuario_type=UsuarioTypeEnum.GAMES, admin_permission=True)
        }
        
    def get_all_usuarios(self) -> List[Usuario]:
        return self.usuarios.values()
    
    def get_usuario(self, usuario_id: int) -> Optional[Usuario]:
        return self.usuarios.get(usuario_id, None)
    
    def create_usuario(self, usuario: Usuario, usuario_id: int) -> Usuario:
        
        self.usuarios[usuario_id] = usuario
        return usuario
    
    def delete_usuario(self, usuario_id: int) -> Usuario:
        usuario = self.usuarios.pop(usuario_id, None)
        return usuario
        
        
    def update_usuario(self, usuario_id:int, name: str = None, agency: str = None, account: str = None, current_balance: float = None) -> Usuario:
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
        
    
    