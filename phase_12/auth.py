import uuid


class AuthManager:

    def __init__(self):

        # Current active user
        self.current_user = None

        # token -> user mapping
        self.sessions = {}

    # ---------- LOGIN ----------

    def login(self, user):

        # Save current user
        self.current_user = user

        # Generate unique token
        token = str(uuid.uuid4())

        # Store session
        self.sessions[token] = user

        # Return token to API
        return token

    # ---------- LOGOUT ----------

    def logout(self):

        self.current_user = None

    # ---------- REQUIRE LOGIN ----------

    def require_login(self):

        if not self.current_user:

            raise PermissionError(
                "Login required"
            )

    # ---------- TOKEN VALIDATION ----------

    def authenticate_token(
        self,
        token
    ):

        user = self.sessions.get(token)

        if not user:

            raise PermissionError(
                "Invalid token"
            )

        # Restore current user
        self.current_user = user

        return user