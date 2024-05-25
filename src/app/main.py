from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.transacao_repository_mock import TransacaoRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.transacao_tipo_enum import TransacaoTipoEnum

from .entities.transacao import Transacao

from .entities.usuario import Usuario

from .repo.usuario_repository_mock import UsuarioRepositoryMock

app = FastAPI()

repo_user = UsuarioRepositoryMock()
repo_transacao = TransacaoRepositoryMock()

@app.get("/")
def get_api(name: str, agency: str, account: str, current_balance: float):


    return{
        "name": "Vitor Soller",
        "agency": "0000",
        "account": "00000-0",
        "current_balance": 1000.0
    }

@app.get("/history")
def get_history(type: str, value: float, current_balance: float, timestamp: float):

    return{
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

#deposito
@app.post("/deposit")
def create_deposit(request: dict):

    deposit_request = {
        "2": 1,
        "5": 2,
        "10": 3,
        "20": 4,
        "50": 5 ,
        "100": 6,
        "200": 7
    }
    total_deposit = sum(int(note) * int(quantity) for note, quantity in deposit_request.items())
    current_balance = request.get("current_balance")

# erro
    if total_deposit == 2 * current_balance:
        return {"status_code": 403, "message": "Depósito suspeito"}

    return{
        "current_balance": 1000.0,
        "timestamp": 1690482853890
    }

handler = Mangum(app, lifespan="off")
