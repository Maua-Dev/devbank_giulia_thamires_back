from fastapi.exceptions import HTTPException
import pytest
from src.app.entities.usuario import Usuario
from src.app.entities.transacao import Transacao
from src.app.enums.transacao_tipo_enum import TransacaoTipoEnum
from src.app.enums.usuario_type_enum import UsuarioTypeEnum
from src.app.main import get_history, create_deposit, create_withdraw
from src.app.repo.transacao_repository_mock import TransacaoRepositoryMock
from src.app.repo.usuario_repository_mock import UsuarioRepositoryMock

class Test_Main:
    def test_get_history(self):
        repo = TransacaoRepositoryMock()
        all_transacao = 1
        response = get_history(all_transacao=all_transacao)
        assert response == {
            "all_transactions": [
              {
                "type": "deposit",
                "value": 100.0,
                "current_balance": "1000.0",
                "timestamp": 1690482853890
              },
              {  
                "type": "withdraw",
                "timestamp": 1691707985704.6152,
                "current_balance": 700.0,
                "value": 300
              }
           ]
        }
        
    def test_create_deposit(self):
        repo = TransacaoRepositoryMock()
        
        body = {
            "current_balance": 1000.0,
            "timestamp": 1690482853890
        }
        with pytest.raises(HTTPException) as err:
            create_deposit(request=body)
        response = create_deposit(request=body)
        assert response == {'current_balance':1000.0,'timestap':1690482853890}
    
    def test_create_withdraw(self):
        repo = TransacaoRepositoryMock()
        
        body = {
            'current_balance': 1000.0,
            'timestamp': 1690482853890 
        }
        with pytest.raises(HTTPException) as err:
            create_withdraw(request=body)
    
    
        
  