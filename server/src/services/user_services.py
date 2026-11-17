from src.model.user_model import User
from src.repository.user_repo import open_user_account, display_account, close_user_account

def open_account(User:User):

    if User.name is None or User.email is None or User.username is None or User.phone is None or User.password is None:
        raise ValueError("Please enter the all correct value.")

    accnt_no = open_user_account(user=User)
    print(f"You account is created successfully. Your account Number is {accnt_no}")


def view_account(account=None):
    if account is None:
        raise ValueError("Please enter the account number")
    
    user = display_account(account_no=account)
    print(user)


def update_account():
    pass


def close_account(account_no=None):

    if account_no is None:
        raise ValueError("Please enter valid acccount no.")

    result = close_user_account(account_no)
    print(result)
