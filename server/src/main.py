from src.model.user_model import User
from src.services.user_services import open_account, view_account, close_account
from src.utils._id_generator import generate_account_number
from src.services.fund_services import check_balance

while 1:
    ch = int(input("Please choose anyone option.\n1. Open Account \n2. View Account\n3. Close Account\n4. View Balance\n5. Exit : "))

    match ch:
        case 1:
            name = input("Please enter your name : ")
            email = input("Please enter your email : ")
            username = input("Please enter your username : ")
            phone = input("Please enter your phone : ")
            password = input("Please enter your password : ")

            userid = generate_account_number()
            user = User(account_no=userid,name=name, email=email, username=username, phone=phone,           password=password)

            open_account(user)

        case 2:
            account_number = input("Please enter your account no : ")
            view_account(account=account_number)

        case 3:
            account_number = input("Please enter your account no : ")
            close_account(account_no=account_number)

        case 4:
            account_number = input("Please enter your account no : ")
            check_balance(account_number)

        case 5:
            break