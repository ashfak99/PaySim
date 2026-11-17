from src.repository.fund_repo import check_account_balance

def check_balance(account_no : None):

    if account_no is None:
        raise ValueError("User not found")

    user_balance = check_account_balance(account_no)
    print(user_balance)