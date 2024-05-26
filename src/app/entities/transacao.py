from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.transacao_tipo_enum import TransacaoTipoEnum

class Transacao:
    valor: float
    timestamp: float
    transacao_tipo:TransacaoTipoEnum

    def __init__(self,valor: float,timestamp: float, transacao_tipo: TransacaoTipoEnum):
        validation_valor = self.validate_valor(valor)
        if validation_valor[0] is False:
            raise ParamNotValidated("valor", validation_valor[1])
        self.valor = valor
        
        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

        validation_transacao_tipo= self.validate_transacao_tipo(transacao_tipo)
        if validation_transacao_tipo[0] is False:
            raise ParamNotValidated("tipo", validation_transacao_tipo[1])
        self.transacao_tipo = transacao_tipo
        
    @staticmethod
    def validate_valor(valor: float) -> Tuple[bool,float]:
        if valor is None:
            return False, "valor is required"
        if type(valor) != float:
            return False, "valor must be a float"
        return True, ""
        
    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool,float]:
        if timestamp is None:
            return False, "timestamp is required"
        if type(timestamp) != float:
            return False, "timestamp must be a float"
        return True, ""
    
    @staticmethod
    def validate_transacao_tipo(transacao_tipo:TransacaoTipoEnum) -> Tuple[bool,TransacaoTipoEnum]:
        if transacao_tipo is None:
            return False, "tipo is required"
        if type(transacao_tipo) != TransacaoTipoEnum:
            return False, "Transação tipo must be a TransacaoTipoEnum"
        return True, ""