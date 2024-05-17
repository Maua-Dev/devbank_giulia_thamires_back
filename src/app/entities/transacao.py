from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class Transacao:
    
    valor: float
    timestamp: float
    tipo: str

    def __init__(self,valor: float, tipo: str, timestamp: float):
        pass
        
    @staticmethod
    def validate_valor(valor: float) -> Tuple[bool,float]:
        if valor is None:
            return False, "valor is required"
        if type(valor) != float:
            return False, "valor must be a float"
        return True

    @staticmethod
    def validate_tipo(tipo: str) -> Tuple[bool,str]:
        if tipo is None:
            return False, "tipo is required"
        if type(tipo) != str:
            return False, "tipo must be a string"
        return True
        
    
    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool,float]:
        if timestamp is None:
            return False, "timestamp is required"
        if type(timestamp) != float:
            return False, "timestamp must be a float"
        return True
    