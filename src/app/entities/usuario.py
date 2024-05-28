from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class Usuario:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None):
        validation_name = self.validate_name(name=name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name

        validation_agency = self.validate_agency(agency=agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency

        validation_account = self.validate_account(account=account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_current_balance = self.validate_balance(balance=current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current balance", validation_current_balance[1])
        self.current_balance = current_balance


    @staticmethod
    def validate_name(name: str) -> Tuple[bool,str]:
        if name is None: #feito
            return False, "name is required"
        if type(name) != str: #feito
            return False, "Name must be a string"
        return True, ""
    
    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool,str]:
        if agency is None: #feito
            return False, "agency is required"
        if type(agency) != str: #feito
            return False, "agency must be a string"
        if len(agency) != 4: #feito
            return False, "agency must have 4 digits"
        if not agency.isnumeric(): #feito
            return False, "agency must be numeric"
        return True, ""
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool,str]:
        if account is None: #feito
            return False, "account is required"
        if type(account) != str: #feito
            return False, "account must be a string"
        if len(account) != 7: #feito
            return False, "account must have 6 digits"
        if account[5] != "-": #feito
            return False, "invalid format"
        account_splited = account.split("-")
        if not account_splited[0].isnumeric() or not account_splited[1].isnumeric(): #feito
            return False, "invalid format"
        return True, ""
    
    @staticmethod
    def validate_balance(balance: float) -> Tuple[bool,float]:
        if balance is None: #feito
            return False, "balance is required"
        if type(balance) != float:
            return False, "balance must be a float"
        if balance < 0: #feito
            return False, "balance can't be less than 0"
        return True, ""
        