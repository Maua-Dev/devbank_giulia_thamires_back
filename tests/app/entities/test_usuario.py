import pytest

from src.app.entities.usuario import Usuario
from src.app.enums.usuario_type_enum import UsuarioTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_Usuario: #deu errado
    def test_usuario(self):
        usuario = Usuario("test", "0000", "00000-0", 1000.0)
        assert usuario.name == "test"
        assert usuario.agency == "0000"
        assert usuario.account == "00000-0"
        assert usuario.current_balance == 1000.0

    def test_usuario_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="teste", agency="0000", account="00000-0", current_balance=1000.0)

    def test_usuario_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name=100, agency="0000", account="00000-0", current_balance=1000.0)             