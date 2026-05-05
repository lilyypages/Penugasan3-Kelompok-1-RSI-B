class AuthModel:
    def __init__(self, account_id: int, email: str, role_id: int):
        self.account_id = account_id
        self.email = email
        self.role_id = role_id