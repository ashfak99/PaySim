import uuid

def generate_account_number():
    return "NDD" + uuid.uuid4().hex[:10].upper()

def generate_transaction_number():
    return "TXA" + uuid.uuid4().hex[:10].upper()
