class User:
    def __init__(self, account_no,name, email, username, phone, password):
        self.account_no = account_no
        self.name = name
        self.email = email
        self.username = username
        self.phone = phone
        self.password = password
        
    def __str__(self):
        return (f"User Details:\n"
                f"Account No : {self.account_no}\n"
                f"Name       : {self.name}\n"
                f"Email      : {self.email}\n"
                f"Username   : {self.username}\n"
                f"Phone      : {self.phone}")