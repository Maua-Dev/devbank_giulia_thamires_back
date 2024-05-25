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

@app.post("/deposit")
def create_deposit(request: dict):
    

    return{
        "current_balance": 1000.0,
        "timestamp": 1690482853890 
    }

handler = Mangum(app, lifespan="off")
