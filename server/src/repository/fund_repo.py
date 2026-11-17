from src.model.fund_model import Fund, Transfer

Funds : list[Fund]=[]

Transfers : list[Transfer]=[]


def _find_account_index(account_no):
    for i in range(len(Funds)):
        if Funds[i].account_no==account_no:
            return i
    return None

def check_account_balance(account_no):
    index = _find_account_index(account_no)
    
    if index is None:
        return " User Not Found"
    return Funds[index]