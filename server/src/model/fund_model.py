class Fund:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def __str__(self):
        return (f"Balance Details:\n"
                f"Account No : {self.account_no}\n"
                f"Balance      : {self.balance}")

class Transfer:
    def __init__(self, transfer_id, sender_account, receiver_account, amount, date):
        self.transfer_id = transfer_id
        self.sender = sender_account
        self.receiver = receiver_account
        self.amount = amount
        self.date = date

    def __str__(self):
        return (f"Transfer Details :\n"
                f"Transfer Id: {self.transfer_id}"
                f"Sender Account No: {self.sender}"
                f"Receiver Account No: {self.receiver}"
                f"Trasfer Amount : {self.amount}"
                f"Trasfer Date : {self.date}")