import pytest

from src.app.entities.usuario import Usuario
from src.app.enums.usuario_type_enum import UsuarioTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

#with pytest.raises(ParamNotValidated):
#            Usuario(name="test", agency="0000", account="00000-0", current_balance=1000.0)

class Test_Usuario: 
    def test_usuario(self):
        usuario = Usuario("test", "0000", "00000-0", 1000.0)
        assert usuario.name == "test"
        assert usuario.agency == "0000"
        assert usuario.account == "00000-0"
        assert usuario.current_balance == 1000.0

#validate name
    def test_usuario_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            Usuario(agency="0000", account="00000-0", current_balance=1000.0)

    def test_usuario_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name=100, agency="0000", account="00000-0", current_balance=1000.0)       

#validate agency
    def test_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", account="00000-0", current_balance=1000.0)

    def test_agency_type_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency=0000, account="00000-0", current_balance=1000.0)

    def test_agency_len_is_not_4(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="000", account="00000-0", current_balance=1000.0)

    def test_agency_is_not_numeric(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="AAAA", account="00000-0", current_balance=1000.0)

#validate account
    def test_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", current_balance=1000.0)

    def test_account_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", account=00000-0, current_balance=1000.0)

    def test_account_len_is_not_6(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", account="0000-0", current_balance=1000.0)

    def test_account_tracinho(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", account="0000000", current_balance=1000.0)

    def test_account_is_not_numeric(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", account="000A0-0", current_balance=1000.0)

#validate balance
    def test_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", account="00000-0")

    def test_balance_is_less_than_0(self):
        with pytest.raises(ParamNotValidated):
            Usuario(name="test", agency="0000", account="00000-0", current_balance=-1000.0)