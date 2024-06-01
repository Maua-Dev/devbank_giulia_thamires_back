import pytest
from src.app.entities.usuario import Usuario
from src.app.enums.usuario_type_enum import UsuarioTypeEnum
from src.app.repo.usuario_repository_mock import UsuarioRepositoryMock

class Test_UsuarioRepositoryMock:
    def test_get_all_usuarios(self):
        repo = UsuarioRepositoryMock()
        assert all([usuario_expect == usuario for usuario_expect, usuario in zip(repo.usuarios.values(), repo.get_all_usuarios())])

    def test_get_usuario(self):
        repo = UsuarioRepositoryMock()
        usuario = repo.get_usuario(usuario_id=1)
        assert usuario == repo.usuarios.get(1)

    def test_create_usuario(self):
        repo = UsuarioRepositoryMock()
        len_before = len(repo.usuarios)
        usuario = Usuario(name="test", account="00000-0", agency="0000",current_balance=1000.0)
        repo.create_usuario(usuario=usuario, usuario_id=0)
        len_after = len(repo.usuarios)
        assert len_after == len_before + 1
        assert repo.usuarios.get(0) == usuario

    def test_delete_usuario(self):
        repo = UsuarioRepositoryMock()
        usuario_expected_to_be_deleted = repo.usuarios.get(1)
        len_before = len(repo.usuarios)
        
        usuario = repo.delete_usuario(usuario_id=1)
        len_after = len(repo.usuarios)
        assert len_after == len_before - 1
        assert usuario == usuario_expected_to_be_deleted


    def test_update_usuario(self):
        repo = UsuarioRepositoryMock()
        usuario = Usuario(name="test", account="00000-0", agency="0000", current_balance=1000.0)
        usuario_updated = repo.update_usuario(usuario_id=1, name=usuario.name, account=usuario.account, agency=usuario.agency, current_balance=usuario.current_balance)
        
        assert usuario_updated == usuario
        assert repo.usuarios.get(1) == usuario
