from src.model.user_model import User
from src.repository.fund_repo import Funds
from src.model.fund_model import Fund

users : list[User] = []


def open_user_account(user : User):
    users.append(user)
    new_fund = Fund(user.account_no,1000)
    Funds.append(new_fund)
    return user.account_no


def find_user_index(account_no):
    for i in range(len(users)):
        if users[i].account_no==account_no:
            return i
    return None


def close_user_account(account_no):
    index = find_user_index(account_no=account_no)

    if(index==None):
        raise ValueError("User Not Found")
    
    users.pop(index)
    return "Account successfully closed."


def display_account(account_no):
    for i in range(len(users)):
        if users[i].account_no==account_no:
            return users[i]
    print("User not found")