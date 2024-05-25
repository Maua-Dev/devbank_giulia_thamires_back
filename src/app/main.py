from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .environments import Environments

from .repo.transacao_repository_mock import TransacaoRepositoryMock

from .errors.entity_errors import ParamNotValidated

from .enums.transacao_tipo_enum import TransacaoTipoEnum

from .entities.transacao import Transacao

from .entities.usuario import Usuario


app = FastAPI()

repo = Environments.get_transacao_repo()()

@app.get("/transacao/get_all_transacao")
def get_all_transacao():
    transacao = repo.get_all_transacao()
    return {
        "transacao": [transacao.to_dict() for transacao in transacao]
    }

@app.get("/transacao/{transacao_id}")
def get_transacao(transacao_id: int):
    validation_transacao_id = Transacao.validate_transacao_id(transacao_id=transacao_id)
    if not validation_transacao_id[0]:
        raise HTTPException(status_code=400, detail=validation_transacao_id[1])
    
    Transacao = repo.get_transacao(transacao_id)
    
    if Transacao is None:
        raise HTTPException(status_code=404, detail="Item Not found")
    
    return {
        "transacao_id": transacao_id,
        "item": Transacao.to_dict()    
    }

@app.post("/transacao/create_transacao", status_code=201)
def create_transacao(request: dict):
    transacao_id = request.get("transacao_id")
    
    validation_transacao_id = Transacao.validate_transacao_id(transacao_id=transacao_id)
    if not validation_transacao_id[0]:
        raise HTTPException(status_code=400, detail=validation_transacao_id[1])
    
    Transacao = repo.get_transacao(transacao_id)
    if Transacao is not None:
        raise HTTPException(status_code=409, detail="Transacao already exists")
    
    valor = request.get("valor")
    timestamp = request.get("timestamp")
    transacao_tipo = request.get("transacao_tipo")
    if transacao_tipo is None:
        raise HTTPException(status_code=400, detail="Transacao type is required")
    if type(transacao_tipo) != str:
        raise HTTPException(status_code=400, detail="Transação tipo must be a string")
    if transacao_tipo not in [possible_type.value for possible_type in TransacaoTipoEnum]:
        raise HTTPException(status_code=400, detail="Transação Tipo is not a valid one")
    
    admin_permission = request.get("admin_permission")
    
    try:
        Transacao = Transacao(valor=valor, timestamp=timestamp, transacao_tipo=TransacaoTipoEnum[transacao_tipo])
    except ParamNotValidated as err:
        raise HTTPException(status_code=400, detail=err.message)
    
    transacao_response = repo.create_transacao(Transacao, transacao_id)
    return {
        "transacao_id": transacao_id,
        "transacao": transacao_response.to_dict()    
    }
    
@app.delete("/transacao/delete_trasacao")
def delete_transacao(request: dict):
    transacao_id = request.get("transacao_id")
    
    validation_transacao_id = Transacao.validate_transacao_id(transacao_id=transacao_id)
    if not validation_transacao_id[0]:
        raise HTTPException(status_code=400, detail=validation_transacao_id[1])
    
    Transacao = repo.get_transacao(transacao_id)
    
    if Transacao is None:
        raise HTTPException(status_code=404, detail="Transação Not found")
    
    if Transacao.admin_permission == True:
        raise HTTPException(status_code=403, detail="Transação Not found")
    
    transacao_deleted = repo.delete_transacao(transacao_id)
    
    return {
        "transacao_id": transacao_id,
        "transacao": transacao_deleted.to_dict()    
    }
    
@app.put("/transacao/update_transacao")
def update_transacao(request: dict):
    transacao_id = request.get("transacao_id")
    
    validation_transacao_id = Transacao.validate_transacao_id(transacao_id=transacao_id)
    if not validation_transacao_id[0]:
        raise HTTPException(status_code=400, detail=validation_transacao_id[1])
    
    Transacao = repo.get_transacao(transacao_id)
    
    if Transacao is None:
        raise HTTPException(status_code=404, detail="Transação Not found")
    
    valor = request.get("valor")
    timestamp = request.get("timestamp")
    transacao_tipo = request.get("transacao_tipo")
    
    transacao_type_value = request.get("transacao_type")
    if transacao_type_value != None:
        if type(transacao_type_value) != str:
            raise HTTPException(status_code=400, detail="Transação type must be a string")
        if transacao_type_value not in [possible_type.value for possible_type in TransacaoTipoEnum]:
            raise HTTPException(status_code=400, detail="Transação Tipo is not a valid one")
        transacao_type = TransacaoTipoEnum[transacao_type_value]
    else:
        transacao_type = None
        
    transacao_updated = repo.update_transacao(transacao_id, valor, timestamp, transacao_type, transacao_tipo)
    
    return {
        "transacao_id": transacao_id,
        "transacao": transacao_updated.to_dict()    
    }
    


handler = Mangum(app, lifespan="off")
