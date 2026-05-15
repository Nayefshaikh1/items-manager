class AuthManager:

    def __init__(self):

        self.current_user = None

    def login(self, user):

        self.current_user = user

    def logout(self):

        self.current_user = None

    def require_login(self):

        if not self.current_user:

            raise PermissionError(
                "Login required"
            )