import pytest
from src.app.entities.transacao import Transacao
from src.app.enums.transacao_tipo_enum import TransacaoTipoEnum
from src.app.repo.transacao_repository_mock import TransacaoRepositoryMock

class Test_TransacaoRepositoryMock:
    def test_get_all_transacao(self):
        repo = TransacaoRepositoryMock()
        assert all([transacao_expect == transacao for transacao_expect, transacao in zip(repo.transacao.values(), repo.get_all_transacao())])

    def test_get_transacao(self):
        repo=TransacaoRepositoryMock()
        transacao = repo.get_transacao(transacao_id=1)
        assert transacao == repo.transacao.get(1)

    def test_create_transacao(self):
        repo = TransacaoRepositoryMock()
        len_before= len(repo.transacao)
        transacao= Transacao(valor=1000.0, timestamp=1690482853890, transacao_tipo=TransacaoTipoEnum.withdraw)
        repo.create_transacao(transacao=transacao, transacao_id=0)
        len_after = len(repo.transacao)
        assert len_after == len_before + 1
        assert repo.transacao.get(0) == transacao

    def test_delete_transacao(self):
        repo = TransacaoRepositoryMock()
        transacao_expected_to_be_deleted = repo.transacao.get(1)
        len_before = len(repo.transacao)

        Transacao=repo.delete_transacao(transacao_id=1)
        len_after = len(repo.transacao)
        assert len_after == len_before - 1
        assert Transacao == transacao_expected_to_be_deleted

    def test_update_transacao(self):
        repo = TransacaoRepositoryMock()
        transacao = Transacao(valor=1000.0, timestamp=1690482853890, transacao_tipo=TransacaoTipoEnum.withdraw)
        transacao_updated= repo.update_transacao(transacao_id=1, valor=transacao.valor, timestamp=transacao.timestamp, transacao_tipo=transacao.transacao_tipo)

        assert transacao_updated == transacao
        assert repo.transacao.get(1)== transacao