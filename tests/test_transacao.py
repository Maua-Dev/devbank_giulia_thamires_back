import pytest
from src.app.entities.transacao import Transacao
from src.app.enums.transacao_tipo_enum import TransacaoTipoEnum
from src.app.errors.entity_errors import ParamNotValidated

class Test_Transacao:
    def test_transacao(self):
        transacao=Transacao(1000.0, 1690482853890 , TransacaoTipoEnum.withdraw)
        assert transacao.valor == 1000.0
        assert transacao.timestamp == 1690482853890
        assert transacao.transacao_tipo == TransacaoTipoEnum.withdraw

        def test_transacao_valor_is_none(self):
            with pytest.raises(ParamNotValidated):
                Transacao(timestamp=1690482853890, transacao_tipo=TransacaoTipoEnum.withdraw )

        def test_transacao_valor_is_not_float(self):
            with pytest.raises(ParamNotValidated):
                Transacao(valor="1000.0", timestamp=1690482853890, transacao_tipo=TransacaoTipoEnum.withdraw)

        def test_transacao_timestamp_is_none(self):
            with pytest.raises(ParamNotValidated):
                Transacao(valor=1000.0, transacao_tipo=TransacaoTipoEnum.withdraw)

        def test_transacao_timestamp_is_not_float(self):
            with pytest.raises(ParamNotValidated):
                Transacao(valor=1000.0, timestamp="1690482853890", transacao_tipo=TransacaoTipoEnum.withdraw)

        def test_transacao_transacao_tipo_is_none(self):
            with pytest.raises(ParamNotValidated):
                Transacao(valor=1000.0, timestamp=1690482853890)

        def test_transacao_transacao_is_not_withdrawn(self):
            with pytest.raises(ParamNotValidated):
                Transacao(valor=1000.0, timestamp=1690482853890, transacao_tipo=TransacaoTipoEnum.deposit)